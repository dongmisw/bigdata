# page2.py
import streamlit as st
import re
import konlpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def page():
    st.title("page2.py이 실행됨- word cloud")

    president_speech = open('speech_moon.txt', encoding = 'UTF-8').read()
    president_speech = re.sub('[^가-힣]', ' ', president_speech)  # 두번째 파라미터가 공백 문자임에 주의
    st.text(president_speech)

    hannanum = konlpy.tag.Hannanum()
    nouns = hannanum.nouns(president_speech)
    df_word = pd.DataFrame( {'word' : nouns})

    df_word['word_n'] = df_word['word'].str.len()
    df_word = df_word.query('word_n >= 2')
    df_word = df_word.groupby('word', as_index=False) \
                .agg(n = ('word', 'count')) \
                .sort_values('n', ascending=False)
    
    st.dataframe(df_word)

    top20 = df_word.head(20)
    plt.rcParams.update( {'font.family' : 'malgun Gothic',  # 한글 폰트
                      'figure.dpi' : '120',             # 해상도
                      'figure.figsize' : [6.5, 6]})     # 가로, 세로 크기

    #bar graph그리기
    fig = plt.figure()
    sns.barplot(data=top20, y='word', x='n')
    st.pyplot(fig)

    font = 'DoHyeon-Regular.ttf'
    #DataFrame을 dictionary로 변경 
    dic_word = df_word.set_index('word').to_dict()['n']

    # wc 만들기
    wc = WordCloud(random_state = 710,         # 난수 고정, 항상 같은 모양으로 생성
                    font_path = font,           # 폰트 설정
                    width = 400,                # 가로 크기
                    height = 400,               # 세로 크기
                    background_color = 'white') # 배경색

    # 워드 클라우드 만들기
    img_wordcloud = wc.generate_from_frequencies(dic_word)

    # 워드 클라우드 출력하기
    # 자주 사용한 단어는 크게 표시됨
    fig2 = plt.figure(figsize = (5, 5))            # 액자 사이즈
    plt.axis('off')                         # 테두리 선 없애기
    plt.imshow(img_wordcloud)   
    st.pyplot(fig2)