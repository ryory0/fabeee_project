import streamlit as st
import datetime



def header(subheader):
    st.title("Fudo Market")
    st.text_input(label=' ', placeholder="検索")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("ショッピング", use_container_width=True): st.switch_page('Home.py')
    with col2:
        if st.button("レシピ", use_container_width=True): st.switch_page('pages/Recipe.py')
    with col3:
        if st.button("トピック", use_container_width=True): st.switch_page('pages/Topic.py')
    st.divider()
    st.subheader(subheader)
    st.divider()






# from openpyxl import load_workbook
# from io import BytesIO
# import time



# # streamlitオブジェクトクラス
# class stObject:
#     instances = [] # クラス変数
    
#     def __init__(self, category, name, label, value='', bool=''):
#         self.category = category
#         self.name = name
#         self.label = label
#         self.value = value
#         self.bool = bool
#         stObject.instances.append(self)
    
#     @classmethod
#     def getInstances(cls): return cls.instances # 作成したインスタンスをすべて取得



# # ヘッダー
# def Header(name):
#     st.title(f'{name} 点検報告書')
#     st.caption('点検報告書を作成し、Excel形式で保存できます')
#     col1, col2 = st.columns([1,2])
#     with col1:
#         col1_1, col1_2, col1_3 = st.columns([4,1,8])
#         with col1_1: st.page_link('Home.py', label='ホーム')
#         with col1_2: st.write('**>**')
#         with col1_3: st.page_link(f'pages/{name}.py', label=f'{name}')
#     st.divider()



# # 機器情報
# def Info():
#     # インスタンス
#     info1 = stObject('機器情報', '機種名', '１．機種名')
#     info2 = stObject('機器情報', '製造番号', '２．製造番号')
#     info3 = stObject('機器情報', '製造販売業者', '３．製造販売業者')
#     info4 = stObject('機器情報', '機器管理番号', '４．機器管理番号')
#     info5 = stObject('機器情報', '購入年月日', '５．購入年月日')
#     info6 = stObject('機器情報', '実施年月日', '６．実施年月日')
    
#     st.header('機器情報')
#     col1, col2 = st.columns(2)
#     with col1:
#         info1.value = st.text_input(info1.label) # 機種名
#         info3.value = st.text_input(info3.label) # 製造販売業者
#     with col2:
#         info2.value = st.text_input(info2.label) # 製造番号
#         def update_default():
#             st.session_state['デフォルト'] = st.session_state[info4.name] + ' 点検報告書' # デフォルトを更新
#             if not st.session_state['トグル']: # トグルがOFFだったら
#                 st.session_state['ファイル名'] = st.session_state['デフォルト'] # 表示するファイル名をデフォルトにする
#                 st.session_state['新ファイル名'] = st.session_state['デフォルト'] # 新ファイル名をデフォルトにする
#         info4.value = st.text_input(info4.label, key=info4.name, on_change=update_default) # 機器管理番号
#     col1, col2 = st.columns(2)
#     with col1: info5.value = st.date_input(info5.label, value=datetime.date(2000, 1, 1), min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2099, 12, 31)) # 購入年月日
#     with col2: info6.value = st.date_input(info6.label) # 実施年月日
#     st.divider()
#     return info1, info2, info3, info4, info5, info6



# # 電気的安全性点検
# def Eli(toggle=False):
#     # インスタンス
#     eli1 = stObject('電気的安全性点検', '接触電流（NC）', '正常状態（NC）：100μA以下')
#     eli2 = stObject('電気的安全性点検', '接触電流（SFC）', '単一故障状態（SFC）：500μA以下')
#     eli3 = stObject('電気的安全性点検', '接地漏れ電流（NC）', '正常状態（NC）：5,000μA以下')
#     eli4 = stObject('電気的安全性点検', '接地漏れ電流（SFC）', '単一故障状態（SFC）：10,000μA以下')
#     eli5 = stObject('電気的安全性点検', '接地線抵抗', '0.2Ω以下', '     ー', 'ー')
    
#     def return_numin(label, step, threshold, min=0.0, format='%.1f'):
#         value = st.number_input(label, min_value=min, format=format, step=step)
#         return value, value <= threshold # (値, T or F)
    
#     def contents():
#         st.subheader('電気的安全性点検')
#         st.write('**接触電流**')
#         col1, col2 = st.columns(2)
#         with col1: eli1.value, eli1.bool = return_numin(eli1.label, step=0.1, threshold=100) # 接触電流（NC）
#         with col2: eli2.value, eli2.bool = return_numin(eli2.label, step=0.1, threshold=500) # 接触電流（SFC）
#         st.write('**接地漏れ電流**')
#         col1, col2 = st.columns(2)
#         with col1: eli3.value, eli3.bool = return_numin(eli3.label, step=0.1, threshold=5000) # 接地漏れ電流（NC）
#         with col2: eli4.value, eli4.bool = return_numin(eli4.label, step=0.1, threshold=10000) # 接地漏れ電流（SFC）
#         toggle1 = st.toggle('**接地線抵抗**')
#         if toggle1: eli5.value, eli5.bool = return_numin(eli5.label, step=0.01, threshold=0.2, format='%.2f') # 接地線抵抗
    
