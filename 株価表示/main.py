import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('１')
expander.write('２')
expander.write('３')

# # checkbox
# if st.checkbox('Show Image'):
#     img = Image.open('/Users/Kento/Desktop/streamlit/02_06.中高年期と健康_概要.jpg')
#     st.image(img, caption='画像', use_column_width=True)

# selectbox
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)
'あなたの好きな数字は、',option, 'です。'



# inputtext
text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味:', text, 'です。'

# slider
condition = st.slider('あなたの調子は？',0, 100, 50)
'あなたのコンディション:',condition,'です'



