
#streamlit for UI/app interface
import streamlit as st

#Import dependancies
from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain

#path to weights
PATH = 'C:/Users/andre/AppData/Local/nomic.ai/GPT4All/ggml-gpt4all-j-v1.3-groovy.bin'

#Instance of LLM
llm = GPT4All(model=PATH, verbose=True)


#Title
st.title('Simple Chatbot')

#Create a text input box for the user
prompt = st.text_input('Input your prompt here')

#If the user hits enter 
if prompt:
    #Then pass prompt to LLM
    response = llm(prompt)
    # write it out to screen
    st.write(response)
