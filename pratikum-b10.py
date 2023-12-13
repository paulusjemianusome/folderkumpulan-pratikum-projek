import os 
os.system("cls")

def judul():
    #judul
    print("program menghitung volume dan luas permukaan".center(45))
    print("menghitung luas balok".center(45))
    print()

def inputan():
    panjang = float(input("masukan lebar : "))
    lebar = float(input("masukan lebar : "))
    tinggi = float(input("masukan tinggi : "))
    return panjang,lebar,tinggi

def hitung(panjang,lebar,tinggi):
    volume = panjang*lebar*tinggi
    luas_surf = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)
    luas_non_surf = luas_surf - panjang*lebar
    return volume,luas_surf,luas_non_surf

def main():
    while True:
        #judul
        judul()
        #input
        panjang,lebar,tinggi = inputan()
        #hitung
        volume,luas_surf,luas_non_surf = hitung(panjang,lebar,tinggi)
        #tampilan
        print(f"nilai nilai volume = {volume}")
        print(f"nilai luas permukaan = {luas_surf}")
        print(f"nilai luas permukaan tanpa tutup : {luas_non_surf}")
        
        #pilihan
        back = input("lanjut?(y/n) : ").lower()
        if back == "y":
            os.system("cls")
            pass
        else:
            print("terima kasih")
            break

main()