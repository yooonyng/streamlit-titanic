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

night_colors = ['lightskyblue', 'navy', 'snow','aliceblue']


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
            st.subheader('살았따,,')
            # image = Image.open('data/img03.gif')
            # st.image(image)
            file_ = open("data/img03.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
        elif y_pred[0] == 0 :
            st.subheader('죽었따.')
            # image = Image.open('data/img02.gif')
            # st.image(image)
            file_ = open("data/img02.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,)
        
    st.write('---')


    st.subheader('*️⃣나이와 생존과의 관계')
    fig = px.histogram(df, x='Age',  color_discrete_sequence=['lightskyblue'], barmode='overlay')
    fig.update_layout(title="Age")
    st.write(fig)
    st.subheader('\n')

    st.write('---')

    st.subheader('*️⃣성별과 생존과의 관계')
    labels = [x for x in df.Sex.value_counts().index]
    values = df.Sex.value_counts()
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,pull=[0.03, 0])])
    fig.update_layout(title_text="Gender")
    fig.update_traces(marker=dict(colors=night_colors))
    st.write(fig)
    st.subheader('\n')

    st.write('---')


    st.subheader('*️⃣선착장과 생존과의 관계')
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

    st.write('---')


    st.subheader('*️⃣요금과 생존과의 관계')
    fig = px.scatter(data_frame = df
        ,x = 'Fare'
        ,y = 'Age'
        ,color = 'Survived',
        size='Parch',
        hover_data=['Sex', 'Age'],
        color_discrete_sequence =['navy','#57A7F3','#D3DBDD'],
        title="Age vs Fare")
    st.write(fig)
    st.subheader('\n')
    
    






    
if __name__ == '__main__':
    main()