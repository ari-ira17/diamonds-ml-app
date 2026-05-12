import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("./data/diamonds_filtered.csv")
df_original = pd.read_csv("./data/diamonds.csv")

st.header("📊 Визуализация данных")

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Исходные данные")
    fig1 = px.box(df_original, 
                  x="cut", 
                  y="price", 
                  color="cut",
                  title="Цены с аномалиями",
                  points="outliers") 
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)
    st.write(f"Всего записей: {len(df_original)}. Видны экстремальные цены")

with row1_col2:
    st.subheader("Данные после EDA")
    fig2 = px.box(df, 
                  x="cut", 
                  y="price", 
                  color="cut",
                  title="Цены после фильтрации",
                  points=False) 
    fig2.update_layout(showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)
    st.write(f"Осталось записей: {len(df)}. Масштаб графика стал более детальным")

st.divider()

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Цена vs Караты")
    sample_df = df.sample(n=min(2000, len(df))) 
    fig3 = px.scatter(sample_df, x="carat", y="price", color="cut",
                      hover_data=['color', 'clarity'],
                      title="Зависимость стоимости от веса")
    st.plotly_chart(fig3, use_container_width=True)
    st.write("Интерактивный график: можно навести на точку и увидеть детали")

with row2_col2:
    st.subheader("Средняя цена по огранке")
    avg_price_cut = df.groupby('cut')['price'].mean().sort_values().reset_index()
    fig4 = px.bar(avg_price_cut, x='cut', y='price', 
                  color='price', title="Какая огранка в среднем дороже?")
    st.plotly_chart(fig4, use_container_width=True)
    st.write("Сравнение средней стоимости для разных типов огранки")
