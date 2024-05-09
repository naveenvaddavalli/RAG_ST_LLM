from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_community.llms import Ollama

import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a mean person. Only respond your answer with capital letters by misspealling atleast 5 words in the answer and those mis spelt words are lower case"),
        ("user","Qestion:{question}")
    ]
)

st.title("Langchain with Ollama dashboard")
input_text = st.text_input("Search the topic you want to know")

#OLLAMA

llm = Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


