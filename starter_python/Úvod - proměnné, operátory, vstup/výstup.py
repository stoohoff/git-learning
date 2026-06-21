## Napište program, který načte do dvou proměnných vstupy od uživatele. Předpokládáme, že jde o čísla.
## Do další proměnné uloží jejich součin a hodnotu této proměnné následně vypíše

a = int(input("Zadejte první číslo: ")) # někteří studenti dost možná zapomenou přetypovat
b = int(input("Zadejte druhé číslo: ")) # je důležité, aby chápali, co to dělá...

c = a * b

print(c)

# Upravte předchozí příklad tak, aby přijímal desetinná čísla

a = float(input("Zadejte první číslo: "))
b = float(input("Zadejte druhé číslo: "))

c = a * b

print(c)

## ZDE JE NAPROSTO IDEÁLNÍ PŘÍLEŽITOST DÁVAT STUDENTŮM PŘÍKLADY, VE KTERÝCH IMPLEMENTUJÍ NĚJAKÉ VZORCE, KTERÉ
## SE SOUČASNĚ UČÍ V MATICE/FYZICE/... např. odpor rezistorů (paralelně)

r1 = int(input("Odpor prvního rezistoru: "))
r2 = int(input("Odpor druhého rezistoru: "))

r = (r1*r2)/(r1+r2)

print(r)