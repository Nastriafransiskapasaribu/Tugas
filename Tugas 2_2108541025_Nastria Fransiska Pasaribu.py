#!/usr/bin/env python
# coding: utf-8

# # 5.12 list di phyton

# In[1]:


buah = ['jeruk', 'anggur','pisang','jambu']
print(buah)


# In[2]:


print(buah[0])


# In[3]:


print(buah[2])


# In[4]:


print(buah[-1])


# In[5]:


print(buah[-2])


# In[6]:


buah[0] = 'salak'
print(buah)


# In[7]:


print(buah[0:3])


# In[8]:


# tidak merubah list
print(buah)


# # 5.13 Metoda List

# In[9]:


nama = ['Nastria','fransiska']
nama.append('Pasaribu')
print(nama)
        


# In[10]:


nama.insert(0,'syantik')
print(nama)


# In[11]:


nama.remove('fransiska')
print(nama)


# In[12]:


print('Syantik' in nama)


# In[13]:


print('fransiska' in nama)


# In[14]:


print(len(nama))


# # 5.14 For loop
# For loop dapat digunakan untuk memanggil semua isi list.

# In[15]:


buah = ['jambu','nangka','apel','salak']
for jenis in buah:
    print(jenis)


# In[16]:


i = 0
while i < len(buah[i]):
    print(buah[i])
    i+=1


# # 5.15 Fungsi range
# fungsi range berguna untuk membangkitkan bilangan berurutan atau berpola yang kita inginkan.

# In[17]:


angka = range(8)
print(angka)


# In[18]:


for isi in angka:
    print(isi)


# In[19]:


for isi in range(5,12):
    print(isi)


# In[20]:


for isi in range(0,14,3):
    print(isi)


# # latihan

# # 1.buatlah program untuk mencari nilai terbesar didalam suatu list.

# In[21]:


data = [4,1,6,8,9,2,4,3,5]
terbesar = data[0]
for i in range(len(data)):
    if data[i] > terbesar:
        terbesar = data[i]
print(terbesar)


# In[22]:


data = [2,23,56789,234567,123,987,589,325,367,80,]
terbesar = data[1]
for angka in data:
    if angka > terbesar:
        terbesar = angka 
print(terbesar)


# # 2. buatlah program untuk membuat anggota list menjadi unik dengan kata lain tidak ada anggota list yang kembar.

# In[23]:


angka = [9,3,4,1,6,0,8,5,7,8,1,]
angka_unik = []
for angka in angka:
    if angka not in angka_unik:
        angka_unik.append(anggota)
print(angka_unik)


# # list 2 dimensi
# list 2 dimensi pada umumnya adalah menempatkan sebuah list di dalam list. penggambarannya seperti sebuah matriks.

# In[24]:


matrik = [
    [5,6,7,8],
    [10,11,12,13],
    [14,15,16,17,18]
]
print(matrik)


# In[25]:


matrik[1]


# In[26]:


matrik[2][3]


# In[27]:


matrik[1][2]=23456
print(matrik[1][2])


# In[28]:


matrik


# In[29]:


for baris in matrik:
    print(baris)
    for kolom in baris:
        print(kolom)


# # 5.17 Tuples
# tuples mirip dengan list, akan tetapi tuples tidak dapat merubah isinya. jika kita memiliki data yang tidak ingin dirubah isinya,kita gunakan tuples,sedangkan jika datanya masih ingin dimanipulasi kedepannya gunakan list.

# In[30]:


angka = (2,4,6,4,2,1,4,6,2,7)
print(angka[2])


# In[31]:


print(angka[2:4])


# In[32]:


for isi in angka[2:4]:
    print(isi)


# In[33]:


angka[0]


# In[34]:


angka.append(10)


# In[35]:


angka.remove(5)


# In[36]:


angka.count(1)


# In[37]:


angka.index(4)


# # 5.18 Dictionaries
# dictionaries digunakan juka data nya terkait satu sama lain. misalnya data seseorang yang terdisri dari umur,nama, tanggal lahir merupakan satu kesatuan data yang bersumber dari orang tersebut.

# In[38]:


data_orang = {
    "nama" : "Nas Pasaribu",
    "umur" : 19,
    "apakah_singel" : False
}
print(data_orang['nama'])


# In[39]:


print(data_orang.get('nama'))


# In[40]:


print(data_orang['Nama'])


# In[41]:


print(data_orang.get('tanggal_lahir','6-7-2002'))


