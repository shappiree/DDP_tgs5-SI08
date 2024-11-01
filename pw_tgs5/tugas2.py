pilih = int(input("""Selamat datang diaplikasi menghitung
              1. untuk menghitung luas persegi
              2. untuk menghitung luas lingkaran
              3. untuk menghitung luas segitiga 
              
              masukan pilihan anda :"""))

match pilih:
    case 1 :
              print("Kamu memilih 1 untuk menghitung luas persegi")
              sisi = int(input("masukan sisi persegi: ")) 
              luaspsg = sisi*sisi
              print("luas persegi yang sisinya ", sisi,"adalah", luaspsg)
                    
    case 2 :
             print("Kamu memilih 2 untuk menghitung Lingkaran")
             jari2 = int(input("masukan jari-jari: "))
             luasLkr = 3.14 * jari2  * jari2
             print("luas lingkaran yang jari-jarinya", jari2, "adalah", luasLkr)
             
    case 3 :
             print("Kamu memilih 3 untuk menghitung Segitiga")
             alas = int(input("masukan alas segitiga: "))
             tinggi = int(input("masukan tinggi segitiga"))
             luasSegitiga = 0.5 * alas  * tinggi
             print("luas segitiga dengan alas", alas, "dan tinggi",tinggi, "adalah" ,luasSegitiga)
    case _:
             print("Anda Salah Pilih")