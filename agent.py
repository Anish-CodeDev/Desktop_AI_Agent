from typing import TypedDict,Sequence,Annotated
from dotenv import load_dotenv
from langgraph.graph import StateGraph,START,END
from langchain_core.messages import BaseMessage,SystemMessage,HumanMessage
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio
from client import main
from google import genai
from gemini import run_tools
client = genai.Client()

load_dotenv()

class AgentState(TypedDict):
    messages:Annotated[Sequence[BaseMessage],add_messages]

@tool
def cli_filesystem_tool(message:str):
    """Use this tool for any file system operations like copying or moving or executing any command line operations, capture the user's message
    When it comes to file system operations just extract the text from the user's query, do not use any command line operations
    """
    print(message)

    res = asyncio.run(run_tools(message,"D:\\Anish\\ComputerScience\\Computer science\\Machine Learning\\mcp\\mcp_servers\\cli\\server.py"))
    print(res)
    if eval(res) == True:

        res = asyncio.run(main(message,'D:\\Anish\\ComputerScience\\Computer science\\Machine Learning\\mcp\\mcp_servers\\cli\\server.py'))
    return res
tools = [cli_filesystem_tool]
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash').bind_tools(tools)


def agent(state:AgentState):
    instruction = SystemMessage(content='You are my AI Assistant, answer to your best ability')
    response = llm.invoke([instruction] + state['messages'])

    return {"messages":response}


def should_continue(state:AgentState):
    if state['messages'][-1].tool_calls:
        return "continue"
    else:
        return "end"
    
graph = StateGraph(AgentState)

graph.add_node("agent",agent)

tool_node = ToolNode(tools=tools)
graph.add_node("tool_node",tool_node)


graph.add_edge(START,'agent')

graph.add_conditional_edges(
    'agent',
    should_continue,
    {
        "continue":"tool_node",
        "end":END
    }

)

graph.add_edge('tool_node','agent')

app = graph.compile()
conversational_history = []

user_input = input("User: ")

while user_input !='exit':
    conversational_history.append(HumanMessage(content=user_input))
    result = app.invoke({"messages":conversational_history})
    conversational_history = result['messages']
    print("AI: ",dict(conversational_history[-1])['content'])
    user_input = input("User: ")