import streamlit as st
def page():
    st.title('mpg data analysis')
    st.title('page1.py이 단독으로 실행되지 않았습니다.')

def main():
    st.title("page1.py가 단독으로 실행되었습니다.")

if __name__ =='__main__':
    main()
