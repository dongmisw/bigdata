import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import page1

def main():
    #main함수입니다.
    st.sidebar.title("mystreamlit sidebar")
    selected = st.sidebar.selectbox("page를 선택하세요.",
               ['home','mpg data analysis'])
    if selected == "home":
        page()
    elif selected =="mpg data analysis":
        page1.page()

def page():
    st.title("데이터분석_HOME")
    st.image("cat1.jpg")
    #page함수입니다. 

if __name__ =='__main__':
    main()
