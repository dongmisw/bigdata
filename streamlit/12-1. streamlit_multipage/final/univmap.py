#############################
## 서울지역 대학 표시하기
#############################
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# tiles='OpenStreetMap'
# seoul_map = folium.Map(location=[37.55,126.98], 
#                        tiles = "OpenStreetMap",
#                        zoom_start=12)
# seoul_map.show_in_browser()
# seoul_map.save('./seoul.html')

# tiles = 'cartodbpositron'
# seoul_map2 = folium.Map(location=[37.51,126.88], 
#                         tiles = 'cartodbpositron', 
#                         zoom_start=15) # 학교위치. 
# seoul_map2.show_in_browser()

def page():

    st.title('서울지역 대학교 지도입니다.')

    # Folium 지도 생성 
    #df = pd.read_excel('https://github.com/dongmisw/python_programming/blob/main/data/seoul_univ.xlsx?raw=true', index_col=0)
    df = pd.read_excel('seoul_univ.xlsx', index_col=0)
    print(df)
    seoul_map3=folium.Map(location=[37.55,126.98] , tiles = 'cartodbpositron', zoom_start=12)

    for name, lat, lng in zip (df.index, df.위도, df.경도) : 
         folium.Marker([lat, lng], popup=name).add_to(seoul_map3)
        # folium.CircleMarker([lat, lng],
        #                     radius=10, 
        #                     color='brown',
        #                     fill=True,
        #                     fill_color='coral',
        #                     fill_opacity=0.7,
        #                     popup=name
        #                     ).add_to(seoul_map3)
    #seoul_map3.save('seoul_univ.html')
    #seoul_map3.show_in_browser() 
   
    # Streamlit에서 지도 표시
    #         st_data = st_folium(m, width=725)
    st_folium(seoul_map3, width=1000)

    st.title('완료')

