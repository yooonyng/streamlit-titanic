import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sb
# import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
# import os
# import base64
# import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# import plotly.offline as py

night_colors = ['#1d29d1','#fefffc','#d6f089','#edfffd','#d6f089','#f0fcca']


def main():
    df = pd.read_csv('data/titanic_train.csv')

    st.title('π’νμ΄νλ μμ‘΄ μ¬λΆ νμΈνκΈ°')
    st.text('\n')

    image = Image.open('data/img01.jpg')
    st.image(image)
    st.text('\n')

    with st.sidebar:
        st.title('πμμ‘΄μ νμΈνκΈ°')
        st.write('---')

        pclass = st.sidebar.selectbox('ν°μΌ ν΄λμ€λ₯Ό μ ννμΈμ', [1, 2, 3])
        st.subheader('\n')

        age = st.sidebar.slider('λμ΄λ₯Ό μ ννμΈμ',1,100,30,1)
        st.subheader('\n')

        sex = st.radio('μ±λ³μ μ ννμΈμ',['λ¨μ','μ¬μ'])
        if sex == 'μ¬μ':
            sex = 0
        else:
            sex = 1
        st.subheader('\n')
        
        embarked = st.sidebar.selectbox('μ μ°©μ₯μ μ ννμΈμ', ['Cherbourg', 'Queenstown', 'Southampton'])
        #S=2 , C=0, Q=1
        if embarked == 'Cherbourg':
            embarked = 0
        elif embarked == 'Queenstown':
            embarked = 1
        elif embarked == 'Southampton':
            embarked = 2
        st.subheader('\n')

        sibsp = st.number_input('ν¨κ» νμΉν μλ/λ°°μ°μ μλ₯Ό μλ ₯νμΈμ',0)
        st.subheader('\n')
        parch = st.number_input('ν¨κ» νμΉν λΆλͺ¨λ/μμ΄λ€ μλ₯Ό μλ ₯νμΈμ',0)
        st.subheader('\n')
        fare = (st.number_input('νμΉ μκΈμ μλ ₯νμΈμ',0))/1257
        # λ¬λ¬ νμ 
        new_data = np.array([pclass,sex,age,sibsp,parch,fare,embarked])

    

    if st.button('μμ‘΄ νμΈ') :

        classifier = joblib.load('data/classifier.pkl')
        scaler_X = joblib.load('data/scaler_X.pkl')
        encoder = joblib.load('data/encoder.pkl')

        new_data = np.array([new_data])
        X_new = scaler_X.transform(new_data)
        y_pred = classifier.predict(X_new)

        # μμ‘΄ = 1
        # μμ‘΄ μλ = 0

        if y_pred[0] == 1 :
            st.subheader('\"λΉμ μ μ΄μμ΅λλ€.\"')
            # image = Image.open('data/img03.gif')
            # st.image(image)
            # file_ = open("data/img03.gif", "rb")
            # contents = file_.read()
            # data_url = base64.b64encode(contents).decode("utf-8")
            # file_.close()
        elif y_pred[0] == 0 :
            st.subheader('\"λΉμ μ μ£½μμ΅λλ€.\"')
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

    st.subheader('*οΈβ£λμ΄λ³ μΉκ° νν© νμΈ')
    st.write('---')
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('*\"λμ΄λλ³λ‘ μΉκ°μ΄ μΌλ§λ μμμκΉ?\"*')
        image = Image.open('data/img04.jpg')
        st.image(image)
    with col2:
        fig = px.histogram(df, x=['Age'], color_discrete_sequence=['#1d29d1'], barmode='overlay')
        fig.update_layout(title="Age")
        st.write(fig)

    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')


    st.subheader('*οΈβ£μ±λ³κ³Ό μμ‘΄κ³Όμ κ΄κ³')
    st.write('---')
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('*\"μ¬μμΉκ° 74%, μ΄λ¦°μ΄ 52%, λ¨μμΉκ° 20% κ΅¬μ‘°\"*')
        st.text('1λ±μ μΉκ° λ¨μ±μ 70%κ° μ¬λ§\n2λ±μ μΉκ° λ¨μ±μ 90%κ° μ¬λ§')
        st.text('λΉμ 1,2λ±μμ ν λ¨μ μΉκ°λ€μ\nλ―Έκ΅­,μκ΅­μ μ΅μλ₯μΈ΅μ΄μλ€.')
        image = Image.open('data/img05.jpg')
        st.image(image)
        st.caption('Titanic Inquiry Project')

    with col2:
        # labels = [x for x in df.Sex.value_counts().index]
        # values = df.Sex.value_counts()
        # fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,pull=[0.03, 0])])
        # fig.update_layout(title_text="Gender")
        # fig.update_traces(marker=dict(colors=night_colors))
        # st.write(fig)

        fig2 = px.pie(df,names=['Male', 'Female'],
        values=[35.2,64.8],
        color_discrete_sequence=px.colors.sequential.haline,
        title='Gender')
        st.plotly_chart(fig2)

    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')




    st.subheader('*οΈβ£μ μ°©μ₯κ³Ό μμ‘΄κ³Όμ κ΄κ³')
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




    st.subheader('*οΈβ£μκΈκ³Ό μμ‘΄κ³Όμ κ΄κ³')
    st.write('---')
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('*\"λΉμΌ μκΈμ λλ€λ©΄ μμ‘΄μ¨μ΄ λμκΉ?\"*')
        st.text('μ¬κ³ λ‘ 1,514λͺμ΄ μ¬λ§νκ³ \n710λͺμ΄ κ΅¬μ‘°λμμ΅λλ€.')
        image = Image.open('data/img10.jpg')
        st.image(image)
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


    st.subheader('*οΈβ£λ°μ΄ν°νλ μκ³Ό ν΅κ³μΉλ₯Ό μ ν')
    st.write('---')
    radio_menu = ['λ°μ΄ν°νλ μ','ν΅κ³μΉ']
    selected = st.radio('',radio_menu)

    if selected == radio_menu[0]:
        st.dataframe(df)
    elif selected == radio_menu[1]:
        st.dataframe(df.describe())
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')

    st.subheader('*οΈβ£ν΄λΉ μ»¬λΌμ μ΅λκ° λ°μ΄ν°μ μ΅μκ° λ°μ΄ν°')
    st.write('---')
    col_list = df.columns[4:]
    selected_col = st.selectbox('μ΅λ μ΅μ μνλ μ»¬λΌ μ ν',col_list)
    col1,col2 = st.columns(2)
    with col1:
        df_max = df.loc[df[selected_col] == df[selected_col].max(),]
        st.text('{}μ»¬λΌμ μ΅λκ°μ ν΄λΉνλ λ°μ΄ν°μλλ€.'.format(selected_col))
        st.dataframe(df_max)
    with col2:
        df_min = df.loc[df[selected_col] == df[selected_col].min(),]
        st.text('{}μ»¬λΌμ μ΅μκ°μ ν΄λΉνλ λ°μ΄ν°μλλ€.'.format(selected_col))
        st.dataframe(df_min)
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')


    st.subheader('*οΈβ£μκ΄κ³μ νμΈνκΈ°')
    st.write('---')
    selected_list = st.multiselect(' ',col_list)
    if len(selected_list) > 1:    
        fig1 = sb.pairplot(data=df[selected_list])
        st.pyplot(fig1)
    
        st.subheader('μ ννμ  μ»¬λΌλΌλ¦¬μ μκ΄κ³μμλλ€.')
        st.dataframe(df[selected_list].corr())

        fig2 = plt.figure()
        sb.heatmap(data=df[selected_list].corr(),annot=True,fmt='.2f',
            vmin=-1,vmax=1,cmap='coolwarm',linewidths=0.5)
        st.pyplot(fig2)


    
    




    
if __name__ == '__main__':
    main()