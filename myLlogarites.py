def add(numer1, numer2):
    return numer1 + numer2

def subtract(numer1, numer2):
    return numer1 - numer2

def multiply(numer1, numer2):
    return numer1 * numer2

def divide(numer1, numer2):
    return numer1 / numer2

print("Operimet që mund të zgjidhni janë:\n" \
    "1. Mbledhje\n" \
    "2. Zbritje\n" \
    "3. Shumëzim\n" \
    "4. Pjestim\n")

# Merr input nga përdoruesi
select = input("Zgjidh një nga operimet:")

numer_1 = int(input("Fusni numrin e parë: "))
numer_2 = int(input("Fusni numrin e dytë: "))

if select == '1':
    print(numer_1, "+", numer_2, "=",
    add(numer_1, numer_2))

elif select == '2':
    print(numer_1, "-", numer_2, "=",
    subtract(numer_1, numer_2))


elif select == '3':
    print(numer_1, "*", numer_2, "=",
    multiply(numer_1, numer_2))


elif select == '4':
    print(numer_1, "/", numer_2, "=",
    divide(numer_1, numer_2))
else:
    print("Çfarë keni futur nuk është e saktë")




