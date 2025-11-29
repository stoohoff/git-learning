## Napište program, který pro zadaný věk vypíše, zda je uživatel plnoletý
vek = int(input("Zadejte věk: "))

if vek >= 18:
  print("Jsi plnoletý")
else:
  print("Nejsi plnoletý")

## Napište program, který pro zadané celé číslo vypíše, zda je kladné, nebo záporné
cislo = int(input("Zadejte cislo: "))

if cislo > 0:
  print("Číslo je kladné")
else:
  print("Číslo je záporné")

# Pro vstup 0 program vypíše "Číslo je kladné", což není pravda.
# Opravte tento nedostatek pomocí klíčového slova ELIF
cislo = int(input("Zadejte cislo: "))

if cislo > 0:
  print("Číslo je kladné")
elif cislo == 0:
  print("Číslo je nulové")
else:
  print("Číslo je záporné")

## Napište program, který pro zadané celé číslo vypíše jeho absolutní hodnotu.
cislo = int(input("Zadejte cislo: "))

if cislo < 0:
  print(0-cislo)
else:
  print(cislo)

## Napište program, který pro dvě zadaná čísla vypíše to větší.
a = int(input("Zadejte prvni cislo: "))
b = int(input("Zadejte druhe cislo: "))

if a > b:
  print(a)
else:
  print(b)

# Upravte výstup tak, aby obsahoval informaci o zadaných hodnotách
if a > b:
  print(f"Číslo {a} je větší než číslo {b}")
else:
  print(f"Číslo {a} je menší než číslo {b}")

# Přidejte do výstupu informaci o tom, o jakou hodnotu je číslo a větší, než číslo b
if a > b:
  rozdil = a - b
  print(f"Číslo {a} je větší než číslo {b} o {rozdil}")
else:
  rozdil = b - a
  print(f"Číslo {a} je menší než číslo {b} o {rozdil}")

## Napište program, který pro dvě zadaná čísla spočítá a vypíše jejich podíl.
## Ošetřete případy, ve kterých by mohlo dojít k chybě.
a = int(input("Dělenec: "))
b = int(input("Dělitel: "))

if b == 0:
  print("Pozor! Číslem 0 nelze dělit!!!")
else:
  print(a/b)

## Napište program, který provede hod šestistěnnou kostkou a následně vypíše, které číslo padlo.
## Pokud padne číslo 6, program uživateli pogratuluje.
import random
kostka = random.randint(1,6)

if (kostka == 6):
  print(f"Číslo {kostka} Vyhrál jsi!!")
else:
  print(f"Číslo: {kostka}. Třeba příště...")

# Upravte předchozí program tam, aby házel dvěma kostkami. Vždy vypíše obě hodnoty.
# Pokud navíc na obou padne 6, opět pogratuluje.
import random
kostka1 = random.randint(1,6)
kostka2 = random.randint(1,6)

if kostka1 == 6:
  if kostka2 == 6:
    print(f"Padly hodnoty {kostka1} a {kostka2}. Gratuluji!")
  else:
    print(f"Padly hodnoty {kostka1} a {kostka2}. Třeba příště")
else:
  print(f"Padly hodnoty {kostka1} a {kostka2}. Třeba příště")

## Napište program, který vypíše jídelní menu a uživatel si bude moct vybrat, které jídlo si chce objednat.
## Program mu následně vypíše, kolik jídlo bude stát.
print("""
1. Řízek
2. Špagety
3. Hranolky
""")

vyber = int(input("Zadejte vaši volbu: "))

if vyber == 1:
  print("170,-")
elif vyber == 2:
  print("190,-")
elif vyber == 3:
  print("70,-")
else:
  print("Neplatný výběr")

## Napište program, který bude očekávat dvě čísla a znaménko základní operace (+,-,*,/).
## Poté provede výpočet a výsledek vypíše.
a = int(input("a: "))
b = int(input("b: "))
op = input("Operace: ")

if op == "+":
  print(a+b)
elif op == "-":
  print(a-b)
elif op == "*":
  print(a*b)
elif op == "/":
    print(a/b)
else:
  print("Neplatná operace.")

# Upravte předchozí program tak, aby navíc ošetřoval dělení nulou.
a = int(input("a: "))
b = int(input("b: "))
op = input("Operace: ")

if op == "+":
  print(a+b)
elif op == "-":
  print(a-b)
elif op == "*":
  print(a*b)
elif op == "/":
  if b != 0:
    print(a/b)
  else:
    print("Nulou nelze dělit.")
else:
  print("Neplatná operace.")

## Napište program, který bude mít na vstupu finanční úspory uživatele a následně mu odpoví,
## zda si může koupit byt. Pokud ano, dodatečně mu řekne, kolik by mu ještě zbylo peněz. Pokud mu to vyšlo přesně, upozorní ho, že už nic nemá. (Cenu bytu si vymyslete)
uspory = int(input("Zadejte své úspory: "))
byt = 7000000
zbytek = byt-uspory

if uspory < byt:
  print("Bohužel. Budeš ještě muset šetřit")
elif uspory > byt:
  print(f"Máš dostatek peněz! Ještě by ti zbylo {zbytek} Kč.")
else:
  print("No to je tak akorát!")

## Napište program, který bude představovat kontrolu na letišti.
## Uživatele se bude ptát, zda má platný pas, letenku a zda jeho zavazadlo splňuje podmínky.
## Pokud vše bude v pořádku, popřeje mu příjemný let, jinak ho pošle domů
pas = input("Máte platný pas? y/n: ")
if pas == "y":

  letenka = input("Máte letenku? y/n: ")
  if letenka == "y":

    zavazadlo = input("Máte zavazadlo y/n: ")
    if zavazadlo == "y":
      print("Přejeme příjemný let!")

    else:
      print("Bohužel. Nemůžete letět.")
  else:
    print("Bohužel. Nemůžete letět.")
else:
  print("Bohužel. Nemůžete letět.")