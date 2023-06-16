from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime


class ListaZakupow:
  

    def __init__(self) -> None:
        self._produkty = []

    def dodaj_produkt(self, produkt: str) -> None:
       
        self._produkty.append(produkt)

    def usun_produkt(self, produkt: str) -> None:
       
        if produkt in self._produkty:
            self._produkty.remove(produkt)

    def wyswietl_liste(self) -> None:
       
        print("Lista zakupów:")
        for produkt in self._produkty:
            print(produkt)
        print()

    def utworz_memento(self) -> ListaZakupowMemento:
        
        return ListaZakupowMemento(self._produkty.copy())

    def przywroc(self, memento: ListaZakupowMemento) -> None:
       
        self._produkty = memento.pobierz_stan().copy()


class ListaZakupowMemento:
   

    def __init__(self, produkty: list[str]) -> None:
        self._produkty = produkty
        self._data = str(datetime.now())[:19]

    def pobierz_stan(self) -> list[str]:
        
        return self._produkty

    def pobierz_date(self) -> str:
       
        return self._data


class HistoriaListyZakupow:
  

    def __init__(self, lista_zakupow: ListaZakupow) -> None:
        self._historia = []
        self._lista_zakupow = lista_zakupow

    def zapisz_stan(self) -> None:
      
        memento = self._lista_zakupow.utworz_memento()
        self._historia.append(memento)

    def cofnij(self) -> None:
       
        if len(self._historia) > 1:
            self._historia.pop()
            memento = self._historia[-1]
            self._lista_zakupow.przywroc(memento)
        elif len(self._historia) == 1:
            self._historia.pop()
            self._lista_zakupow.przywroc(ListaZakupowMemento([]))

    def wyswietl_historie(self) -> None:
        
        
        print("Historia listy zakupów:")
        for memento in self._historia:
            data = memento.pobierz_date()
            stan = memento.pobierz_stan()
            print(f"{data}: {stan}")
        print()


if __name__ == "__main__":
    lista_zakupow = ListaZakupow()
    historia = HistoriaListyZakupow(lista_zakupow)

    lista_zakupow.dodaj_produkt("Mleko")
    lista_zakupow.dodaj_produkt("Jajka")
    lista_zakupow.dodaj_produkt("Chleb")
    lista_zakupow.wyswietl_liste()

    historia.zapisz_stan()

    lista_zakupow.dodaj_produkt("Masło")
    lista_zakupow.usun_produkt("Mleko")
    lista_zakupow.wyswietl_liste()

    historia.zapisz_stan()

    lista_zakupow.dodaj_produkt("Ser")
    lista_zakupow.wyswietl_liste()
    historia.zapisz_stan()

    historia.wyswietl_historie()

    print("Cofanie ostatniej zmiany...")
    historia.cofnij()

    lista_zakupow.wyswietl_liste()

    print("Cofanie ponownie...")
    historia.cofnij()

    lista_zakupow.wyswietl_liste()
