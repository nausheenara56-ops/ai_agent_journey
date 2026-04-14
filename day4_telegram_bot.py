from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant. Answer the user's question clearly and concisely.

Question: {question}
""")

chain = prompt | llm | StrOutputParser()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am Nausheen's AI Assistant.\n"
        "Ask me anything and I will answer!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"User asked: {user_message}")
    
    await update.message.reply_text("Thinking...")
    
    response = chain.invoke({"question": user_message})
    
    await update.message.reply_text(response)

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    app = Application.builder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is running. Open Telegram and message @NausheenAI_bot")
    print("Press Ctrl+C to stop.\n")
    
    app.run_polling()

if __name__ == "__main__":
    main()