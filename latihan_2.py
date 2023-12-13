inp = input('Masukkan suatu input: ')
if len(inp) != 3:
 print('Panjang string ', len(inp),'tidak sama dengan 3')
else:
 print('Panjang input sesuai yang diinginkan')
print()
nilai = int(input('Masukan nilai: '))

if nilai >= 90:
    print('kamu dapat rating: A')
elif nilai > 75:
    print('kamu dapat rating: B')
elif nilai > 55:
    print('kamu dapat rating: C')
else:
    print('kamu dapat rating: D')