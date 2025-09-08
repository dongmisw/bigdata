import streamlit as st
import json
import folium
import pandas as pd
from streamlit_folium import st_folium

def page():
    st.title("지도데이터")

    #1) streamlit에서 지도 표현 (marking)
    # 서울 중심, 동양미래대학교 두개 표현
    data1 =pd.DataFrame({
        'lat': [37.5665, 37.50108],
        'lon': [126.9780, 126.8675]
    })
    st.map(data1)
 
    #2)
    # center on Liberty Bell, add marker
    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    folium.Marker(
        [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)

    #3) 한국 인구 밀집 지도

    geo = json.load(open('SIG.geojson', encoding = 'UTF-8'))
    df_pop = pd.read_csv('Population_SIG.csv')
    map_sig = folium.Map(location = [35.95, 127.7],
                      zoom_start =7, 
                     tiles='cartodbpositron') # 지도 종류 - 단계 구분이 잘되는 밝은색 지도
    bins = list(df_pop["pop"].quantile([0, 0.2, 0.4, 0.6, 0.8, 1]))

    # 단계별 구분도 만들기
    folium.Choropleth(
        geo_data=geo,                      # 지도 데이터
        data =df_pop,                      # 통계 데이터
        columns = ('code', 'pop'),         # df_pop의 행정구역 코드, 인구
        key_on = 'feature.properties.SIG_CD', # geo 행정 구역 코드
        fill_color = 'YlGnBu',                # 컬러 맵
        fill_opacity = 1,                     # 투명도
        line_opacity = 0.5,                   # 경계선 투명도
        bins = bins).add_to(map_sig)          # 계급 구간 기준 값 / 배경 지도에 추가
    st_data = st_folium(map_sig, width=725)