#     st.header('点検')
#     contents() if toggle and st.toggle('電気的安全性点検') else contents()
#     st.divider()
#     return eli1, eli2, eli3, eli4, eli5



# # 外装点検・機能点検・性能点検のチェックボックス
# def Checkbox(*args):
#     for instance in args: instance.bool = st.checkbox(instance.label)



# # 設定値
# def settingAction(instance, key, new_key, min, max, unit, value=0.0, min_value=0.0, format='%.1f', step=0.1):
#     if key not in st.session_state: st.session_state[key] = value
#     def update(): st.session_state[key] = st.session_state[new_key]
#     instance.value = st.number_input(f'{instance.label}（{str(min)} ～ {str(max)} {unit}）', value=st.session_state[key], min_value=min_value, format=format, step=step, key=new_key, on_change=update)
#     st.session_state[key] = instance.value
#     instance.bool = min <= instance.value and instance.value <= max
#     return instance

# # 流量点検
# def Flow(percent):
#     # インスタンス
#     flow = stObject('性能点検', '流量精度', '１．流量精度')
    
#     st.write('**流量点検**')
#     col1, col2 = st.columns(2)
#     with col1: set = st.number_input('設定値（ml/h）', value=120, min_value=0, step=1) # 設定値
#     min, max = round(set-(set*percent/100), 1), round(set+(set*percent/100), 1)
#     with col2:
#         flow = settingAction(flow, 'flow', 'new_flow', min, max, 'ml/h') # 流量
#     return set, flow

# # 閉塞圧点検
# def Pressure():
#     # インスタンス
#     pressure = stObject('性能点検', '閉塞圧', '２．閉塞圧')
    
#     st.write('**閉塞圧点検**')
#     col1, col2 = st.columns(2)
#     with col1:
#         col2_1, col2_2, col2_3,= st.columns([10, 1, 9])
#         with col2_1: set1 = st.number_input('規定値（kPa）', value=100.0, min_value=0.0, format='%.1f', step=0.1) # 設定値
#         with col2_2:
#             st.write('')
#             st.write('')
#             st.write('±')
#         with col2_3: set2 = st.number_input(' ', value=10.0, min_value=0.0, format='%.1f', step=0.1) # 設定値
#     min, max = round(set1-set2, 1), round(set1+set2, 1)
#     with col2:
#         pressure = settingAction(pressure, 'pressure', 'new_pressure', min, max, 'kPa') # 閉塞圧
#     return set1, set2, pressure

# # SPO2
# def Spo2():
#     # インスタンス
#     spo2 = stObject('性能点検', '酸素飽和度', '１．酸素飽和度測定精度（93 ～ 100 %）')
#     pulse = stObject('性能点検', '脈拍数', '２．脈拍数測定精度（69 ～ 75 拍）')
    
#     st.subheader('性能点検')
#     st.write('**SPO2**')
#     col1, col2 = st.columns(2)
#     with col1:
#         spo2.value = st.number_input(spo2.label, min_value=0, max_value=100, format='%d', step=1) # 酸素飽和度測定精度
#         spo2.bool = 93 <= spo2.value and spo2.value <= 100
#     with col2:
#         pulse.value = st.number_input(pulse.label, min_value=0, step=1) # 脈拍数測定精度
#         pulse.bool = 69 <= pulse.value and pulse.value <= 75
#     return spo2, pulse

# # 体温部
# def Temperature():
#     # インスタンス
#     temperature = stObject('性能点検', '体温部', '４．体温測定精度', '   ー', 'ー')
#     set = 'ー'
    
#     if st.toggle('**体温部**'):
#         col1, col2 = st.columns(2)
#         with col1:
#             set = st.number_input('設定値（℃）', value=37.0, format='%.1f', step=0.1)
#             set, min, max = round(set, 1), round(set-0.1, 1), round(set+0.1, 1)
#         with col2:
#             temperature = settingAction(temperature, 'temperature', 'new_temperature', min, max, '℃', min_value=None) # 体温測定精度
#     return set, temperature

# # 血圧部
# def blood_pressure():
#     # インスタンス
#     up = stObject('性能点検', '血圧部（上限）', '５．最高血圧警報測定(上限値)')
#     down = stObject('性能点検', '血圧部（下限）', '６．最高血圧警報測定(下限値)')
    
#     st.write('**血圧部**')
#     col1, col2 = st.columns(2)
#     with col1:
#         set_up = st.number_input('設定値（mmHg）', value=120, step=1)
#         min1, max1 = set_up-20, set_up+130
#     with col2:
#         up = settingAction(up, 'up', 'new_up', min1, max1, 'mmHg', value=0, min_value=None, format='%d', step=1) # 最高血圧警報測定(上限値)
#     col1, col2 = st.columns(2)
#     with col1:
#         set_down = st.number_input('設定値（mmHg）', value=80, step=1)
#         min2, max2 = set_down-20, set_down+70
#     with col2:
#         down = settingAction(down, 'down', 'new_down', min2, max2, 'mmHg', value=0, min_value=None, format='%d', step=1) # 最高血圧警報測定(下限値)
#     st.divider()
#     return set_up, up, set_down, down



