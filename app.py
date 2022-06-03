import streamlit as st
import pandas as pd
import numpy as np
import joblib


def main():
    df = pd.read_csv('data/titanic_train.csv')
    st.subheader('타이타닉 생존 여부 확인하기')

    st.sidebar.header('Menu')
    st.sidebar.markdown("Drag the sliders")

    pclass = st.sidebar.selectbox('Pclass', [1, 2, 3])
    sex = st.sidebar.radio('Sex',['Male','Female'])
    age = st.sidebar.slider('Age',1,120,30,1)
    embarked = st.sidebar.selectbox('Embarked', ['Cherbourg', 'Queenstown', 'Southampton'])

    if st.checkbox("Show original dataset"):
     st.write(df.iloc[0:age])   

    column_list = df.columns
    choice_list = st.multiselect('컬럼을 선택하세요',column_list)
    df[choice_list]
    st.dataframe(print(choice_list))

    classifier = joblib.load('data/classifier.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')
    encoder = joblib.load('data/encoder.pkl')
    
    encoder.fit(pclass)
    new_data = np.array([['pclass','sex','age','embarked']])
    new_data2 = np.vectorize(new_data)
    X_new = scaler_X.transform(new_data)
    X_new = X_new.toarray()


    # menu = ['home']
    # choice = st.sidebar.selectbox(menu)

    # if choice == menu[0]:
    #     pass
    # elif choice == menu[1]:
    #     pass
    # elif choice == menu[2]:
    #     pass
    # elif choice == menu[3]:
    #     pass
    
if __name__ == '__main__':
    main()