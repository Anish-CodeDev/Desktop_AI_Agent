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
from gemini import run_tools,extract_filename_for_instruction_following
import os
client = genai.Client()

load_dotenv()

class AgentState(TypedDict):
    messages:Annotated[Sequence[BaseMessage],add_messages]

@tool
def system_agent_tool(message:str):
    """Use this tool for any file system operations like copying or moving or executing any command line operations, capture the user's message
    When it comes to file system operations just extract the text from the user's query, do not use any command line operations
    This tool also has the power to generate various files with formatting.
    You can use this tool to open folders.
    Don't use this tool for the opening of files but you can use this for opening programs.

    This tool has the power of encryption files.

    When capturing the input donot use quotes in the captured input

    This tool has the power to open programs and interact with various GUI components
    """
    print(message)
    print('invoked')
    res = asyncio.run(run_tools(message,"D:\\Anish\\ComputerScience\\Computer science\\Machine Learning\\mcp\\mcp_servers\\system_agent\\server.py"))
    print(res)
    '''with open('data.txt','w') as f:
        f.write(res)
        f.close()'''


@tool
def open_file_tool(path:str):
    """
    This tool is used when the user wants to open a specific file of any type
    ARGS: path

    """
    print(path)
    os.startfile(path)
@tool
def deep_research_tool(topic:str):
    """
    This tool is used when the user wants to conduct deep research on  a specific topic
    ARGS: topic
    """
    res = asyncio.run(main("What is " + topic,'D:\\Anish\\ComputerScience\\Computer science\\Machine Learning\\mcp\\mcp_servers\\deep_research\\server.py'))
    return str(res)
@tool
def execute_instructions_from_file(filename:str):
    """
    This tool is used when the user wants the agent to execute instructions from the file
    ARGS: filename

    """
    with open(filename,'r') as f:
            content = f.read()
        
    for c in content.split('\n'):
        instructions.append(HumanMessage(content=c))
        res = agent.invoke({"messages":c})
        instructions = res['messages']
    
    return instructions
tools = [system_agent_tool,open_file_tool,deep_research_tool]
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash').bind_tools(tools)


def agent(state:AgentState):
    
    res  = extract_filename_for_instruction_following(state['messages'])
    if res == "False":

        instruction = SystemMessage(content='You are my AI Assistant, answer to your best ability, your abilities are now extended with the help of various tools. At any cost do not give any error type messages return the tool messages')
        response = llm.invoke([instruction] + state['messages'])
        return {"messages":response}
    else:
        with open(res,'r') as f:
            content = f.read()
        content_str = []
        for c in content.split('\n'):
            content_str.append(c)
        instruction = SystemMessage(content='You are my AI Assistant, answer to your best ability, your abilities are now extended with the help of various tools. At any cost do not give any error type messages return the tool messages')
        response = llm.invoke([instruction] + content_str)
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