from google import genai
from dotenv import load_dotenv
from client import MCPClient
import asyncio
load_dotenv()
client = genai.Client()

mcp_client = MCPClient()
async def list_tools(loc):
    tools_list = await mcp_client.list_tools(loc)
    return tools_list
async def run_tools(ques,loc):

    tools_list = await list_tools(loc)
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
            
            Return the response as a list whoose first element is a list comprising of the names of the tools, the second element is a list  whoose elements are dictionaries with key as argument name and value of the key as the value to be passed,comprising of the args to be passed
            like this : 
            """
        ]
    )
    response = eval(res.text)
    if response == 1:
        return True

    tool_names = response[0]
    args = response[1]
    print(args)
    try:

        for i in range(len(tool_names)):
            
            response = await mcp_client.call_tool(tool_names[i],args[i],loc)
    
    except Exception as e:
        return f"An error occured due to: {str(e)}"
    

    return str(dict(response)['content'][0].text)


#status = asyncio.run(run_tools("I would like to copy a file a.txt from one folder documents to another folder folder-2 and then rename the same as test.txt",'D:\\Anish\\ComputerScience\\Computer science\\Machine Learning\\mcp\\mcp_servers\\cli\\server.py'))
#print(status)

#I would like to copy a file a.txt from one folder documents to another folder folder-2 and then rename the same as test.txt"