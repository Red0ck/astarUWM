import math

def algorytm(start, cel, mapa):
    #definicja klasy ktora posiada pozycje kratki, rodzica oraz f,g,h
    class Obiekt():
        def __init__(self, pozycja=None, rodzic=None):
            self.pozycja = pozycja
            self.rodzic = rodzic
            self.f = 0
            self.g = 0
            self.h = 0

        def __eq__(self, inna):
            return self.pozycja == inna.pozycja

    #tablice do potencjalnych sciezek, sciezki koncowej, sciezki do wypisania, sasiednich kratek pol
    listaPotencjalnychSciezek = []
    listaZeSciezka = []
    sciezkaDoWypisania = []
    sasiednieKratki = []

    #przypisanie aktualnego obiektu z parametru funkcji algorytm (start), oraz koncowego obiektu (cel)
    aktualnyObiekt = Obiekt(start, None)
    koncowyObiekt = Obiekt(cel, None)
    #dodanie poczatkowego obiektu do tablicy potencjalnych sciezek jako pierwszej kratki
    listaPotencjalnychSciezek.append(aktualnyObiekt)

    #dopki lista potencjalnych sciezek nie jest rowna 0, petla sie wykonuje i poszukuje nastepnych kratek w poszukiwaniu drogi do celu ze startu
    while (len(listaPotencjalnychSciezek) > 0):
        sasiednieKratki.clear()
        aktualnyObiekt = listaPotencjalnychSciezek[0]

        #z listy potencjalnych sciezek szuka kratki o najmniejszym f
        for tmpNode in listaPotencjalnychSciezek:
            if (tmpNode.f < aktualnyObiekt.f):
                aktualnyObiekt = tmpNode

        #dodanie kratki do tablicy ze sciezka koncowa
        listaZeSciezka.append(aktualnyObiekt)
        #usuniecie kratki ktora zostala dodana do tablicy z sciezka koncowa
        listaPotencjalnychSciezek.remove(aktualnyObiekt)

        #jezeli kratka na ktorej aktualnie sie znajduje algorytm jest rowniez celem
        #dodaje pozycje aktualnej kratki do tablicy sciezka do wypisania
        if (aktualnyObiekt == koncowyObiekt):
            tymczasowyAktualnyObiekt = aktualnyObiekt

            while (tymczasowyAktualnyObiekt is not None):
                sciezkaDoWypisania.append(tymczasowyAktualnyObiekt.pozycja)
                #na mapie wypisuje 9 jako sciezke
                mapa[tymczasowyAktualnyObiekt.pozycja[0]][tymczasowyAktualnyObiekt.pozycja[1]] = 9
                tymczasowyAktualnyObiekt = tymczasowyAktualnyObiekt.rodzic
            #wstawia 9 jako punkt startowy
            mapa[start[0]][start[1]] = 9
            return sciezkaDoWypisania[::-1]

        pozycjeSasiednichKratek = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        #petla sprawdza czy kazda z sasiednich kratek nie wychodzi poza mape lub nie jet sciana
        for pozycjaSasiedniejKratki in pozycjeSasiednichKratek:
            pozycjaAktualnegoObiektuX = aktualnyObiekt.pozycja[0] + pozycjaSasiedniejKratki[0]
            pozycjaAktualnegoObiektuY = aktualnyObiekt.pozycja[1] + pozycjaSasiedniejKratki[1]

            if ((pozycjaAktualnegoObiektuX < 0) or (pozycjaAktualnegoObiektuX > len(mapa) - 1)):
                continue
            if ((pozycjaAktualnegoObiektuY < 0) or (pozycjaAktualnegoObiektuY > len(mapa[0]) - 1)):
                continue

            if (mapa[pozycjaAktualnegoObiektuX][pozycjaAktualnegoObiektuY] != 0):
                continue

            #jesli powyzsze warunki nie sa spelnione to dodaje obiekt do sasiednich kratek
            nowyObiekt = Obiekt((pozycjaAktualnegoObiektuX, pozycjaAktualnegoObiektuY), aktualnyObiekt)
            sasiednieKratki.append(nowyObiekt)

        #liczy h,g,f sasiednich kratek, jezeli nie zostaly one juz obliczne, badz nie sa juz w sciezce
        for sasiedniaKratka in sasiednieKratki:
            for obiektZeSciezki in listaZeSciezka:
                if (obiektZeSciezki == sasiedniaKratka):
                    continue
            sasiedniaKratka.h = ((sasiedniaKratka.pozycja[0] - koncowyObiekt.pozycja[0]) ** 2) + (
                        (sasiedniaKratka.pozycja[1] - koncowyObiekt.pozycja[1]) ** 2) #obliczanie heurestyki
            sasiedniaKratka.g = aktualnyObiekt.g + 1 #krok, ilosc krokow na koncu
            sasiedniaKratka.f = sasiedniaKratka.g + sasiedniaKratka.h #wartosc funkcji drogi

            #szuka najwiekszego g i dodaje do tablicy potencjalnych sciezek
            for obiektPotencjalny in listaPotencjalnychSciezek:
                if ((obiektPotencjalny == sasiedniaKratka) and (obiektPotencjalny.g < sasiedniaKratka.g)):
                    continue
            listaPotencjalnychSciezek.append(sasiedniaKratka)


mapa = [[0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [5 ,5 ,5 ,5 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,5 ,5],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,5 ,5],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [5 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,5 ,0 ,0 ,0 ,0]]


#wypisanie mapy czystej, przed przejsciem
for wiersz in mapa:
    for kolumna in wiersz:
        print(kolumna, end='  ')
    print()

sciezkaDoCelu = algorytm((0, 0), (19, 16), mapa)
print('================================================================')
#wypisanie mapy ze sciezka
for wiersz in mapa:
    for kolumna in wiersz:
        print(kolumna, end='  ')
    print()

print(sciezkaDoCelu)