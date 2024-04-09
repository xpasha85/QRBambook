import streamlit as st
import qrcode



st.set_page_config(page_title='QRCode BambookCafe', page_icon='📱')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.subheader('Создание QRCode для BambookCafe')
name = st.text_input(label='Введите имя',)
summ_input = int(st.number_input(label='Введите сумму', min_value=500, max_value=10000, step=500, value=2000))

if st.button('Создать'):
    cont = st.container(border=True)
    with cont:
        st.title(' ')
        st.header('BambookCafe')
        base_url = 'https://www.qrtag.net/api/qr.png?url='
        sber_url = f'https://sberbank.ru/qr/?uuid=1000200649&amount={summ_input}.0'
        img = qrcode.make(sber_url)
        img.save('qr.jpg')
        st.image('qr.jpg')
        if name:
            st.text(f'{name.title()}, ваш QRCode на \n {str(summ_input)} руб.')
        else:
            st.text(f'Ваш QRCode на \n {str(summ_input)} руб.')