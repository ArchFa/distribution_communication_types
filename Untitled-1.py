# %%
import pandas as pd
import streamlit as st
from collections import Counter
from PIL import Image

# %%
im = Image.open("./logo_ugry.png")
st.set_page_config(page_title="Распределение типов связи", page_icon=im)

# %%
st.title("Распределение типов связи")
st.write("Выбранные типы связи для задач. Датафрейм был отфильтрован, учитываются только следующие платформы: iOS, Android")
uploaded_file = st.file_uploader("Выбирете файл")

use_example_file = st.checkbox(
    "Использовать пример выгрузки", False, help="Будет использована старая выгрузка"
)


if use_example_file:
    uploaded_file = "communication_type.csv"


if uploaded_file is not None:
     df = pd.read_csv(uploaded_file, sep='|')
     df.columns = ['offer_id', 'platform', 'communication_type']

     df = df.query('platform != " admins   "')
     df = df.query('platform != "          "')
     df = df.query('platform != " web      "')
     df = df.query('platform != " whatsapp "')

     # удаление пропусков, которые появляются из за особенностей выгрузки
     df = df.dropna()

     file_container = st.expander("Check your uploaded .csv")   
     st.write(df)

st.info(
   f"""
        👆 Загрузите файл с расширением csv. В файле должны стого содержаться следующие столбцы:
        - id оффера
        - платформа
        - тип связи
        """
)

if not uploaded_file or not use_example_file:
        st.stop()

# %%
all_task = df['offer_id'].nunique()
st.write('Всего задач:', all_task)

# %%
by_phone = df.query('communication_type == " by_phone"').count()[0]
st.write('Количество задач с типом связи "by_phone"', by_phone)


st.write('Процент пользователей, которые создавали задачу через телефон {:.0f}%'
        .format(by_phone * 100 / all_task))

# %%
in_app = df.query('communication_type == " in_app"').count()[0]
st.write('Количество задач с типом связи "by_phone"', in_app)

st.write('Процент пользователей, которые создавали задачу через приложение {:.0f}%'
        .format(in_app * 100 / all_task))


