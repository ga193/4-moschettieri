while True:
    try:
        a = input("inserire a:")
        break
    except:
        print("errore")
operatore = input("che operazione vuoi fare")
while True:
    try:
        b = input("inserire b:")
        break
    except:
        print("errore")
match operatore:
    case '*': 
        risultato = a * b
    case '+':
        risultato=a+b
    case _:
        print("errore")
print(risultato)