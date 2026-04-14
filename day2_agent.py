from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

search = DuckDuckGoSearchRun()
tools = [search]

system_message = SystemMessage(content="""You are a helpful AI assistant with access to a web search tool called 'duckduckgo_search'. 
Always use duckduckgo_search to find current information.
Never use any other tool name.""")

agent = create_react_agent(llm, tools, prompt=system_message)

print("Web Search Agent ready. Type 'quit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    result = agent.invoke({"messages": [("human", user_input)]})
    print(f"\nFinal Answer: {result['messages'][-1].content}\n")