import asyncio
from typing import Optional
from contextlib import AsyncExitStack
import re
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google import genai
from dotenv import load_dotenv
load_dotenv()
gemini = genai.Client() 


def get_result(query,tools):
    tools_with_desc = {
        tool.name:tool.description
    
    for tool in tools
    }
    response = gemini.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"""Given the {query}, decide the tool by the tool's name and description which are represented by triple backticks
            ```{tools_with_desc}```
            Choose the tool best suits the user's query, extract arguments,
            Return the best tool with the key 'tool'and the extracted arguments under the key 'args' in the form of json.
            Remove all the backticks like ``` at any cost.
            """,
    )
    return eval(str(re.sub('json','',response.text)))

class MCPClient:
    def __init__(self):
        self.session:Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()

    async def list_tools(self,loc):
        try:

            server_params = StdioServerParameters(
                command='python',
                args=[loc],
                env=None
            )
            stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
            self.read,self.write = stdio_transport

            self.session = await self.exit_stack.enter_async_context(ClientSession(self.read,self.write))

            await self.session.initialize()

            tools_list = await self.session.list_tools()
            tools_list = tools_list.tools
        
        finally:
            await self.exit_stack.aclose()

        
        return {
             "name":[tool.name for tool in tools_list],
             "desc":[tool.description for tool in tools_list]
        } 
    async def connect_with_server(self,query,loc):
        server_params = StdioServerParameters(
            command='python',
            args=[loc],
            env=None
        )
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.read,self.write = stdio_transport

        self.session = await self.exit_stack.enter_async_context(ClientSession(self.read,self.write))

        await self.session.initialize()


        response = await self.session.list_tools()
        tools = response.tools

        result = get_result(query,tools)

        return result
    
    async def call_tool(self,name,args,loc):
        server_params = StdioServerParameters(
            command='python',
            args=[loc],
            env=None
        )
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.read,self.write = stdio_transport

        self.session = await self.exit_stack.enter_async_context(ClientSession(self.read,self.write))

        await self.session.initialize()
        try:

            response = await self.session.call_tool(name,args)
        
        finally:
            await self.exit_stack.aclose()
        
        return response



client = MCPClient()

async def main(user_inp,loc):
    print(user_inp)
    try:
        #user_inp = input("User: ")
        #while user_inp !='exit':
            
            result = await client.connect_with_server(user_inp,loc=loc)
            tool_name = result['tool']
            args = result['args']
            print(tool_name)
            print(args)
            response = await client.session.call_tool(tool_name,args)

            #print("AI: ",response.content[0].text)
            #user_inp = input("User: ")
            return str(response)
    
    finally:
        await client.exit_stack.aclose()

#asyncio.run(main(''))