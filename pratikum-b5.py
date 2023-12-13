import os
os.system ('clear')

nim = (2,3,1,0,3,1,0,6,3)
print (nim)
# akses item 
print ('item indeks 0 :',nim[0])
print ('item indeks 0 :',nim[3])
print ('item indeks terahir :',nim[len(nim)-1])
# akses indeks negatif
print ('item indeks 0 :',nim[-1])
print ('item indeks pertama :',nim[-len(nim)])
print ('item indeks 3 : [-6]  ',nim [-6])
print ('item indeks 5 : [-4]  ',nim [-4])
print ('item indeks -7 : [2]  ',nim [-4])
print ('item indeks 2 : [-7]  ',nim [-4])
#akses indeks batas
print (f'isi nya  nim ta,......:{nim [0:]}')  
print (f'item indeks 3,4,......:{nim [3:]}')
print (f'item indeks 0,1,2,3....:{nim [4:]}') 
print (f'item indeks 0 :{nim [1:]}')
print (f'item indeksindeks semua:{nim [:]}')
print (f'item indeks [:8]:{nim [:-1]}')
print (f'item indeks [:4]:{nim [:-5]}')
#  pengirisan
print (f'item indeks 1,2,:{nim [1:3]}')
print (f'item indeks []:{nim [1:3]}')
print (f'item indeks 2,3,4:{nim [2:5]}')
print (f'item indeks[1:8]]:{nim [1:-1]}')
print (f'item indeks [2:7]]:{nim [2:-2]}')
# nested  list
kelas = [('Kaldas1',2),
         ('inggris2',3)]
print ( kelas)
kelas.uppend  (('indo3',2))
kelas.uppend (('Agama Katolik',3))
kelas.uppend (('prog',3))
print ( kelas)
# Tambahkan matkul 4 dan 5

# mata kuliah 1: matkul1 denga 2 sks
# mata kuliah 1: matkul2 denga 3 sks
# mata kuliah 1: matkul3 denga 2 sks
# mata kuliah 1: matkul4 denga .. sks
# mata kuliah 1: matkul5 denga ..sks 







