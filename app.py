import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sklearn


def main():
    df = pd.read_csv('data/titanic_train.csv')
    st.subheader('타이타닉 생존 여부 확인하기')
    print(sklearn.__version__)

    with st.sidebar:

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

        if y_pred[0] == 1 :
            st.text('살았따.')
        elif y_pred[0] == 0 :
            st.text('죽었따.')
        







    # st.sidebar.header('Menu')
    # st.sidebar.markdown("Drag the sliders")

    # if st.checkbox("Show original dataset"):
    #  st.write(df.iloc[0:age])   

    # column_list = df.columns
    # choice_list = st.multiselect('컬럼을 선택하세요',column_list)
    # df[choice_list]
    # st.dataframe(print(choice_list))
    
    # pclass = [[pclass]]
    # sex =[[sex]]
    # encoder.fit_transform(sex)
    # encoder.fit_transform(pclass)
    # new_data = np.array([pclass,sex,age,embarked],dtype=object)
    # new_data2 = np.vectorize(new_data)
    # X_new = scaler_X.transform(new_data)
    # X_new = X_new.toarray()

    
if __name__ == '__main__':
    main()