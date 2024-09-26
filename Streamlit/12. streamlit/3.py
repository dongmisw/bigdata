import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mpg= pd.read_csv("mpg.csv")
#st.dataframe(mpg)
c= st.sidebar.selectbox("자동차회사를 선택하세요",
                     mpg['manufacturer'].unique().tolist())
mpg_selected= mpg.query('manufacturer == @c')
st.dataframe(mpg_selected)

tab1, tab2, tab3, tab4, tab5 \
= st.tabs(['drv별 city 평균','category별 city 평균',
          'tab3번', 'tab4번','tab5번'])
with tab1:
    #2. tab1 - drv별 city 평균, 그래프
    st.title("1번")
    mpg_tab1 = mpg_selected.groupby('drv')\
        .agg(시티평균=('cty', 'mean'))
    st.dataframe(mpg_tab1)
    fig1 = plt.figure()
    sns.barplot(data = mpg_tab1, x='drv', y ='시티평균')
    st.pyplot(fig1)

with tab2:
    st.title("2번")
   #3. tab2 - category 별로 highway별로 평균 연비 
    mpg_tab2 = mpg_selected.groupby('category')\
                    .agg(hwy_mean = ('hwy', 'mean'))
    st.dataframe(mpg_tab2)
    fig2 = plt.figure()
    sns.barplot(data = mpg_tab2, x= 'category', y ='hwy_mean' )
    st.pyplot(fig2)
with tab3:
    st.title("3번")
#4. tab3 - category 별로 모든 데이터 확인하기
with tab4:
    st.title("4번")
    #고양이 사진
with tab5:
    st.title("5번")
    #유튜브




#0. sidebar select box에서 데이터를 한정시킴 
# (manufacturer를 선택)
#1. tab으로 여러 값을 나타냄
#2. tab1 - drv별 city 평균, 그래프
#3. tab2 - category 별로 highway별로 평균 연비 
#4. tab3 - category 별로 모든 데이터 확인하기

