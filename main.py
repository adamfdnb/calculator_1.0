import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

# Program make a simple calculator

print(f"Witam w programie Kalkulator 1.0")
input("# aby uruchomć wciśij dowony klawisz #")

def calc():
    for i in range(1000):
        newList = []
        z = ""

        # This function show menu

        def menu():
            print(
                f"\n::MENU::\n 1 - dodawanie\n 2 - odejmowanie\n 3 - mnożenie\n 4 - dzielenie\n"
            )

        menu()

        # This function selects the operation

        def method():
            print(
                f"Podaj rodzaj działania, posługując się odpowiednią liczbą:")
            global a
            a = int(input())
            a = a

        method()

        # This function checks the inserted variables

        def insert():
            global x
            x = input('Podaj składnik 1  :')
            global y
            y = input('Podaj składnik 2  :')

            if x.isalpha() == True or len(x) == 0:
                x = input('Sprawdź składnik 1 podaj liczbę: ')
            if y.isalpha() == True or len(y) == 0:
                y = input('Sprawdź składnik 2 podaj liczbę: ')

            x = x.replace(',', '.', 1)
            y = y.replace(',', '.', 1)

            x = float(x)
            y = float(y)

            newList.append(x)
            newList.append(y)

        insert()

         # This function add two numbers

        def add():
            for i in range(1):
                if a == 1:
                    logger.info("Dodaje %.2f i %.2f", x, y)
                    print(f'Twój wynik to: {x + y:.2f}')
                for j in range(1000):
                    if a == 1:
                        z = input(
                            '\nWstaw T jeżeli chcesz dodać kolejny składnik,\nlub N jeżeli chcesz zakończyć działanie:  '
                        )
                        if z == 't':
                            k = float(input('Podaj kolejny składnik :'))
                            newList.append(k)
                            # print(newList)
                            newList_float = map(float, newList)
                            NumbersSum = sum(newList_float)
                            print(f"Twój nowy wynik {NumbersSum:.2f}")
                        if z == 'n':
                            print(f"Twój ostateczny zbiór liczb {newList}")
                            logger.info("Koniec działania")
                            newList_float = map(float, newList)
                            NumbersSum = sum(newList_float)
                            print(f'Twój wynik końcowy to: {NumbersSum:.2f}\n')
                            break

        add()

        # This function subtracts two numbers

        def subtract(x, y):
            if a == 2:
                logger.info("Odejmuję %.2f i %.2f", x, y)
                print(f'Twój wynik to: {x - y:.2f}')

        subtract(x, y)

        # This function multiplies many numbers

        def multiply(x, y):
            global z
            for i in range(1):
                if a == 3:
                    logger.info("Mnożę %.2f i %.2f", x, y)
                    print(f'Twój wynik to: {x * y:.2f} ')
                    z = input(
                        '\nWstaw T jeżeli chcesz dodać kolejny składnik, \nlub N jeżeli chcesz zakończyć działanie:  '
                    )
            for i in range(1000):
                if a == 3:
                    if z == 't':
                        k = float(input('Podaj kolejny składnik :'))
                        newList.append(k)

                    newList_params = []
                    for i in newList:
                        newList_params.append(float(i))
                        # print(f"Twój zbiór liczb {newList_params}")

                    def multiply(*params):
                        global iloczyn
                        iloczyn = 1
                        for i in params:
                            iloczyn *= i
                        print(f"Twój nowy wynik {iloczyn:.2f}")

                    if z == 'n':
                        print(f"Twój ostateczny zbiór liczb {newList_params}")
                        logger.info("Koniec działania")
                        print(f'Twój wynik końcowy to: {iloczyn:.2f}\n')
                        break

                    multiply(*newList_params)

                    z = input(
                        '\nWstaw T jeżeli chcesz dodać kolejny składnik, \nlub N jeżeli chcesz zakończyć działanie:  '
                    )

        multiply(x, y)

        # This function divides two numbers

        def divide(x, y):
            if a == 4:
                logger.info("Dzielę %.2f i %.2f", x, y)
                print(f'Twój wynik to: {x / y:.2f}')

        divide(x, y)

        z = input("czy chcesz wykonać kolejne działanie? T / N :")

        if z == 'n':
            print("Koniec działania")
            break
        if z == 't':
            print("Kontynuuj program")


calc()