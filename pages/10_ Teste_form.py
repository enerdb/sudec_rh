import streamlit as st



st.set_page_config(
    page_title="Inserir dados",
    page_icon='✏',
    layout = 'wide'
)

st.markdown("""
            # ESSA PÁGINA AINDA NÃO ESTÁ FUNCIONANDO
            # FAVOR NÃO UTILIZAR AINDA
            """)

with st.form("my_form"):
    st.write("Inside the form")
    my_number = st.slider('Pick a number', 1, 10)
    my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
    st.form_submit_button('Submit my picks')

# This is outside the form
st.write(my_number)
st.write(my_color)
