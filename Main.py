risultato = "errore"

while True:
    while True:
        try:
            a = float(input("inserire a:"))
            break
        except:
            print("errore")
    while True:
        try:
            b = float(input("inserire b:"))
            break
        except:
            print("errore")
    
    operatore = input("che operazione vuoi fare")
    match operatore:
        case '*': 
            risultato = a * b
        case '-': 
            risultato = a - b
        case '+':
            risultato=a+b
        case '/': 
            try:
                risultato = a / b
            except:
                print("errore inserisci un divisore maggiore di 0")
        case _:
            print("errore\nPerfavore inserisci esclusivamente '+' '-' '*' o '/' ")
    print(risultato)