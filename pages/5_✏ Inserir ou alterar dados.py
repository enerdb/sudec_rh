import streamlit as st

st.set_page_config(
    page_title="Inserir dados",
    page_icon='✏',
    layout = 'wide'
)

st.markdown('## Selecione uma das ações abaixos para abrir um formulário')

st.link_button("Cadastrar ou alterar dados de servidor", "https://forms.gle/ESrKb61p9kf8U3X59")

st.link_button("Nomear Servidor em Cargo Gratificado", "https://forms.gle/dUgVQ3DjBYzcZ3nF8")

st.link_button("Exonerar Servidor de Cargo Gratificado", "https://forms.gle/9wri9mmgVHRRfrjB7")

st.link_button("Registrar ou alterar atividade predominante de servidor", "https://forms.gle/xzh6i2hSmL4tdu5y5")

st.link_button("Cadastrar ou alterar férias", "https://forms.gle/GyZYLyVm2eFLE92i6")

# Desativado. Agora os abonos são lançados em página própria dentro do sistema.
# st.link_button("Cadastrar ou alterar abono anual","https://forms.gle/EACbK7HUKTtt5HVw8")

st.link_button("Cadastrar dipensa médica ou outro tipo de afastamento", "https://forms.gle/Yhex7dzj4pF6CD3o6")

