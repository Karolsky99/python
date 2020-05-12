n = int(input("Liczba bialych kul: "))
m = int(input("Liczba czarnych kul: "))
k = int(input("Liczba losowanych kul: "))
pwhite = 1
pblack = 1
whiteleft = n # aktualna liczba kul bialych
blackleft = m # aktualna liczba kul czarnych

for i in range(k):
    # 2 linie obliczaja prawdopodobienstwo losowania kolejno wylacznie bialych kul
    pwhite = pwhite * (whiteleft/(whiteleft+m))
    whiteleft -= 1
    # prawdopodobienstwo losowania kolejno wylacznie czarnych kul
    pblack = pblack * (blackleft / (n + blackleft))
    blackleft -= 1

psame = pwhite + pblack
print("Prawdopodobienstwo wylosowania jednakowych kul wynosi: ", psame)
