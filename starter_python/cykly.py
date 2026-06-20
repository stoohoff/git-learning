## Napište program, který 3x za sebou vypíše libovolný řetězec

print("Ahoj")
print("Ahoj")
print("Ahoj")

# Nyní program upravte tak, aby využíval cyklus while

i = 3
while (i != 0):
    print("Ahoj")
    i = i - 1

# Nyní program upravte tak, aby využíval cyklus for (each.. Pozn. 1)

for i in range (3):
    print ("Ahoj")

## Pomocí cyklu for vypište přirozená čísla od 1 do 10

for i in range (1,11):
    print(i)

## Pomocí cyklu for vypište tuto posloupnost: -10, -5, 0, 5, 10, 15, 20

for i in range (-10, 25, 5):
    print(i)

## Pomocí cyklu while upravte příklad pro dělení dvou čísel tak, aby se při pokusu o dělení nulou znovu zeptal na vstup
chyba = 1

while chyba == 1:
    a = int(input("Dělenec: "))
    b = int(input("Dělitel: "))

    if b == 0:
        print("Pozor! Číslem 0 nelze dělit!!!")
        chyba = 1
    else:
        print(a/b)
        chyba = 0

## Pomocí cyklu while upravte příklad pro kontrolu na letišti tak, aby se uživatele ptal opakovaně, DOKUD nesplní všechny podmínky

splneno = 0
while splneno == 0:

    pas = input("Máte platný pas? y/n: ")
    obcanka = input("Máte platnou občanku? y/n: ")
    letenka = input("Máte letenku? y/n: ")
    zavazadlo = input("Máte zavazadlo y/n: ")

    if (pas == "y" or obcanka == "y") and letenka == "y" and zavazadlo == "y":
        print("Přejeme příjemný let!")
        splneno = 1
    else:
        print("Bohužel. Nemůžete letět.")

## Pomocí cyklu for vypište tento obrazec:
## *
## * *
## * * *
## * * * *
## * * * * *

for i in range(5):
    for j in range(0,i):
        print("*", end=" ")
    print("\n")

## Pomocí cyklu for vypište tento obrazec:
## *
## * *
## * * *
## * *
## *
for i in range(4):
    for j in range(0,i):
        print("*", end=" ")
    print("\n")

for k in range (2,0,-1):
    for l in range (0,k):
        print("*", end=" ")
    print("\n")


# Poznamky:
# 1: Ve skutečnosti se jedná o cyklus "for each", nikoliv "for". Nemá ale smysl studenty zatěžovat technikáliemi, info se dá kdyžtak doplnit na maturitním semináři apod... hlavní je myšlenka toho cyklu