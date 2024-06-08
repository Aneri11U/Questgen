import streamlit as st
from pprint import pprint
from Questgen import main
from spacy.cli import download

download('en_core_web_sm')

st.set_page_config(
    page_title='Questgen',
    page_icon= ':fire:',
)

st.title(body='Question Generator')

input_text = st.text_area(
    label='Enter text from which questions are to be generated',
    value = 'Sachin Tendulkar is the best batsman in the history of cricket. Sachin is from Mumbai. Sachin has two children.'
)

qg = main.QGen()

payload = {
    'input_text' : input_text
}

output = qg.predict_mcq(payload=payload)

st.subheader(body='*Generated Questions are:*', divider='orange')
for question in output['questions']:
    st.write(f"{question['question_statement']}")

if st.toggle(label='Show Total Output'):
    st.write(output)
