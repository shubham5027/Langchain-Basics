# #interate our code with openai API
import os
import streamlit as streamlit
openai_key='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'
os.environ["OpenAI_API_KEY"]=openai_key
from langchain.llms import OpenAI
import streamlit as st
# from openai import OpenAI


st.title("LAngchain Demo")
input_text=st.text_input("write here")

llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
