from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
'''
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
'''

## Langmith tracking

##prompt template

openai_api_key = "sk-proj-H2pa8KX3tiTFsZEsXG1NT3BlbkFJo8zizliAclmwDujJWE4u"

HUGGINGFACE_API_KEY = "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"

LANGCHAIN_API_KEY ="ls__3eee125da9d440dfa83a4c381483f4bc"



prompt = ChatPromptTemplate.from_messages(
    
    [
        ("system","You are a helpfull assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit

st.title('Langchain demo with openAI')

input_text = st.text_input("Search the topic you want")

#openAI LLM

llm = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key = "sk-proj-H2pa8KX3tiTFsZEsXG1NT3BlbkFJo8zizliAclmwDujJWE4u"
)

output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    
    st.write(chain.invoke({'question':input_text}))