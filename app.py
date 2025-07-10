import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key= os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="customised bot", page_icon=":robot_face:")
st.title("myself jarvis ask me anything")

user_question=st.text_input("Ask me")

if st.button("Get answer") and user_question:
    with st.spinner("Thinking..."):
        
        try:
            client=openai
            response= client.chat.completions.create(
                model = "gpt-3.5-turbo" ,
                messages=[{"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_question}
                ],
                temperature=0.7,
                max_tokens=300)
            answer=response.choices[0].message.content
            st.success(answer)
        except Exception as e:
            st.error(f"Error, {e}")

            

