#interate our code with openai API
import os
openai_key='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'
os.environ["OpenAI_API_KEY"]=openai_key
from langchain.llms import openai
import streamlit as st
from openai import OpenAI
llm=OpenAI(temperature=0.7)

st.title("LAngchain Demo")
input_text=st.text("Search")

if input_text:
    st.write(llm(input_text))