# In[42]:


print(data_orang)


# In[43]:


data_orang['NIM'] = '2108541025'


# In[44]:


print(data_orang["NIM"])


# In[45]:


print(data_orang)


# In[46]:


data_orang['Alamat'] = 'Ungasan'
print(data_orang['Alamat'])


# In[47]:


print(data_orang)


# # latihan
# buatlah program untuk merubah no hp yang tadinya beruoa angka menjadi sebutan bilangan tersebut. Misalnya angka 0812 menjadi nol delapan satu dua

# In[48]:


angka ={
    "0" : "nol"
    "1" : "satu"
    "2" : "dua"
    "3" : "tiga"
    "4" : "empat"
    "5" : "lima"
    "6" : "enam"
    "7" : "tujuh"
    "8" : "delapan"
    "9" : " sembilan"
}


# In[ ]:


nomor_HP = input("Masukkan nomor HP anda")
nomor_angka = " "
for isi in nomor_HP:
    nomor_angka += angka.get(isi) + " "
print(nomor_angka)


# In[ ]:


nomor_HP = input("Masukkan nomor HP anda ")
nomor_angka = "1. "
for isi in nomor_HP:
    nomor_angka += angka.get(isi) +" "
    print(nomor_angka)


# # Fungsi dalam python
# pada dasarnya fungsi dibentuk untuk menghindari pengulangan pembuatan program secara manual dimana fungsi tersebut memiliki pengulangan yang tinggidalam program yang kita buat.

# In[ ]:


first_name = input("Nama depan anda adalah Nastria ")
last_name = input("Nama belakang anda adalah Pasaribu")
full_nama(first_name,last_name)


# # 5.19.1 Tugas Fungsi Pada python

# In[ ]:


def waktu_sampai(jarak,kecepatan):
    waktu = jarak/kecepatan
    print(waktu)


# In[ ]:


def waktu_tempuh(jarak,kecepatan):
    waktu = jarak/kecepatan
    return waktu


# In[ ]:


waktu_sampai(80,60)


# In[ ]:


waktu_tempuh(80,60)


# In[ ]:


a = waktu_sampai(80,60)
print(a)


# In[ ]:


b = waktu_tempuh(80,60)
print(b)


# # Latihan
# buatlah program yang menggunakan fungsi di python untuk mengitung luas segitiga, lingkaran, persegi dan persegi panjang.selain itu berikan peringatan bagi bidang lain yang tidak termasuk dalam perhitungan.

# In[ ]:


import numpy as np


# In[ ]:


def luas_segitiga(alas,tinggi):
    luas = (1/2)*alas*tinggi
    return luas
def luas_lingkaran(jari_jari):
    luas = np.pi*(jari_jari**2)
    return luas
def luas_persegi(sisi):
    luas = sisi**2
    return luas
def luas_persegi_panjang(panjang,lebar):
    luas = panjang*lebar
    return luas


# In[ ]:


jenis_bidang = input("Tulis jenis bidangnya ")
if jenis_bidang.upper() == 'SEGITIGA':
    alas = float(input('Berapakah panjang alasnya? '))
    tinggi = float(input('Berapakah tingginya? '))
    Luas = luas_segitiga(alas,tinggi)
    print(f"Luas {jenis-bidang}) adalah {luas}")
elif jenis_bidang.upper() == 'LINGKARAN':
    alas = float(input('Berapakah panjang jari-jarinya? '))
    Luas = luas_lingkaran(jari_jari)
    print(f"Luas {jenis-bidang}) adalah {luas}")
elif jenis_bidang.upper() == 'PERSEGI': or (jenis_bidang.upper() == 'BUJUR SANGKAR'):
    sisi = float(input('Berapakah panjang sisinya? '))
    Luas = luas_persegi(sisi)
    print(f"Luas {jenis-bidang}) adalah {luas}")
elif jenis_bidang.upper() == 'PERSEGI PANJANG':
    panjang = float(input('Berapakah panjangnya? '))
    lebar = float(input('Berapakah lebarnya? '))
    Luas = luas_persegi_panjang(panjang,lebar)
    print(f"Luas {jenis-bidang}) adalah {luas}")
else:
    print(f"Maaf bidang {jenis_bidang} yang anda masukkan tidak ada.")
    print("pilihan cuma SEGITIGA,LINGKARAN,PERSEGI dan PERSEGI PANJANG.")
    print('Terimakasih')


# In[ ]:




