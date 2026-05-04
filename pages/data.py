import streamlit as st
import pandas as pd

st.title("Информация о наборе данных")

st.subheader("ℹ️ Описание")

st.markdown("""
**Предметная область** — данные о стоимости бриллиантов (в долларах США)  

**Целевая переменная** — `price`
""", unsafe_allow_html=True)

# ---- Признаки ----
def type_badge(dtype):
    if "float" in dtype:
        return ":blue-badge[float64]"
    elif "int" in dtype:
        return ":green-badge[int64]"
    elif "object" in dtype:
        return ":orange-badge[object]"
    return dtype

data = {
    "Признак": ["unnamed", "carat", "cut", "color", "clarity", "depth", "table", "price", "x", "y", "z"],
    "Описание": [
        "Порядковый номер записи",
        "Вес алмаза в каратах",
        "Качество огранки",
        "Цвет бриллианта",
        "Чистота алмаза",
        "Глубина (%)",
        "Ширина площадки (%)",
        "Цена (USD)",
        "Длина (мм)",
        "Ширина (мм)",
        "Высота (мм)"
    ],
    "Тип данных": [
        type_badge("int64"),
        type_badge("float64"),
        type_badge("object"),
        type_badge("object"),
        type_badge("object"),
        type_badge("float64"),
        type_badge("float64"),
        type_badge("int64"),
        type_badge("float64"),
        type_badge("float64"),
        type_badge("float64"),
    ]
}

df = pd.DataFrame(data)
with st.expander("📋 Описание признаков"):
    col1, col2, col3 = st.columns([0.3, 2, 0.2])
    
    with col2:
        st.markdown("""
        <style>
        table {
            font-size: 14px;
            width: 100%;
        }
        th, td {
            padding: 8px 10px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)

st.subheader("👀 Данные")
df = pd.read_csv("./data/diamonds.csv")
st.dataframe(df.head())

st.subheader("🛠 Предобработка данных")

st.write("""
В процессе предобработки были выполнены следующие шаги:
- проверка пропущенных значений
- удаление или обработка выбросов
- преобразование категориальных признаков (`cut`, `color`, `clarity`)
- проверка независимости признаков
- создание Mind Map
""")

from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGES_DIR = ROOT_DIR / "images"

col1, col2 = st.columns(2)

with col1:
    st.image(
        str(IMAGES_DIR / "corr_matrix.png"), 
        caption="Корреляционная матрица"
    )

with col2:
    st.image(
        str(IMAGES_DIR / "mind_map.png"), 
        caption="Mind Map"
    )

st.subheader("📈 EDA")

st.write("""
В ходе анализа были выявлены следующие закономерности:
- цена сильно зависит от веса (`carat`)
- более высокая огранка увеличивает стоимость
- цвет и чистота также влияют на цену, но слабее
""")


