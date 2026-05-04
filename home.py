import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] {
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(
    page_title="Diamond Price Predictor",
    page_icon="💎",
    layout="wide"
)

st.title("Сколько стоит бриллиант? 💎")
col1, col2 = st.columns([1.5, 0.8], gap="large", width=900)

with col2:
    st.image(f'./images/diamonds.jpg')

with col1:

    st.markdown(f"""
               
    Данное приложение создано для оценки стоимости бриллиантов при помощи моделей 
    машинного обучения.
                
    Алгоритмы были обучены на большом объеме данных, что позволяет предсказвать цены
    различных алмазов.

    Для получения стоимости бриллианта следует указать его признаки, например, вес в каратах, качество огранки и 
    так далее.
                   
    """, unsafe_allow_html=True)

st.divider() # Горизонтальная черта

st.header("Разработчик")
col1, col2 = st.columns([0.4, 0.8], gap="large")
with col1:
    st.image(f'./images/me.jpg')

github_url = "https://github.com/ari-ira17"
with col2:

    st.markdown(f""" 
                **ФИО:** Аристова Ирина Витальевна

                **ВУЗ**: ОмГТУ

                **Факультет:** Факультет информационных технологий и компьютерных сисетм

                **Курс:** 2

                **Специальность:** 02.03.03 Математическое обеспечение и администрирование информационных систем
""")
    
    st.markdown(
    f"""
    <a href="{github_url}" target="_blank">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" 
             width="25" height="25">
    </a>
    """,
    unsafe_allow_html=True
)
