import streamlit as st
import pandas as pd
import joblib
import os
import numpy as np

FEATURES_ALL = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'radius']
KBEST_FEATURES = ['carat', 'color', 'clarity', 'radius'] 

cut_mapping = {"Fair": 0, "Good": 1, "Ideal": 2, "Premium": 3, "Very Good": 4}
color_mapping = {"D": 0, "E": 1, "F": 2, "G": 3, "H": 4, "I": 5, "J": 6}
clarity_mapping = {"I1": 0, "IF": 1, "SI1": 2, "SI2": 3, "VS1": 4, "VS2": 5, "VVS1": 6, "VVS2": 7}

MODEL_PATHS = {
    "Модель 1 (Polynomial)": "models/polynomial_reg_model_1.pkl",
    "Модель 2 (Boosting)": "models/boosting_reg_model_2.pkl",
    "Модель 3 (CatBoost)": "models/catboost_reg_model_3.pkl",
    "Модель 4 (Bagging)": "models/bagging_reg_model_4.pkl",
    "Модель 5 (Stacking K-Best)": "models/stacking_reg_model_5.pkl",
    "Модель 6 (MLP K-Best)": "models/mlp_optuna_reg_model_6.pkl"
}

@st.cache_resource
def load_model(path):
    if os.path.exists(path):
        return joblib.load(path)
    return None

st.set_page_config(page_title="Предсказание цены", layout="wide")
st.title("💎 Оценка стоимости бриллианта")

selected_model_names = st.multiselect(
    "Выберите модели для сравнения:",
    options=list(MODEL_PATHS.keys()),
    default=["Модель 1 (Polynomial)"]
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📏 Физические параметры")
    carat = st.number_input("Вес (carat)", min_value=0.1, max_value=5.0, value=0.7, step=0.01)
    # Пользователь вводит радиус напрямую, как в твоем датасете
    radius = st.number_input("Радиус (radius, мм)", min_value=1.0, max_value=15.0, value=5.5)
    depth = st.number_input("Глубина (depth, %)", min_value=40.0, max_value=80.0, value=61.0)
    table = st.number_input("Площадка (table, %)", min_value=40.0, max_value=95.0, value=57.0)

with col2:
    st.markdown("### ✨ Качественные характеристики")
    cut_raw = st.selectbox("Огранка (cut)", list(cut_mapping.keys()))
    color_raw = st.selectbox("Цвет (color)", list(color_mapping.keys()))
    clarity_raw = st.selectbox("Чистота (clarity)", list(clarity_mapping.keys()))

st.divider()

if st.button("🚀 Рассчитать стоимость", type="primary", use_container_width=True):
    if not selected_model_names:
        st.warning("Выберите хотя бы одну модель.")
    else:
        input_dict = {
            "carat": carat,
            "cut": cut_mapping[cut_raw],
            "color": color_mapping[color_raw],
            "clarity": clarity_mapping[clarity_raw],
            "depth": depth,
            "table": table,
            "radius": radius
        }
        full_df = pd.DataFrame([input_dict])

        results = []
        
        for name in selected_model_names:
            model = load_model(MODEL_PATHS[name])
            if model:
                try:
                    final_input = full_df[FEATURES_ALL]
                    
                    prediction = model.predict(final_input)[0]

                    results.append({
                        "Модель": name,
                        "Цена": f"${prediction:,.2f}"
                    })
                except Exception as e:
                    st.error(f"Ошибка в {name}: {e}")
            else:
                st.error(f"Файл {name} не найден.")

        if results:
            st.subheader("📊 Результаты предсказания")
            st.table(pd.DataFrame(results))
            
            if len(results) > 1:
                prices = [float(r["Цена"].replace('$', '').replace(',', '')) for r in results]
                st.info(f"**Средняя цена:** ${np.mean(prices):,.2f}")
                