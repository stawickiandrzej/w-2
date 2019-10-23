choice = 't'

print("Witaj w programie do odwracania stringów")

while choice == 't':

    zdanie = input("Podaj zdanie które chcesz odwrócić")

    for i in range(1, len(zdanie)+1):
        print(zdanie[-i])

    print(zdanie[::-1])

    choice = input("Czy chcesz podać odwrócić inne zdanie? (t/n)")
