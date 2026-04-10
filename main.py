import streamlit as st

# Налаштування екрана
st.set_page_config(page_title="BUILD-FLOW OS", layout="wide")
st.title("🏗 BUILD-FLOW OS v4.1")

# Твій Master-Key прайс
prices = {
    "Q4_стіни": 380,
    "Q4_стеля": 420,
    "вузол_07": 350,
    "кути": 300
}

st.sidebar.markdown("### 📊 Меню")
st.sidebar.info("Тут будуть звіти для Тіни та Валика")

# Поля вводу для OnePlus Pad 2
col1, col2 = st.columns(2)
with col1:
    sw = st.number_input("Стіни м²", value=0.0, step=0.1)
    sg = st.number_input("ГКЛ стеля м²", value=0.0, step=0.1)
with col2:
    nd = st.number_input("Вузли 0.7 м.п.", value=0.0, step=0.1)
    an = st.number_input("Кути м.п.", value=0.0, step=0.1)

if st.button("🚀 ПОРАХУВАТИ ОБ'ЄКТ"):
    # Логіка Master-Key
    total = (sw * prices["Q4_стіни"]) + (sg * prices["Q4_стеля"]) + \
            (nd * prices["вузол_07"]) + (an * prices["кути"])
    
    st.success(f"### ЗАГАЛЬНА СУМА: {int(total):,} грн")
    st.balloons()
  
