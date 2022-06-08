import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sb
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
import os
import base64
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as py

night_colors = ['#1d29d1','#fefffc','#d6f089','#edfffd','#d6f089','#f0fcca']


def main():
    df = pd.read_csv('data/titanic_train.csv')

    st.title('🚢타이타닉 생존 여부 확인하기')
    st.text('\n')

    image = Image.open('data/img01.jpg')
    st.image(image)
    st.text('\n')

    with st.sidebar:
        st.title('🔍생존자 확인하기')
        st.write('---')

        pclass = st.sidebar.selectbox('티켓 클래스를 선택하세요', [1, 2, 3])
        st.subheader('\n')

        age = st.sidebar.slider('나이를 선택하세요',1,100,30,1)
        st.subheader('\n')

        sex = st.radio('성별을 선택하세요',['남자','여자'])
        if sex == '여자':
            sex = 0
        else:
            sex = 1
        st.subheader('\n')
        
        embarked = st.sidebar.selectbox('선착장을 선택하세요', ['Cherbourg', 'Queenstown', 'Southampton'])
        #S=2 , C=0, Q=1
        if embarked == 'Cherbourg':
            embarked = 0
        elif embarked == 'Queenstown':
            embarked = 1
        elif embarked == 'Southampton':
            embarked = 2
        st.subheader('\n')

        sibsp = st.number_input('함께 탑승한 자녀/배우자 수를 입력하세요',0)
        st.subheader('\n')
        parch = st.number_input('함께 탑승한 부모님/아이들 수를 입력하세요',0)
        st.subheader('\n')
        fare = (st.number_input('탑승 요금을 입력하세요',0))/1257
        # 달러 환전
        new_data = np.array([pclass,sex,age,sibsp,parch,fare,embarked])

    

    if st.button('생존 확인') :

        classifier = joblib.load('data/classifier.pkl')
        scaler_X = joblib.load('data/scaler_X.pkl')
        encoder = joblib.load('data/encoder.pkl')

        new_data = np.array([new_data])
        X_new = scaler_X.transform(new_data)
        y_pred = classifier.predict(X_new)

        # 생존 = 1
        # 생존 아님 = 0

        if y_pred[0] == 1 :
            st.subheader('\"당신은 살았습니다.\"')
            # image = Image.open('data/img03.gif')
            # st.image(image)
            # file_ = open("data/img03.gif", "rb")
            # contents = file_.read()
            # data_url = base64.b64encode(contents).decode("utf-8")
            # file_.close()
        elif y_pred[0] == 0 :
            st.subheader('\"당신은 죽었습니다.\"')
            # image = Image.open('data/img02.gif')
            # st.image(image)
            # file_ = open("data/img02.gif", "rb")
            # contents = file_.read()
            # data_url = base64.b64encode(contents).decode("utf-8")
            # file_.close()
        # st.markdown(
        #     f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        #     unsafe_allow_html=True,)
        
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')

    st.subheader('*️⃣나이와 생존과의 관계')
    st.write('---')
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('*\"나이가 어릴수록 생존율이 높을까?\"*')
        image = Image.open('data/img04.jpg')
        st.image(image)
    with col2:
        fig = px.histogram(df, x='Age',  color_discrete_sequence=['#1d29d1'], barmode='overlay')
        fig.update_layout(title="Age")
        st.write(fig)
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')



    st.subheader('*️⃣성별과 생존과의 관계')
    st.write('---')
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('*\"여자승객 74%, 어린이 52%, 남자승객 20% 구조\"*')
        st.text('1등석 승객 남성은 70%가 사망\n2등석 승객 남성은 90%가 사망')
        st.text('당시 1,2등석에 탄 남자 승객들은\n미국,영국의 최상류층이었다.')
        image = Image.open('data/img05.jpg')
        st.image(image)
        st.caption('Titanic Inquiry Project')

    with col2:
        labels = [x for x in df.Sex.value_counts().index]
        values = df.Sex.value_counts()
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,pull=[0.03, 0])])
        fig.update_layout(title_text="Gender")
        fig.update_traces(marker=dict(colors=night_colors))
        st.write(fig)
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')



    st.subheader('*️⃣선착장과 생존과의 관계')
    st.write('---')
    
    labels = [x for x in df.Embarked.value_counts().index]
    values = df.Embarked.value_counts()
    fig=go.Figure(data=[go.Pie(labels=["Southampton","Cherbourg","Queenstown"],values=values,hole=.3,pull=[0,0,0.06,0])])
    fig.update_layout(title_text="Embarked")
    fig.update_traces(marker=dict(colors=night_colors))
    st.write(fig)

    fig = make_subplots(rows=1, cols=3, specs=[[{"type": "pie"}, {"type": "pie"}, {"type": "pie"}]])
    fig.add_trace(go.Pie(labels=df.loc[df['Embarked'] == 'C']['Survived'], pull = [.1, .1],
                    title = 'Embarked C vs. Survived'), row=1, col=1)
    fig.add_trace(go.Pie(labels=df.loc[df['Embarked'] == 'S']['Survived'], pull = [.07, .07],
                    title = 'Embarked S vs. Survived'),row=1, col=2)
    fig.add_trace(go.Pie(labels=df.loc[df['Embarked'] == 'Q']['Survived'], pull = [.1, .1],
                    title = 'Embarked Q vs. Survived'), row=1, col=3)
    fig.update_traces(marker=dict(colors=night_colors))
    st.write(fig)
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')




    st.subheader('*️⃣요금과 생존과의 관계')
    st.write('---')
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('*\"비싼 요금을 냈다면 생존율이 높을까?\"*')
        st.text('사고로 1,514명이 사망했고\n710명이 구조되었습니다.')
        image = Image.open('data/img06.jpg')
        st.image(image)
        st.caption('타이타닉호의 침몰, 또 다른 이야기: http://memorialnews.net/news/article.html?no=11768')
    with col2:
        fig = px.scatter(data_frame = df
            ,x = 'Fare'
            ,y = 'Age'
            ,color = 'Survived',
            size='Parch',
            hover_data=['Sex', 'Age'],
            title="Age vs Fare")
        st.write(fig)
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')

    
    

    # st.subheader('2. 최근 소년범죄 이슈')
    # col1,col2,col3 = st.columns(3)
    # with col1:
    #     gif_html = get_img_with_href('data/sum01.png', 'https://www.youtube.com/watch?v=h-WmvzCtRh0')
    #     st.markdown(gif_html, unsafe_allow_html=True)
    # with col2:
    #     pass
    # with col3:
    #     st.subheader('끊임없는 촉법소년 논란 연령하향 해야 vs 처벌이 능사는 아냐')
    #     st.text('#촉법소년 #소년법 #촉법소년범죄')
    # st.text('\n')
    # st.text('\n')




    
if __name__ == '__main__':
    main()