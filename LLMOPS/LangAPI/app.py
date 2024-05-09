from fastapi import FastAPI


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

import uvicorn
import os

from langchain_community.llms import Ollama


from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


app = FastAPI(
    title="Langchain Server",
    verrsion = "1.0",
    description  = "A simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
    
)

model = ChatOpenAI()

llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me a message on {topic} with 100 words, and misspell atleast 5 words with capital letters")

prompt2 = ChatPromptTemplate.from_template("Write me a poem on {topic}")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)