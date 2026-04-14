from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import pypdf

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

print("Loading your PDF...")

pdf_text = ""
with open("PROJECT REPORT (2).pdf", "rb") as f:
    reader = pypdf.PdfReader(f)
    for page in reader.pages:
        pdf_text += page.extract_text() + "\n"

print(f"PDF loaded — {len(pdf_text)} characters extracted.")

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Answer the question based only on the document below.

DOCUMENT:
{context}

QUESTION: {question}

Answer clearly and concisely.
""")

chain = prompt | llm | StrOutputParser()

print("\nRAG Chatbot ready. Ask anything about your project!\n")

while True:
    question = input("You: ")
    if question.lower() == "quit":
        break
    answer = chain.invoke({
        "context": pdf_text[:6000],
        "question": question
    })
    print(f"\nAI: {answer}\n")