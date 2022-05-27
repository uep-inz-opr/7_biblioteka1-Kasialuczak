class Ksiazka:
 def __init__(self,lista):
  self.lista=lista
 def dodaj_egzemplarz_ksiazki(self):
  pojedynczalista=set(self.lista)
  informacjaoksiazce=[]
  for i in pojedynczalista:
   tytul=i[0]
   autor=i[1]
   liczbaegzemplarzy=self.lista.count(i)
   informacjaoksiazce.append((tytul,autor,liczbaegzemplarzy))
   informacjaoksiazce.sort(key=lambda x:x[0],reverse=False)
  for j in informacjaoksiazce:
   print (j)

liczbaksiazek=int(input())
listaksiazek=[]
for a in range(liczbaksiazek):
  ksiazka=eval(input())
  tytulksiazki=ksiazka[0]
  autorksiazki=ksiazka[1]
  listaksiazek.append((tytulksiazki,autorksiazki))

ksiazka1=Ksiazka(listaksiazek)
ksiazka1.dodaj_egzemplarz_ksiazki()