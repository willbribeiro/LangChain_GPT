### Pacotes ###
import os
from apikey import apikey
import streamlit as st # estrutura de aplicação
from langchain.llms import OpenAI # dará o serviço da OpenAI

# disponibilização da chave a para o aplicativo
os.environ['OPENAI_API_KEY'] = apikey

### configuração do aplicativo ###
st.title('Utilizando ChatGPT')
prompt = st.text_input('Coloque o seu prompt aqui')

# criação de uma instância para a API
modelo = OpenAI(temperature=0.9, max_tokens=500)

# se houver um prompt, passar o prompt para a llm, resceber a resposta e escrever na tela
if prompt:
    resposta = modelo(prompt) # resposta da llm ao passa o prompt para ela
    st.write(resposta) # escrever na tela do aplicativo a resposta