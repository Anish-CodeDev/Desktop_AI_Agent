from typing import TypedDict,Sequence,Annotated
from dotenv import load_dotenv
from langgraph.graph import StateGraph,START,END
from langchain_core.messages import BaseMessage,SystemMessage,HumanMessage
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
from client import main
import asyncio
load_dotenv()
class AgentState(TypedDict):
    messages:Annotated[Sequence[BaseMessage],add_messages]

@tool
def tool(message:str):
    """Use this tool for any file system operations like copying or moving"""
    print(message)
    return "Done"
tools = []
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

async def test():
    return 'test'
def agent(state:AgentState):
    instruction = SystemMessage(content='You are my AI assistant, just extract the task from the user\'s prompt')

    response = llm.invoke([instruction] + state['messages'])
    #print(dict(response)['content'])
    res = asyncio.run(main(dict(response)['content']))
    print(dict(res)['content'][0].text)
    return {"messages":dict(res)['content'][0].text}

def should_continue(state:AgentState):
    if state['messages'][-1].tool_calls:
        return "continue"
    else:
        return "end"
graph = StateGraph(AgentState)
graph.add_node("agent",agent)
'''
tool_node = ToolNode(tools=tools)
graph.add_node("tool_node",tool_node)'''

graph.add_edge(START,"agent")
'''
graph.add_conditional_edges(
    'agent',
    should_continue,
    {
        "continue":"tool_node",
        "end":END
    }
)'''

#graph.add_edge("tool_node","agent")
graph.add_edge("agent",END)
agent = graph.compile()

conversational_history = []

user_input = input("User: ")

while user_input !='exit':
    conversational_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages":conversational_history})
    conversational_history = result['messages']
    print("AI: ",dict(conversational_history[-1])['content'])
    user_input = input("User: ")