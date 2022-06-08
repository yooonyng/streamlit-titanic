# **🚢타이타닉 생존 여부 확인하기**
![Alt text](/data/img08.jpg)

``` C
📌목차
1. 데이터셋 확인하기
2. 타이타닉호의 침몰
3. 데이터 분석 목적
4. 데이터 분포를 통해서 알 수 있는 점
5. 저작권, 라이선스 정보
6. 일정
``` 

## 1️⃣. 데이터셋 확인하기
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
타이타닉 데이터를 통해 승객 정보를 확인할 수 있다.
먼저 필요없는 데이터인 'Cabin', 'Ticket', 'PassengerId'는 삭제해준다.


## 2️⃣. 타이타닉호의 침몰
타이타닉 호가 1912년 북대서양에서 침몰한 사고로 세계에서 가장 유명한 침몰선이다.
1912년 4월 14일 타이타닉호는 2,200여명의 승선자 중 에드워드 스미스(Edward Smith)선장을 포함한 1,500여명과 함께 차가운 바닷속으로 가라앉았다.
- 기록이 상세히 남아있다.
- 유명인과 귀족이 상당수 탑승해있었다.
- 선진 강대국 대영제국의 배로 미국인과 영국인들이 대부분이었다.
- 당시 타이타닉은 세계 최대 규모와 최첨단 기술로 가장 유명한 배로 첫 항해에 침몰했다.


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


## 5️⃣. 저작권, 라이선스 정보
- [📁 캐글](https://www.kaggle.com/competitions/titanic)   
- [📁 네이버 지식백과](https://terms.naver.com/entry.naver?docId=3574197&cid=58940&categoryId=58956)


## 6️⃣. 일정

| Day | 작업 | 내용 |
| ------ | -- |----------- |
|  1일 | ☑️ | 데이터 탐색 및 데이터 선택 |
|  2일 | ☑️ | 코랩 데이터 기획 & 분석 |
|  3일 | ☑️ | 코랩 데이터 기획 & 분석, 서버연결 |
|  6일 | ☑️ | 비주얼 스튜디오 스트림릿 차트 작업 |
|  7일 | ☑️ | 비주얼 스튜디오 스트림릿 차트 작업 |
|  8일 | ☑️ | 비주얼 스튜디오 스트림릿 차트 작업 |
