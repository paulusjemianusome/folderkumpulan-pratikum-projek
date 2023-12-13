import os
os.system('clear')

nim = [2,3,1,0,3,1,0,6,3]
print(nim)
# akses item
print('item indeks 0:',nim[0])
print('item indeks 3:',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])
# akses indeks negatif
print('item indeks terakhir:',nim[-1])
print('item indeks pertama:',nim[-len(nim)])
print('item indeks 3: [-6] ',nim[-6])
print('item indeks 5: [-4] ',nim[-4])
print('item indeks -7: [2] ',nim[2])
print('item indeks 2: [-7] ',nim[-7])
# akses indeks batas
print(f'item indeks 1,2,....: {nim[1:]}')
print(f'item indeks 3,4,....: {nim[3:]}')
print(f'item indeks 0,1,2,3: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8]: {nim[:-1]}')
print(f'item indeks [:4]: {nim[:-5]}')
# pengirisan
print(f'item indeks 1,2: {nim[1:3]}')
print(f'item indeks []: {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:5]}')
print(f'item indeks [1:8]: {nim[1:-1]}')
print(f'item indeks [2:7]: {nim[2:-2]}')
# Nested List
kelas = [('Kaldas',3),
         ('Sainster',3)]
print(kelas)
kelas.append(('Cinta',2))
kelas.append(('Agama katolik',3))
kelas.append(('Pancasila',2))
print(kelas)
# tambahkan matkul 4 dan 5 dan sksnya

# Mata kuliah 1: Matkul1 dengan 3 sks
print(f'Mata kuliah 1:{kelas[0][0]} dengan {kelas[0][1]} sks ')
# Mata kuliah 2: Matkul2 dengan 3 sks
print(f'mata kuliah 2 :{kelas[1][0]} dengan {kelas[1][1]} sks ')
# Mata kuliah 3: Matkul3 dengan 2 sks
print(f'mata kuliah 3 : {kelas [2][0]} dengan {kelas[2][1]} sks')
# Mata kuliah 4: Matkul4 dengan 3 sks
print(f'mata kuliah 4 : {kelas [3][0]} dengan {kelas[3][1]} sks')
# Mata kuliah 5: Matkul5 dengan 2 sks
print(f'mata kuliah 5 : {kelas [4][0]} dengan {kelas[4][1]} sks')

data = [('Paulus',2023,'Aktif'),
        (80,98,100,97,100),
        [3,3,2,3,2],
        ('S1-Reguler','Sistem Informasi B','Ganjil')]

# Nama mahasiswa: Paulus
print(f'Nama mahasiswa: {data[0][0]}')
# Inisial Paulus: P
print(f'inisial {data[0][0]} : {data[0][0][0]}')
# NIM Paulus: 231031063
nim_int = int("".join(map(str,nim)))
print(f'NIM {data[0][0]}: {nim_int} ')
# Program Paulus: S1-Reguler Sistem Informasi B
print(f'Program {data[0][0]}:{data[3][0]} {data[3][1]}')
# Angkatan Paulus: Ganjil-2023
print(f'Angkatan {data[0][0]}: {data[3][2]}-{data[0][1]}')
# Total sks Paulus adalah: 13
print(f'Total sks {data[0][0]} adalah: {sum(data[2])}')
# Jumlah Nilai Paulus: 5
print(f'Jumlah Nilai {data[0][0]}:{len(data[1])}')
# Nilai tertinggi Paulus: 100
print(f'Nilai Tertinggi {data[0][0]}: {max(data[1])}')
# Nilai terendah Paulus: 
print(f'Nilai Tertinggi {data[0][0]}: {min(data[1])}')
# Rata-rata nilai Paulus: 95.0
x_bar = sum(data[1])/len(data[1])
print(f'Rata-rata nilai {data[0][0]}: {x_bar}')








