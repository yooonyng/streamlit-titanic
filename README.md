# **๐ขํ์ดํ๋ ์์กด ์ฌ๋ถ ํ์ธํ๊ธฐ**
``` C
http://ec2-15-164-104-66.ap-northeast-2.compute.amazonaws.com:8504/
``` 
![Alt text](/data/img10.jpg)

``` C
๐๋ชฉ์ฐจ
1. ๋ฐ์ดํฐ์ ํ์ธํ๊ธฐ
2. ๋ผ์ด๋ธ๋ฌ๋ฆฌ
3. ๋ฐ์ดํฐ ๋ถ์ ๋ชฉ์ 
4. ๋ฐ์ดํฐ ๋ถํฌ๋ฅผ ํตํด์ ์ ์ ์๋ ์ 
5. ์ ์๊ถ, ๋ผ์ด์ ์ค ์ ๋ณด
``` 

## 1๏ธโฃ. ๋ฐ์ดํฐ์ ํ์ธํ๊ธฐ
ํ์ดํ๋ ๋ฐ์ดํฐ๋ฅผ ํตํด ์น๊ฐ ์ ๋ณด๋ฅผ ํ์ธํ  ์ ์๋ค.
``` C
# Survived - ์์กด ์ฌ๋ถ (0 = ์ฌ๋ง, 1 = ์์กด)
# Pclass - ํฐ์ผ ํด๋์ค (1 = 1๋ฑ์, 2 = 2๋ฑ์, 3 = 3๋ฑ์)
# Sex - ์ฑ๋ณ
# Age - ๋์ด
# SibSp - ํจ๊ป ํ์นํ ์๋ / ๋ฐฐ์ฐ์ ์ ์
# Parch - ํจ๊ป ํ์นํ ๋ถ๋ชจ๋ / ์์ด๋ค ์ ์
# Ticket - ํฐ์ผ ๋ฒํธ
# Fare - ํ์น ์๊ธ
# Cabin - ์ํ๋ฌผ ๋ฒํธ
# Embarked - ์ ์ฐฉ์ฅ (C = Cherbourg, Q = Queenstown, S = Southampton)
``` 
โ๏ธ ํ์์๋ ๋ฐ์ดํฐ์ธ 'Cabin', 'Ticket'๋ dropํ๋ค.
```python
train = train.drop(['Cabin', 'Ticket'], axis=1)
```
โ๏ธ X์ y ๋๋๊ธฐ
```python
X = train[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
X = train.iloc[:,1:]
y = train['Survived']
```
โ๏ธ ๋ฌธ์์ด์ธ ๋ ์ด๋ธ ์ธ์ฝ๋๋ก 'Sex'์ปฌ๋ผ์ ํ์ต์ํค๊ธฐ ์ํด ์ซ์๋ก ์ธ์ฝ๋ฉํ๋ค.
```python
encoder = LabelEncoder()
encoder.fit(train['Sex'])
train['Sex'] = encoder.fit_transform(train['Sex'])
```


