# **🚢타이타닉 생존 여부 확인하기**
``` C
http://ec2-15-164-104-66.ap-northeast-2.compute.amazonaws.com:8504/
``` 
![Alt text](/data/img10.jpg)

``` C
📌목차
1. 데이터셋 확인하기
2. 라이브러리
3. 데이터 분석 목적
4. 데이터 분포를 통해서 알 수 있는 점
5. 저작권, 라이선스 정보
``` 

## 1️⃣. 데이터셋 확인하기
타이타닉 데이터를 통해 승객 정보를 확인할 수 있다.
``` C
# Survived - 생존 여부 (0 = 사망, 1 = 생존)
# Pclass - 티켓 클래스 (1 = 1등석, 2 = 2등석, 3 = 3등석)
# Sex - 성별
# Age - 나이
# SibSp - 함께 탑승한 자녀 / 배우자 의 수
# Parch - 함께 탑승한 부모님 / 아이들 의 수
# Ticket - 티켓 번호
# Fare - 탑승 요금
# Cabin - 수하물 번호
# Embarked - 선착장 (C = Cherbourg, Q = Queenstown, S = Southampton)
``` 
☑️ 필요없는 데이터인 'Cabin', 'Ticket', 'PassengerId'는 drop했다.
```python
train = train.drop(['Cabin', 'Ticket', 'PassengerId'], axis=1)
```
☑️ X와 y 나누기
```python
X = train[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
X = train.iloc[:,1:]
y = train['Survived']
```
☑️ 문자열인 레이블 인코더로 'Sex'컬럼을 학습시키기 위해 숫자로 인코딩했다.
```python
encoder = LabelEncoder()
encoder.fit(train['Sex'])
train['Sex'] = encoder.fit_transform(train['Sex'])
```


## 2️⃣. 라이브러리
- [streamlit](https://streamlit.io/)   
- [joblib](https://joblib.readthedocs.io/en/latest/)
- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [seaborn](https://seaborn.pydata.org/)
- [plotly](https://plotly.com/python/)
- [matplotlib](https://matplotlib.org/)



## 3️⃣. 데이터 분석 목적
이 데이터를 통해서 다음 3가지를 확인하고자한다.
1. 생존과 사망에 영향을 미치는 정보를 찾는다.
2. 인공지능을 통해 특정 데이터 값으로 생존을 예측한다.
3. 시각적 데이터 자료를 활용한다.

<br>

## 4️⃣. 데이터 분포를 통해서 알 수 있는 점

1. 나이별 승객 현황을 확인할 수 있다.

```python
# px.histogram를 이용해 차트 만들기

import plotly.express as px
fig = px.histogram(df, x=['Age'], color_discrete_sequence=['#1d29d1'], barmode='overlay')
        fig.update_layout(title="Age")
        st.write(fig)
```
![Alt text](/data/chart01.png)

---
2. 성별에 따른 생존 상황을 살펴보면
남성의 생존 가능성이 더 낮다.

```python
# px.pie를 이용해 파이차트 만들기

import plotly.express as px
fig2 = px.pie(df,names=['Male', 'Female'],
        values=[35.2,64.8],
        color_discrete_sequence=px.colors.sequential.haline,
        title='Gender')
        st.plotly_chart(fig2)

```
![Alt text](/data/chart02.png)
---

3. 선착장과 생존과의 관계를 살펴보면 S선착장에서 탄 사람들이 가장 사망률이 높았다.
```python
# go.figure를 이용해 파이차트 만들기

import plotly.graph_objects as go
labels = [x for x in df.Embarked.value_counts().index]
    values = df.Embarked.value_counts()
    fig=go.Figure(data=[go.Pie(labels=["Southampton","Cherbourg","Queenstown"],values=values,hole=.3,pull=[0,0,0.06,0])])
    fig.update_layout(title_text="Embarked")
    fig.update_traces(marker=dict(colors=night_colors))
    st.write(fig)
```
![Alt text](/data/chart03.png)
![Alt text](/data/chart04.png)
---

4. 요금과 생존과의 관계를 살펴보니 비싼 표를 지불한 승객의 생존률이 높았다.

```python
# px.scatter를 이용해 상관관계 살펴보기

import plotly.express as px
fig = px.scatter(data_frame = df
            ,x = 'Fare'
            ,y = 'Age'
            ,color = 'Survived',
            size='Parch',
            hover_data=['Sex', 'Age'],
            title="Age vs Fare")
        st.write(fig)
```
![Alt text](/data/chart05.png)

5. 데이터프레임과 통계치를 선택해서 확인할 수 있다

```python
radio_menu = ['데이터프레임','통계치']
    selected = st.radio('',radio_menu)

    if selected == radio_menu[0]:
        st.dataframe(df)
    elif selected == radio_menu[1]:
        st.dataframe(df.describe())
```
![Alt text](/data/chart06.png)

6. 해당 컬럼의 최대값 데이터와 최소값 데이터를 확인할 수 있다

```python
col_list = df.columns[4:]
    selected_col = st.selectbox('최대 최소 원하는 컬럼 선택',col_list)
    col1,col2 = st.columns(2)
    with col1:
        df_max = df.loc[df[selected_col] == df[selected_col].max(),]
        st.text('{}컬럼의 최대값에 해당하는 데이터입니다.'.format(selected_col))
        st.dataframe(df_max)
    with col2:
        df_min = df.loc[df[selected_col] == df[selected_col].min(),]
        st.text('{}컬럼의 최소값에 해당하는 데이터입니다.'.format(selected_col))
        st.dataframe(df_min)
```
![Alt text](/data/chart07.png)


7. 상관계수 확인하기

```python
selected_list = st.multiselect(' ',col_list)
    if len(selected_list) > 1:    
        fig1 = sb.pairplot(data=df[selected_list])
        st.pyplot(fig1)
    
        st.subheader('선택하신 컬럼끼리의 상관계수입니다.')
        st.dataframe(df[selected_list].corr())

        fig2 = plt.figure()
        sb.heatmap(data=df[selected_list].corr(),annot=True,fmt='.2f',
            vmin=-1,vmax=1,cmap='coolwarm',linewidths=0.5)
        st.pyplot(fig2)
```
![Alt text](/data/chart08.png)
![Alt text](/data/chart09.png)
![Alt text](/data/chart10.png)


## 5️⃣. 저작권, 라이선스 정보
- [📁 캐글](https://www.kaggle.com/competitions/titanic)   
- [📁 네이버 지식백과](https://terms.naver.com/entry.naver?docId=3574197&cid=58940&categoryId=58956)




