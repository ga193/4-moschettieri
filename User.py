#User:il suo nome, l'indirizzo email e una lista di libri acquistati.
class User(): 
    def  __init__(self, nome, email,lista_libri):
        self.__nome = nome
        self.__email = email
        self.__lista_libri = lista_libri
    def getNome(self):
        return self.__nome
    def getEmail(self):
        return self.__email
    def getLista_libri(self):
        for libro  in self.__lista_libri: 
            print(libro)
    #metodo fatto a caso per testare
    def setLista_libri(self, lista_libri):
        self.__lista_libri = lista_libri
    #metodo  fatto a caso per aggiungere libri alla lista
    #in questo caso cambiare init (non passare lista_libri e self.__lista_libri = [])
    def aggiungiLibro(self, libro):
        self.__lista_libri.append(libro)

    def setNome(self, nome):
        self.__nome = nome
    def setEmail(self, email):
        self.__email = email
    
    def __str__(self):
        st = ""
        for i in self.__lista_libri:
            st += i + " "
        return "User: \nNome utente:" + self.__nome + "\nEmail: " + self.__email + "\nLista libri dell'utente: "  + st 


