import streamlit as st
from htbuilder import div, big, h2, styles
from htbuilder.units import rem
import math

st.markdown('# PRESSÃO DE VAPOR PELA LEI DE ANTOINE')

st.markdown('Esta aplicação permite que você escolha um composto e selecione uma temperatura para determinação da pressão de vapor pela Lei de Antoine. Aproveite!')

def antoine(a,b,c,t):

    p = math.exp(a-(b/(c+t)))
    return p

st.markdown("### Seleção do composto:")
composto = st.selectbox('Composto:', ('Ácido clorídrico', 'Ácido fluorídrico', 'Ácido iodídrico', 'Ácido sulfídrico', 'Água', 'Amônia', 'Argônio', 'Benzeno', 'Bromo gasoso', 'Clorofórmio', 'Cloro gasoso', 'Dióxido de carbono', 'Diclorometano', 'Deutério', 'Etanol', 'Flúor gasoso', 'Hexano', 'Hidrogênio', 'Iodo', 'Metanol', 'Monóxido de carbono', 'Oxigênio', 'Ozônio','Nitrogênio'))

if composto == 'Ácido clorídrico':
    t = st.slider('Selecione a temperatura (K):', 137, 200, 170)
    a, b, c = 16.5040, 1714.25, -14.45
    pressao = antoine(a,b,c,t)

elif composto == 'Ácido fluorídrico':
    t = st.slider('Selecione a temperatura (K):', 206, 313, 260)
    a, b, c = 17.6958, 3404.49, 15.06
    pressao = antoine(a,b,c,t)

elif composto == 'Ácido iodídrico':
    t = st.slider('Selecione a temperatura (K):', 215, 256, 235)
    a, b, c = 12.9149, 957.96, -85.06
    pressao = antoine(a,b,c,t)

elif composto == 'Ácido sulfídrico':
    t = st.slider('Selecione a temperatura (K):', 190, 230, 210)
    a, b, c = 16.1040, 1768.69, -26.06
    pressao = antoine(a,b,c,t)

elif composto == 'Água':
    t = st.slider('Selecione a temperatura (K):', 284, 441, 360)
    a, b, c = 18.3036, 3816.44, -46.13
    pressao = antoine(a,b,c,t)

elif composto == 'Amônia':
    t = st.slider('Selecione a temperatura (K):', 179, 261, 220)
    a, b, c = 16.9481, 2132.50, -32.98
    pressao = antoine(a,b,c,t)

elif composto == 'Argônio':
    t = st.slider('Selecione a temperatura (K):', 81, 94, 87)
    a, b, c = 15.2330, 700.51, -5.84
    pressao = antoine(a,b,c,t)

elif composto == 'Benzeno':
    t = st.slider('Selecione a temperatura (K):', 280, 377, 330)
    a, b, c = 15.9008, 2788.51, -52.36
    pressao = antoine(a,b,c,t)

elif composto == 'Bromo gasoso':
    t = st.slider('Selecione a temperatura (K):', 259, 354, 310)
    a, b, c = 15.8441, 2582.32, -51.56
    pressao = antoine(a,b,c,t)

elif composto == 'Clorofórmio':
    t = st.slider('Selecione a temperatura (K):', 260, 370, 315)
    a, b, c = 15.9732, 2696.80, -46.16
    pressao = antoine(a,b,c,t)

elif composto == 'Cloro gasoso':
    t = st.slider('Selecione a temperatura (K):', 172, 264, 220)
    a, b, c = 15.9610, 1978.32, -27.01
    pressao = antoine(a,b,c,t)

elif composto == 'Deutério':
    t = st.slider('Selecione a temperatura (K):', 19, 25, 22)
    a, b, c = 13.2954, 157.80, 0
    pressao = antoine(a,b,c,t)

elif composto == 'Dióxido de carbono':
    t = st.slider('Selecione a temperatura (K):', 154, 204, 180)
    a, b, c = 22.5898, 3103.39, -0.16
    pressao = antoine(a,b,c,t)

elif composto == 'Diclorometano':
    t = st.slider('Selecione a temperatura (K):', 229, 332, 280)
    a, b, c = 16.3029, 2622.44, -41.70
    pressao = antoine(a,b,c,t)

elif composto == 'Etanol':
    t = st.slider('Selecione a temperatura (K):', 270, 320, 369)
    a, b, c = 18.9119, 3803.98, -41.68
    pressao = antoine(a,b,c,t)

elif composto == 'Flúor gasoso':
    t = st.slider('Selecione a temperatura (K):', 59, 91, 75)
    a, b, c = 15.6700, 714.10, -6.00
    pressao = antoine(a,b,c,t)

elif composto == 'Hexano':
    t = st.slider('Selecione a temperatura (K):', 245, 370, 310)
    a, b, c = 15.8366, 2697.55, -48.78
    pressao = antoine(a,b,c,t)

elif composto == 'Hidrogênio':
    t = st.slider('Selecione a temperatura (K):', 14, 25, 20)
    a, b, c = 13.6333, 164.90, 3.19
    pressao = antoine(a,b,c,t)

elif composto == 'Iodo':
    t = st.slider('Selecione a temperatura (K):', 383, 487, 435)
    a, b, c = 16.1597, 3709.23, -68.16
    pressao = antoine(a,b,c,t)

elif composto == 'Metanol':
    t = st.slider('Selecione a temperatura (K):', 257, 364, 310)
    a, b, c = 18.5875, 3626.55, -34.29
    pressao = antoine(a,b,c,t)

elif composto == 'Monóxido de carbono':
    t = st.slider('Selecione a temperatura (K):', 63, 108, 85)
    a, b, c = 14.3686, 530.22, -13.15
    pressao = antoine(a,b,c,t)

elif composto == 'Oxigênio':
    t = st.slider('Selecione a temperatura (K):', 63, 100, 80)
    a, b, c = 15.4075, 734.55, -6.43
    pressao = antoine(a,b,c,t)

elif composto == 'Ozônio':
    t = st.slider('Selecione a temperatura (K):', 109, 174, 140)
    a, b, c = 15.7427, 1272.18, -22.16
    pressao = antoine(a,b,c,t)

elif composto == 'Nitrogênio':
    t = st.slider('Selecione a temperatura (K):', 54, 90, 72)
    a, b, c = 14.9542, 588.72, -6.60
    pressao = antoine(a,b,c,t)

# Creating parameters to use after
color = '#FF4D4C'
title = 'Pressão de vapor:'
value = '{:.2f}'.format(pressao) + ' ' + 'mmHg' + ' ' + '=' + ' ' + '{:.2f}'.format(pressao/7.501) + ' ' + 'kPa'

st.markdown(
        div(
            style=styles(
                text_align="left",
                color = color,
                padding=(rem(1), 0, rem(1), 0),
            )
        )(
            h2(style=styles(font_size=rem(2), font_weight=600, padding=0))(title),
           big(style=styles(font_size=rem(3.6), font_weight=600, line_height=1.5))(
                value
            ),
        ),
        unsafe_allow_html=True,
    )