## 2๏ธโฃ. ๋ผ์ด๋ธ๋ฌ๋ฆฌ
- [streamlit](https://streamlit.io/)   
- [joblib](https://joblib.readthedocs.io/en/latest/)
- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [seaborn](https://seaborn.pydata.org/)
- [plotly](https://plotly.com/python/)
- [matplotlib](https://matplotlib.org/)



## 3๏ธโฃ. ๋ฐ์ดํฐ ๋ถ์ ๋ชฉ์ 
์ด ๋ฐ์ดํฐ๋ฅผ ํตํด์ ๋ค์ 3๊ฐ์ง๋ฅผ ํ์ธํ๊ณ ์ํ๋ค.
1. ์์กด๊ณผ ์ฌ๋ง์ ์ํฅ์ ๋ฏธ์น๋ ์ ๋ณด๋ฅผ ์ฐพ๋๋ค.
2. ์๊ฐ์  ๋ฐ์ดํฐ ์๋ฃ๋ฅผ ํ์ฉํ๋ค.
3. ์ธ๊ณต์ง๋ฅ์ ํตํด ํน์  ๋ฐ์ดํฐ ๊ฐ์ผ๋ก ์์กด์ ์์ธกํ๋ค.

<br>

## 4๏ธโฃ. ๋ฐ์ดํฐ ๋ถํฌ๋ฅผ ํตํด์ ์ ์ ์๋ ์ 

1. ๋์ด๋ณ ์น๊ฐ ํํฉ์ ํ์ธํ  ์ ์๋ค.

```python
# px.histogram๋ฅผ ์ด์ฉํด ์ฐจํธ ๋ง๋ค๊ธฐ

import plotly.express as px
fig = px.histogram(df, x=['Age'], color_discrete_sequence=['#1d29d1'], barmode='overlay')
        fig.update_layout(title="Age")
        st.write(fig)
```
![Alt text](/data/chart01.png)

---
2. ์ฑ๋ณ์ ๋ฐ๋ฅธ ์์กด ์ํฉ์ ์ดํด๋ณด๋ฉด
๋จ์ฑ์ ์์กด ๊ฐ๋ฅ์ฑ์ด ๋ ๋ฎ๋ค.

```python
# px.pie๋ฅผ ์ด์ฉํด ํ์ด์ฐจํธ ๋ง๋ค๊ธฐ

import plotly.express as px
fig2 = px.pie(df,names=['Male', 'Female'],
        values=[35.2,64.8],
        color_discrete_sequence=px.colors.sequential.haline,
        title='Gender')
        st.plotly_chart(fig2)

```
![Alt text](/data/chart02.png)
---

3. ์ ์ฐฉ์ฅ๊ณผ ์์กด๊ณผ์ ๊ด๊ณ๋ฅผ ์ดํด๋ณด๋ฉด S์ ์ฐฉ์ฅ์์ ํ ์ฌ๋๋ค์ด ๊ฐ์ฅ ์ฌ๋ง๋ฅ ์ด ๋์๋ค.
```python
# go.figure๋ฅผ ์ด์ฉํด ํ์ด์ฐจํธ ๋ง๋ค๊ธฐ

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

4. ์๊ธ๊ณผ ์์กด๊ณผ์ ๊ด๊ณ๋ฅผ ์ดํด๋ณด๋ ๋น์ผ ํ๋ฅผ ์ง๋ถํ ์น๊ฐ์ ์์กด๋ฅ ์ด ๋์๋ค.

```python
# px.scatter๋ฅผ ์ด์ฉํด ์๊ด๊ด๊ณ ์ดํด๋ณด๊ธฐ

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

5. ๋ฐ์ดํฐํ๋ ์๊ณผ ํต๊ณ์น๋ฅผ ์ ํํด์ ํ์ธํ  ์ ์๋ค

```python
radio_menu = ['๋ฐ์ดํฐํ๋ ์','ํต๊ณ์น']
    selected = st.radio('',radio_menu)

    if selected == radio_menu[0]:
        st.dataframe(df)
    elif selected == radio_menu[1]:
        st.dataframe(df.describe())
```
![Alt text](/data/chart06.png)

6. ํด๋น ์ปฌ๋ผ์ ์ต๋๊ฐ ๋ฐ์ดํฐ์ ์ต์๊ฐ ๋ฐ์ดํฐ๋ฅผ ํ์ธํ  ์ ์๋ค

```python
col_list = df.columns[4:]
    selected_col = st.selectbox('์ต๋ ์ต์ ์ํ๋ ์ปฌ๋ผ ์ ํ',col_list)
    col1,col2 = st.columns(2)
    with col1:
        df_max = df.loc[df[selected_col] == df[selected_col].max(),]
        st.text('{}์ปฌ๋ผ์ ์ต๋๊ฐ์ ํด๋นํ๋ ๋ฐ์ดํฐ์๋๋ค.'.format(selected_col))
        st.dataframe(df_max)
    with col2:
        df_min = df.loc[df[selected_col] == df[selected_col].min(),]
        st.text('{}์ปฌ๋ผ์ ์ต์๊ฐ์ ํด๋นํ๋ ๋ฐ์ดํฐ์๋๋ค.'.format(selected_col))
        st.dataframe(df_min)
```
![Alt text](/data/chart07.png)





## 5๏ธโฃ. ์ ์๊ถ, ๋ผ์ด์ ์ค ์ ๋ณด
- [๐ ์บ๊ธ](https://www.kaggle.com/competitions/titanic)   
- [๐ ๋ค์ด๋ฒ ์ง์๋ฐฑ๊ณผ](https://terms.naver.com/entry.naver?docId=3574197&cid=58940&categoryId=58956)




