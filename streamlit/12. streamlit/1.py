import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 

st.title("title -  hello world") 
st.header("header ")
st.subheader("subheader")
st.text("text ")

st.image("cat1.jpg")
st.video("https://youtu.be/2oWN7waCXIo")

st.success("success")
st.info("info")
st.warning("warning")
st.error("error")


mpg= pd.read_csv("mpg.csv")
st.dataframe(mpg)

mpg_drv_cty = mpg.groupby('drv')\
        .agg(mean_cty = ('cty', 'mean'))
st.dataframe(mpg_drv_cty)

fig1 = plt.figure()
sns.barplot(data = mpg_drv_cty, x='drv', y='mean_cty')
st.pyplot(fig1)


tab1, tab2, tab3 =st.tabs(['T1','T2','T3'])

with tab1:
    # T1을 눌렀을때 나오는 tab
    st.header("여기는 tab1입니다.")
    st.image("cat1.jpg")
with tab2:
    # T2을 눌렀을때 나오는 tab
    st.header("여기는 tab2입니다.")
    st.video("https://youtu.be/2oWN7waCXIo")

with tab3: 
    # T3을 눌렀을때 나오는 tab
    st.header("여기는 tab3입니다.")
