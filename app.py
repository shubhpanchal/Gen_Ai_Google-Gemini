import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import streamlit as st

genai.configure(api_key='Your API Key')
model = genai.GenerativeModel('gemini-pro')


def getGeminiresponse(user_input):
    response = model.generate_content(user_input)
    return response.text

st.set_page_config(page_title = "Know your thing😎" ,
                page_icon = "🤖",
                layout = "centered",
                initial_sidebar_state = "collapsed")
  

st.header("Know your thing😎")

user_input = st.text_input("What are you curious about? 🤔💭")

submit = st.button("Find Out")


if submit:
    st.write(getGeminiresponse(user_input=user_input))
