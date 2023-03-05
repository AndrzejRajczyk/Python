#h = int(input("Czas startu (godziny): "))
#m = int(input("Czas startu (minuty): "))
#d = int(input("Czas trwania wydarzenia (minuty): "))
h=12
m=17
d=59
# wprowadź tutaj swój kod - o której godzinie zakończy się wydarzenie

hEnd=round((m+d)/60)    #hEnd  -ustalanie godziny zakończenia - ile ogdzin dodajemy
hEnd=h+hEnd
hEnd=hEnd%24 - 1
m=(m+d) % 60


print("Czas końcowy: Godzina ",hEnd , end="")
print(" Minut ", m)