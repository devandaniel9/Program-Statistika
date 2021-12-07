# Title

'Statistika'

# List import
import statistics
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import math

# Menjalankan program
# streamlit run 'Statistika 3.py'

# Streamlit
st.write("""# Program Statisika""")
st.write('Made by Devan Daniel ')
st.write('- Silahkan pilih data dari sample data yang tersedia atau pilih angka yang anda inginkan (custom) di **Menu Input Data**')
st.write('- Hasil statistika akan muncul otomatis di menu **Hasil**')

st.sidebar.write('## **Menu Input Data**')

data_list = ["Data 1", "Data 2", "Custom"]
data = st.sidebar.selectbox("Sample Data:", data_list)

if data == data_list[0]:
    tabel = [49,23,46,83,46,27,38,67,55,91]
if data == data_list[1]:
    np.random.seed(1)
    x = np.random.normal(50,5,30)
    tabel = []
    for i in list(x):
        tabel.append(math.floor(i))


if data == data_list[2]:
    x = int(st.sidebar.number_input("Masukkan jumlah data yang ingin dimasukkan:", value=5, min_value=0))
    tabel = []
    for i in range(x):
        tabel.append(int(st.sidebar.number_input(f"Masukkan angka ke {i+1}", value=0)))


grafik_list = ["Garis", "Titik", "Batang", "Lingkaran", "Histogram"]
grafik = st.sidebar.selectbox("Jenis Grafik:", grafik_list)


df = pd.DataFrame()

df['Data'] = tabel
#df.set_index('Data', inplace=True)



st.write('## **Input Data**')
st.dataframe(df)

#st.dataframe(df.assign(hack='').set_index('hack'))


st.write('## **Hasil**')

st.info('''
- Total Data   : {}
- Banyak Data  : {}
- Maksimum     : {}
- Minimum      : {}
- Mean         : {}
- Median       : {}
- Mode         : {}

'''.format(sum(tabel),len(tabel), max(tabel),min(tabel),np.mean(tabel),np.median(tabel),statistics.mode(tabel)))



angka = []
for n in range(len(tabel)):
    angka.append(n+1)

if grafik == grafik_list[0]:
    plt.plot(angka, tabel,marker='o')
    plt.xlabel("Data ke")
    plt.ylabel("Nilai")
    plt.xticks(np.arange(min(angka), max(angka)+1, 1.0))
if grafik == grafik_list[1]:
    plt.scatter(angka,tabel)
    plt.xlabel("Data ke")
    plt.ylabel("Nilai")
    plt.xticks(np.arange(min(angka), max(angka)+1, 1.0))
if grafik == grafik_list[2]:
    plt.bar(angka,tabel)
    plt.xlabel("Data ke")
    plt.ylabel("Nilai")
    plt.xticks(np.arange(min(angka), max(angka)+1, 1.0))
if grafik == grafik_list[3]:
    plt.pie(tabel,labels=tabel)
if grafik == grafik_list[4]:
    plt.hist(tabel,bins=10)
    plt.ylabel("Banyak Data")
    plt.xlabel("Kelas")
    


st.write('## **Grafik**')

plt.savefig('Grafik.png')

img = Image.open('Grafik.png')
st.image(img, width=500)



a = '''
st.write(f"Data = {tabel}")
st.write(f"Total data = {sum(tabel)}")
st.write(f"Banyak data = {len(tabel)}")
st.write(f"Maksimum = {max(tabel)}")
st.write(f"Minimum = {min(tabel)}")
st.write(f"Mean = {statistics.mean(tabel)}")
st.write(f"Median = {statistics.median(tabel)}")
st.write(f"Mode = {statistics.mode(tabel)}")
'''
