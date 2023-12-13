profil = {'nama' : 'Paulus Jemianus Ome',
          'nim'  : 231031063,
          'tgl'  : '18,November,2002',
          'kls'  : 'SI23B',
          'prodi': 'sistem informasi',
          'jkl'  : 'laki laki'
          }
print(profil)
print()
print('Biodata'.center(70))
print()
print(f"""Nama          : {profil['nama']}
NIM           : {profil['nim']}
Tanggal       : {profil['tgl']}
Kelas         : {profil['kls']}
Prodi         : {profil['prodi']}
Jenis Kelamin : {profil['jkl']}""")
    