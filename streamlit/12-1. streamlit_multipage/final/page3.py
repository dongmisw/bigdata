# page3.py
import streamlit as st
import plotly.express as px
import pandas as pd

def page():
    st.title("Plotly chart")

    mpg= pd.read_csv('mpg.csv')

    #1) scatter plot
    fig1 = px.scatter(data_frame=mpg, x='cty', y='hwy', color='drv')
    st.subheader('고속도로 연비와 도심연비의 상관관계')
    st.plotly_chart(fig1)
    

    #2) box plot
    fig2 = px.box(data_frame=mpg, x='category', y='cty', color='category' )
    st.subheader('자동차 종류 별 도심 연비 분포')
    st.plotly_chart(fig2)
    
    #3) bar plot
    result = mpg.groupby("manufacturer", as_index=False)\
                .agg(city_mean = ('cty', 'mean'))
    st.subheader('자동차 제조사 별 도심연비 평균')
    fig3 = px.bar(data_frame=result, x='manufacturer', y='city_mean', color= 'manufacturer')
    st.plotly_chart(fig3)

