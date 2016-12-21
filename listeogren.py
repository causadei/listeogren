import liste
import time

acıklama = """
[1] Append metodu
[2] Remove metodu
[3] İnsert metodu
[4] Reverse metodu
[5] Pop metodu
[6] Sort metodu
[7] Sort metodu reverse
[8] Clear metodu
[9] Liste görüntüleme
[10] Çıkış
"""
s = "*"*30
d = "Devam etmek için bir tuşa basın .."
append = """
Listenin sonuna tek öğe eklenmesinin sağlar
Kullanımı : liste.append("öğe") şeklindedir.
"""
remove ="""
Listeden öğe silmeyi sağlar
Kullanımı : liste.remove("öğe")
"""
insert = """
Listenin istenilen konumuna öğe eklemeyi sağlar.
Kullanımı : liste.insert(0,"öğe")
İlk değer 0 listedeki öğenin konumunu belirtir.
0 olarak ilk değeri seçmiş olduk.
"""
reverse = """
Listedeki öğeleri tersden sıralamayı sağlar.
Kullanımı : liste.reverse()
"""
pop = """
Listedeki istediğimiz konumdaki öğeyi silmemizi sağlar.
Kullanımı : liste.pop() ve liste.pop(0)
Pop metoduna değer belirtilmez ise son öğeyi siler.
Değer belirtilir ise belirtilen konumdaki öğeyi siler.
"""
sort = """
Listeyi sıralamayı sağlar.
Kullanımı : liste.sort()
Sıralı olarak listelemeyi sağlar.
Örneğin [a,b,c] veya [0,1,2] gibi ..
Listede harf ve rakam bulunuyorsa rakamlar öncelikli değer olarak başa gelir.
"""
sortreverse = """
Listeyi tersden sıralamayı sağlar.
Kullanımı : liste.sort(reverse=True)
Tersden sıralı olarak listelemeyi sağlar.
Örneğin [c,b,a] veya [2,1,0] gibi ..
Listede harf ve rakam bulunuyorsa harfler öncelikli değer olarak başa gelir.
"""
clear = """
Listeyi temizleyi sağlar.
Kullanımı : liste.clear()
"""
while True:
    print(acıklama)
    try:
        sec = input("Yapmak istediğiniz işlemi seçin: ")
        if sec == "1":
            print(append)
            print(s)
            liste.ekle()
            input(d)
        elif sec == "2":
            print(remove)
            print(s)
            liste.sil()
            input(d)
        elif sec == "3":
            print(insert)
            print(s)
            liste.basaekle()
            input(d)
        elif sec == "4":
            print(reverse)
            print(s)
            liste.tercevir()
            input(d)
        elif sec == "5":
            print(pop)
            print(s)
            liste.isteksil()
            input(d)
        elif sec == "6":
            print(sort)
            print(s)
            liste.duzgunliste()
            input(d)
        elif sec == "7":
            print(sortreverse)
            print(s)
            liste.tersliste()
            input(d)
        elif sec == "8":
            print(clear)
            print(s)
            liste.temizle()
            input(d)
        elif sec == "9":
            print(s)
            liste.goster()
            input(d)
        elif sec == "10":
            print("Çıkış Yapılıyor ..")
            time.sleep(2)
            break
        else:
            pass
    except:
        print("Hata!")
