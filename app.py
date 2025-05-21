import streamlit as st
import pandas as pd
import random
import numpy as np

st.title('GohanApp')
st.subheader('Seu app para um arroz perfeito!')
# Cria vetores
tipos_arroz = ['Parboilizado', 'Branco', 'Integral', 'Arbóreo', 'Gohan', 'Negro', 
               'Vermelho', 'da Terra', 'Basmati', 'Carnaroli']
pontos_arroz = ['Soltinho', 'Empapado', 'Queimado', 'Cru', 'Ao dente']

receitas = {'Parboilizado': ['Arroz com nada', 'Arroz sem nada'],
            'Branco': ['Arroz maluco', 'Arroz à grega', 'Arroz de brócolis', 'Arroz com feijão'],
            'Integral': ['Arroz fit', 'Arroz com raiva'],
            'Arbóreo': ['Risoto', 'à Piamontese'],
            'Carnaroli': ['Risoto', 'à Piamontese'],
            'Gohan': ['Poke', 'Sushi'],
            'Negro': ['Arroz negro com polvo'],
            'Vermelho': ['Arroz vermelho com amor'],
            'da Terra': ['Arroz de leite', 'Arrubacão'],
            'Basmati': ['Arroz indiano'],
            }

# Coloca em ordem
tipos_arroz.sort()
pontos_arroz.sort()

with st.sidebar:
    st.image('gohan.jpg')
    nome = st.text_input('Digite seu nome')
    escolha_tipo = st.selectbox(options=tipos_arroz, label='Escolha o seu tipo de arroz favorito')
    escolha_ponto = st.selectbox(options=pontos_arroz, label='Escolha o ponto do seu arroz')
    botao = st.button('Preparar arroz')

if botao:
    receita_escolhida = receitas[escolha_tipo]
    receita_escolhida = random.choice(receita_escolhida)
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header(f'Olá, {nome}!')
        st.write('Vamos preparar sua receita de', escolha_tipo)

        map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])

        st.map(map_data)
    
    with col2:
        st.write(f'Pensamos em uma receita de {receita_escolhida}')
        st.write(f'Para isso, você precisará de {escolha_tipo}')
        st.write(f'O ponto ótimo do seu arroz é em {random.randint(4, 11)} minutos.')
