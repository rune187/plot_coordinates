import folium
from datetime import datetime


plain_datas = ''''''

now = datetime.now().strftime('%Y-%m-%d %H:%M')
temporary = ''
list_datas = []
LATs = []
LONGs = []

for i in plain_datas:
    if i == '\n':
        list_datas.append(temporary)
        temporary = ''
    else:
        temporary += i

for one_shot in list_datas:
    LATs.append(one_shot[5:17])
    LONGs.append(one_shot[24:])

try:
    map = folium.Map(location=[LATs[0], LONGs[0]], zoom_start=14) # ここで初期位置の中心を決定

    for i in range(len(LATs)):
        folium.Marker(location=[LATs[i], LONGs[i]], popup=i).add_to(map)

    map.save(f'map_{now}.html')
except:
    print('LATs or LONGs list is empty')
    
