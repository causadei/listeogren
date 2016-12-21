liste = []
s = "*"*30
def ekle(): #listenin sonuna tek öğe eklemek
    a = input("Listeye eklenecek öğeyi girin: ")
    liste.append(a)
    print(s)
    print("Listeye eklenen öğe {}".format(a))
def sil(): #listeden öğe silmek
    try:
        a = input("Listeden silinecek öğeyi girin: ")
        liste.remove(a)
        print("Listeden silinen öğe {}".format(a))
    except:
        print("Silmek istediğiniz öğe listede mevcut değil")

def goster(): #listeyi göstermek
    print(liste)

def basaekle(): #listenin istediğimiz konumuna öğeyi ekler
    a = input("Listeye eklenecek öğeyi girin: ")
    b = int(input("Listenin kaçıncı sırasına eklemek istediğinizi girin: "))
    b -=1
    liste.insert(b,a)
    print(s)
    print("Listeye eklenen öğe {} konumu {}".format(a,b+1))

def tercevir(): #listeyi ters çevirir
    liste.reverse()
    print(liste)

def isteksil(): #listeden istediğimiz konumdaki öğeyi silme
    try:
        a = int(input("Listeden silmek istediğiniz öğenin konumunu girin: "))
        a -= 1
        liste.pop(a)
        print(s)
        print("Seçtiğiniz konumdaki öğe silindi")
    except:
        print("Silmek istediğiniz öğe mevcut değil")

def duzgunliste(): #listeyi sıralar
    liste.sort()
    print(liste)
def tersliste(): #listeyi ters sıralar
    liste.sort(reverse=True)
    print(liste)
def temizle(): #listeyi temizler
    liste.clear()
    print(liste)

