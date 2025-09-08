#page1.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def page():
    st.header('page1.py 이 실행됩니다.')
    st.header('mpg 데이터 분석')

    mpg = pd.read_csv("mpg.csv")
    #cty와 hwy의 상관관계를 나타내는 scatter chart
    mpg_cty_hwy = mpg[['manufacturer',
                       'model',
                       'cty', 'hwy']]
    st.dataframe(mpg_cty_hwy)

    fig1 = plt.figure()
    sns.scatterplot(data = mpg_cty_hwy,
                    x="cty", y="hwy")
    st.pyplot(fig1)


 
    #7. mpg 데이터를 확인하는데, manufacturer로 filtering이 진행.
    # 전체도 보고싶다. 

    st.header("7번 : 전체 선택 가능")
    #st.header(mpg['manufacturer'].unique().tolist())
    l1 = ['전체']
    l1.extend(mpg['manufacturer'].unique().tolist())
    #st.header(l1)

    #만약에 '전체'이 선택 -> mpg_selected = mpg.copy()
    #만약에 '전체 '빼고 나머지 => mpg_selected =mpg.query('manufacturer == @c')
    c=st.selectbox("회사를 선택하세요",l1)
    if c == "전체" :
        #참일때 실행하는 코드
        mpg_selected = mpg.copy()    
    else:
        #거짓일때 실행하는 코드
        mpg_selected =mpg.query('manufacturer == @c')    

    st.dataframe(mpg_selected)


    #6.  
    # 1) 그룹핑을 할것을 정하고 싶어. 
    # - manufacturer, model, drv, category
    # 2) 연비 - cty, hwy
    # 3) 함수 - min, max, count, mean, sum
    st.header("6번")
    var1 = st.selectbox('분석하고 싶은 그룹을 선택', 
                        ['manufacturer','model', 'drv', 'category'])
    var2 = st.selectbox('연비종류를 선택', ['cty','hwy'])
    var3 = st.selectbox('통계 종류 선택',['min', 'max', 'mean', 'count','sum'])
    st.header("당신이 선택한 그룹은 : " + var1 + " 연비는:  " +var2 +  " 통계는 : " +var3)
    mpg7 = mpg.groupby(var1)\
                .agg(value = (var2, var3))
    st.dataframe(mpg7)


    #5. multiselect를 한다. 
    st.header("5번 multi-select")
    multi_selected_manufacturer = st.multiselect('여러개의 자동차회사를 선택하세요.', 
                mpg['manufacturer'].unique().tolist())
    st.header(multi_selected_manufacturer)
    #mpg.query('manufacturer in ["honda", "audi"]')
    mpg_multi = mpg.query('manufacturer in @multi_selected_manufacturer')
    st.dataframe(mpg_multi)
    #manufacture별로 city 평균연비 구해서 dataframe 프린트 하고, 
    # x축 manufaucturer, y축 - city 평균 연비 , bargraph 그리기

    mpg_multi = mpg_multi.groupby('manufacturer', as_index=False)\
                .agg(mean_city = ('cty', 'mean'))

    st.dataframe(mpg_multi)

    fig1 = plt.figure()
    sns.barplot(data=mpg_multi, x="manufacturer", y="mean_city" )
    st.pyplot(fig1)
    

    #4. mpg['manufacturer'] 모든 값을 select box에 넣고 싶다.
    st.header("4번 - 모든 자동차회사 리스트")
    company = st.selectbox('원하는 자동차회사를 선택.',
                        mpg['manufacturer'].unique().tolist())
    mpg_selected_manufacturer = mpg.query('manufacturer == @company')
    st.dataframe(mpg_selected_manufacturer)

    #3. 사용자가 회사명을 입력하도록 설정
    st.header("3번 selectbox 이용한것입니다.")
    company = st.selectbox('원하는 자동차회사를 선택하세요.', 
                                ['audi', 'hyundai','honda','dodge'])
    mpg_selected_manufacturer = mpg.query('manufacturer == @company')
    st.dataframe(mpg_selected_manufacturer)


    #2. 회사명을 따로 변수로 분리
    company ="hyundai"
    st.header("2번")
    mpg_hyundai = mpg.query('manufacturer == @company')
    st.dataframe(mpg_hyundai)

    #1. query문에 직접 회사명을 쓴다.
    mpg_hyundai = mpg.query('manufacturer == "hyundai"')
    st.header("1번")
    st.dataframe(mpg_hyundai)
    

def main():
    st.header("mpg 데이터 main입니다.")

if __name__ =='__main__':
    main()
