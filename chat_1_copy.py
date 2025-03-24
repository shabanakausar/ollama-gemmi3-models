# ----------------Enhanced Q&A Chatbot With Gemma3:1b, Gemma3:4b----------------------------------
# ------------------------------------------------------------------------------------------------
# It uses 'Ollama' class of langchain community to generate response to the user query. 
# The user can select the Ollama model from the sidebar and adjust the response parameters
# like temperature and max tokens. The user can ask any question and get the response from 
# the chatbot. The response is generated using the 'generate_response' function which takes
# the user query, Ollama model, temperature, and max tokens as input and returns the response. 
# The response is displayed on the screen. If the user has not entered any question or Ollama 
# API key, it displays a message to enter the question or API key in the settings. The user can
# also enter the Ollama API key in the settings to get the response from the chatbot. The chatbot
#  uses Gemma3:1b and Gemma3:4b models to generate the response to the user query. 
#-------------------------------------------------------------------------------------------------

import streamlit as st
import os
import langchain
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from ollama import chat

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API")
os.environ["HF_API_KEY"] = os.getenv("HF_API_KEY")
os.environ['Geminie_API_KEY'] = os.getenv("Geminie_API_KEY") 
os.environ["LANGCHAIN_PROJECT"] = 'QnA-Chatbot-Ollama'



# Project Template
prompt = ChatPromptTemplate.from_messages(
    [
      ("system", "You are a helpful assistant . PLease provide responses to the user query"),
       ("user", "Question: {question}")
    ]
)

def generate_response(question, llm, temperature, max_tokens):
    llm  = Ollama(model=llm)
    output_parser = StrOutputParser()
    chain = prompt|llm | output_parser
    answer = chain.invoke({'question' : question}) 
    return answer
    

st.title("Enhanced Q&A Chatbot With Gemma3")

st.sidebar.title("Settings")
llm  = st.sidebar.selectbox("Select Ollama Model", ["Gemma3:1b", "Gemma3:4b"])

# adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value = 0.0, max_value = 1.0, value = 0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value = 50, max_value = 300, value = 150)

#Main Interface for using Input
st.write("Go head and ask any Question")
user_input = st.text_input("You :")

if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write("Bot: ", response)
else:
    st.write("Please enter a question to get a response")
