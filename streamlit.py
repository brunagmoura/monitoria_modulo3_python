import streamlit as st
import pandas as pd

st.write("Sou servidor público")

st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

numero = st.slider('Selecione um número', min_value = 0, max_value = 100)
st.text("Seu número é " + str(numero))

#criando elementos gráficos
'''Informar como colher os dados através de variáveis'''
x = st.checkbox('Sim')
st.write(x)

#fazer o mesmo com alguns dos comandos abaixo
st.title(x)
st.button('Clique')
st.radio('Selecione seu gênero',['Masculino','Feminino'])
st.selectbox('Selecione seu gênero',['Masculino','Feminino'])
st.multiselect('Escolha um departamento',['DCS', 'DE', 'DIR'])
st.select_slider('Selecione uma resposta', ['Ruim', 'Bom', 'Excelente'])
st.slider('Selecione um número', 0,50)
st.number_input('Selecione um número', 0,10)
st.text_input('Endereço de e-mail')
st.date_input('Data de viagem')
st.time_input('Tempo de escola')
st.text_area('Descrição')
st.file_uploader('Atualize uma foto')
st.color_picker('Escolha sua cor favorita')

#mensagens de status
st.success("Você conseguiu!")
st.error("Erro!")
st.warning("Advertência")
st.info("Esta é uma informação")

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})

st.write("Criando uma tabela!")
#tabelas interativas
st.write(df)
#inserindo um selectbox
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])
#O formato de print é diferente de outras versões
#de Python
st.write('Você selecionou: ', opcao)

dfFiltrado = df.loc[df['nomeServidor'] == opcao]
st.write(dfFiltrado)

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#apresentar o dataframe
#https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/27385-localidades.html?=&t=downloads

df.info()
numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))

#quantidade de comunidades por estado
df['NM_UF'].value_counts()

#número de comunidades por estado
st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#dados sobre estatística descritiva
qtdeMunicipios = len(df['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

#os dez municípios com mais comunidades
st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])
