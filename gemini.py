from google import genai
from dotenv import load_dotenv
from client import MCPClient
import asyncio
load_dotenv()
client = genai.Client()
ques = 'I would like to copy a file a.txt from one folder folder-1 to another folder folder-2 and then rename the same as b.txt'
mcp_client = MCPClient()
async def list_tools():
    tools_list = await mcp_client.list_tools(ques,"D:\\Anish\\ComputerScience\\Computer science\\Machine Learning\\mcp\\mcp_servers\\cli\\server.py")
    return tools_list
tools_list = asyncio.run(list_tools())
res = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=[
        f"""
        Given the list of tools: {tools_list['desc']}, analyse whether the operation enclosed by triple backticks is possible with these tools or they require the combination of these tools
        ```{ques}```
        Return the 1 if the operation is possible with these tools(one tool)

        If otherwise generate a plan to execute the process with step by step instruction by mentioning the tool names by using the list of tool names to be used

        tool_names: {tools_list['name']}

        Include just the tool names along with the arguments to be passed and not any additonal text
        
        Return the response as a list whoose first element is a list comprising of the names of the tools, the second element is a list  whoose elements are dictionaries with key as arg and val as the value to be passed,comprising of the args to be passed
        """
    ]
)
print(res.text)
#print(type(eval(res.text)))