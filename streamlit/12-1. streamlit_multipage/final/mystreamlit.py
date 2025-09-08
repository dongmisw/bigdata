import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import page1
import page2
import page3 as p3
import page4
import univmap
#mystreamlit.py 입니다. 
def main():
    #main함수입니다.
    st.sidebar.title("mystreamlit sidebar")
    st.sidebar.image("logo.png")
    selected = st.sidebar.selectbox("page를 선택하세요.",
               ['home', 'mpg데이터','plotly chart', '지도데이터',  \
                '워드클라우드', '대학교지도']) 
    if selected == "home":
        page()
    elif selected =="mpg데이터":
        page1.page()
    elif selected =="워드클라우드":         #else if 
        page2.page()  #page2.py 에 정의되어 있는 page()호출
    elif selected == "plotly chart":
        p3.page()
    elif selected == "지도데이터":
        page4.page()
    elif selected == "대학교지도":
        univmap.page() 

def page():
    st.title("데이터분석")
    st.image("cat1.jpg")
    #page함수입니다. 

if __name__ =='__main__':
    main()
