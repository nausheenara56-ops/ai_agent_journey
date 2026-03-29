from dotenv import load_dotenv              ## loads your secret API key from .env file
from langchain_groq import ChatGroq                  # # connects to Groq's free LLM
from langchain_core.prompts import PromptTemplate        ## builds reusable prompts
from langchain_core.output_parsers import StrOutputParser   ## # cleans the output


load_dotenv()                   # # reads your GROQ_API_KEY from .env — without this, no connection

llm = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in 3 bullet points for a beginner."
)

chain = prompt | llm | StrOutputParser()

result = chain.invoke({"topic": "how to make money with AI"}) 
print(result)