# # 総合評価
# def Evaluation(eval_ctg):
#     st.subheader('総合評価')
#     errorList = [instance for instance in stObject.getInstances() if instance.category in eval_ctg and instance.bool == False]
#     # 評価
#     if not errorList: st.success('**合格**') 
#     else: 
#         st.warning('**不合格**')
#         st.write('不合格の項目')
#         text = [f'「{error.name}」' for error in errorList]
#         st.warning(''.join(text))
#     st.divider()
#     return errorList



# # 備考
# def Remarks():
#     st.subheader('備考')
#     text_area = stObject('備考', '備考', ' ')
#     text_area.value = st.text_area(text_area.label)
#     st.divider()
#     return text_area



# # ファイル名
# def FileName():
#     # ダウンロード
#     st.subheader('ダウンロード', help='点検報告書をExcel形式でダウンロードします')
    
#     # 初期値設定
#     if 'デフォルト' not in st.session_state: st.session_state['デフォルト'] = '点検報告書'
#     if 'ファイル名' not in st.session_state: st.session_state['ファイル名'] = '点検報告書'
#     if '新ファイル名' not in st.session_state: st.session_state['新ファイル名'] = '点検報告書'
#     if 'トグル' not in st.session_state: st.session_state['トグル'] = False

#     # 現在のファイル名
#     st.write('現在のファイル名：' + st.session_state['ファイル名'] + '.xlsx')

#     # トグル
#     def update_toggle(): st.session_state['ファイル名'] = st.session_state['デフォルト'] # ファイル名をデフォルトにする
#     if st.toggle('ファイル名 変更', key='トグル', on_change=update_toggle):
#         def update_file_name(): # 新ファイル名を入力後に（注：トグルが変更されるたびに起動する）
#             if st.session_state['トグル']: st.session_state['ファイル名'] = st.session_state['新ファイル名'] # トグルがONなら、ファイル名を新ファイル名にする
#         st.text_input('新しいファイル名', key='新ファイル名', value=st.session_state['ファイル名'], on_change=update_file_name)
#     st.divider()



# # 作成ボタン
# def CreateButton():
#     # # 初期化
#     if 'ダウンロードボタン' not in st.session_state: st.session_state['ダウンロードボタン'] = False
#     if 'プログレスバー' not in st.session_state: st.session_state['プログレスバー'] = False
#     if st.button('作成', use_container_width=True):
#         # 表示
#         file_name = st.session_state['ファイル名'] + '.xlsx'
#         st.write(f'「{file_name} 」を作成しました\n\n下部の「ダウンロード」からファイルをダウンロードしてください')
#         st.session_state['ダウンロードボタン'] = True
        


# # Excelに共通項目を入力
# def WriteCommon(sheet):
#     # 合格・不合格
#     bools = [instance.bool for instance in stObject.getInstances() if '点検' in instance.category] # 点検項目のboolをすべて取得
#     for i, bool in enumerate(bools, start=11): sheet[f'H{i}'] = ('ー' if bool == 'ー' else '合格' if bool else '不合格') # H11から入力

#     # 機器情報
#     info_cells = ['E3', 'B5', 'B6', 'B7', 'B8', 'E8']
#     info_values = [instance.value for instance in stObject.getInstances() if instance.category in '機器情報']
#     for cell, value in zip(info_cells, info_values): sheet[cell] = value # 機器情報を入力
#     # 電気的安全性点検
#     eli_values = [instance.value for instance in stObject.getInstances() if instance.category in '電気的安全性点検']
#     for i, value in enumerate(eli_values, start=11): sheet[f'F{i}'] = value # F11から入力



# # 保存
# def Save(wb):
#     byte_xlsx = BytesIO()
#     wb.save(byte_xlsx)
#     wb.close()
#     byte_xlsx.seek(0)
#     return byte_xlsx



# # ダウンロードボタン
# def DownloadButton(data):
#     file_name = st.session_state['ファイル名'] + '.xlsx'
#     mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#     download = st.download_button(label='ダウンロード', data=data, file_name=file_name, mime=mime, use_container_width=True)
#     if download: st.session_state['プログレスバー'] = True



# # プログレスバー
# def ProgressBar():
#     if st.session_state['プログレスバー']:
#         # progress_bar = st.progress(0) # 進行バーの初期化
#         # for i in range(100):
#         #     progress_bar.progress(i + 1)
#         #     time.sleep(0.01)
#         # progress_bar.empty()
#         st.success(f'「{st.session_state["ファイル名"]}.xlsx」をダウンロードしました')
#         st.caption('※エラー発生時は、もう一度「作成」＞「ダウンロード」の順に押して下さい')
#         st.session_state['ダウンロードボタン'] = False
#         st.session_state['プログレスバー'] = False