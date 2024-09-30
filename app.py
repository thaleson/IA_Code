import streamlit as st
from utils.api import get_code_suggestions
from utils.code import is_programming_related
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the Streamlit page settings
st.set_page_config(page_title="IACODE", page_icon="💻", layout="wide")

# Apply CSS styles to the page
with open("static/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Title of the application
st.title("🤖 Assistente de Código Inteligente")  # Adds the application title

st.write("💻 Descreva seu problema ou código e o que deseja, e receba sugestões e melhorias!")

# Input area for code/problem with placeholder
problem_input = st.text_area("📝 Insira seu código ou descreva seu problema aqui:", 
                              height=200, 
                              placeholder="Exemplo: Erro de sintaxe no código Python.")

# Input area for what the user desires with placeholder
request_input = st.text_area("🔍 O que você deseja saber ou melhorar:", 
                              height=100, 
                              placeholder="Exemplo: Melhorar a performance do código.")

# Button to obtain suggestions
if st.button("📩 Obter Soluções"):
    if problem_input and request_input:
        if is_programming_related(problem_input) or is_programming_related(request_input):
            with st.spinner("🔄 Processando..."):
                response = get_code_suggestions(problem_input, request_input)
                
                # Section for formatted output
                st.subheader("🔧 Sugestões do Assistente:")
                
                if response:
                    st.markdown(response)
                else:
                    st.warning("⚠️ Sem resposta da API.")
        else:
            st.warning("⚠️ Desculpe, sou uma IA criada para analisar códigos de programação. Por favor, insira apenas questões relacionadas a programação.")
    else:
        st.warning("⚠️ Por favor, preencha ambos os campos.")
