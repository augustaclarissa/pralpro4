#Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Struktur Kontrol Percabangan

'''Kelas 1 SD A sedang mempelajari bilangan - bilangan ganjil. Para siswa sudah dimudahkan dengan teknologi,
hanya butuh 1 inputan kemudian para siswa dapat mengetahui bilangan - bilangan sebanyak 
angka yang sudah diinput. Bantulah membuat programnya!'''

#input : banyaknya bilangan ganjil
#proses : Statement kontrol perulangan dengan For sama seperti sebuah pencacah atau counter. 
        # Sehingga rentang nilai yang diharapkan pada perulangan harus memiliki nilai awal cacahan,
        # nilai akhir cacahan, dan interval cacahan (dimulai dari angka 1, stop di inputan+3, 2 step)
#output : bilangan ganjil, jumlahnya sesuai angka inputan

angka = int(input("Mau menampilkan berapa bilangan ganjil? : "))
for i in range(1,angka+angka,2):
    if (i%2) != 0:
        angka=angka+1
        print("%d "%i, end="") #, perulangan akan dilakukan sebanyak inputan user 
        #dengan setiap perulangan nilai variabel i
    else:
        pass