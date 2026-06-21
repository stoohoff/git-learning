## Upravte program pro kontrolu na letišti tak, aby využíval logické operátory
pas = input("Máte platný pas? y/n: ")
letenka = input("Máte letenku? y/n: ")
zavazadlo = input("Máte zavazadlo y/n: ")

if pas == "y" and letenka == "y" and zavazadlo == "y":
    print("Přejeme příjemný let!")
else:
  print("Bohužel. Nemůžete letět.")

# Do předchozího programu přidejte možnost prokázat se pasem NEBO občankou
pas = input("Máte platný pas? y/n: ")
obcanka = input("Máte platnou občanku? y/n: ")
letenka = input("Máte letenku? y/n: ")
zavazadlo = input("Máte zavazadlo y/n: ")

if (pas == "y" or obcanka == "y") and letenka == "y" and zavazadlo == "y":
    print("Přejeme příjemný let!")
else:
  print("Bohužel. Nemůžete letět.")

## Upravte program házení dvěma kostkami tak, aby využíval logické operátory
import random
kostka1 = random.randint(1,6)
kostka2 = random.randint(1,6)

if kostka1 == 6 and kostka2 == 6:
    print(f"Padly hodnoty {kostka1} a {kostka2}. Gratuluji!")
else:
  print(f"Padly hodnoty {kostka1} a {kostka2}. Třeba příště")

# Rozšiřte předchozí program tak, aby využíval hod třemi kostkami
kostka1 = random.randint(1,6)
kostka2 = random.randint(1,6)
kostka3 = random.randint(1,6)

if kostka1 == 6 and kostka2 == 6 and kostka3 == 6:
    print(f"Padly hodnoty {kostka1}, {kostka2} a {kostka3}. Gratuluji!")
else:
  print(f"Padly hodnoty {kostka1}, {kostka2} a {kostka3}. Třeba příště")

## (PRO TY NEJPOKROČILEJŠÍ)
## Přepište následující kód tak, aby používal logické operátory namísto IF...ELSE

def printt (x):
    print(x)
    return True

# if 5 < 6:
#     print("Toto se vytiskne")
# else:
#     print("Toto se nevytiskne")

(5 < 6 and print("Toto se vytiskne")) or ("Toto se nevytiskne")

##