# Library: rappresenta la libreria online e contiene una lista di libri disponibili e una lista di ordini effettuati.
from Book import Book
from abc import ABC, abstractmethod


class Gestionelibri:
    def __init__(self):
        self.__elenco_libri = []
        self.__elenco_libri_disponibili = []
        self.__ordini = []

    def add_libro(self, input):
        self.__elenco_libri.append(input)

    def add_libri_disponibili(self, input):
        self.__ordini.append(input)

    def add_libri_disponibili(self, input):
        self.__ordini(input)

    def cerca_libri(self, targa):
        for i, libri in enumerate(self.__elenco):
            if libri.get_targa() == targa:
                print("in posizione", i+1, libri)

    def cancella_libri(self, targa):
        flag = 0
        for libri in self.__elenco:
            if libri.get_targa() == targa:
                self.__elenco.remove(libri)
                flag = 1
        if flag == 0:
            print("libri non trovato")

    def totale_libri(self) -> str:
        i = 0
        for libri in self.__elenco:
            i = i+1
        print("Totale libri", i)

    def stampa_libri(self):
        for i, ve in enumerate(self.__elenco):
            print(f"{i+1}   {ve}")

    def costo_totale(self) -> float:
        costo = 0.0
        for ve in self.__elenco:
            costo = costo + float(ve.get_costo())
        print("il costo totale delle auto e di:", costo)

    def ordina_libri(self):
        self.__elenco.sort(key=lambda immobile: immobile.get_targa())
