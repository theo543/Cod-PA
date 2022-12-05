# funcție care furnizează cheia necesară sortării 
# proiectelor descrescător după profit 
def cheieProfit(p): 
    return p[2] 
 
 
# citim datele de intare din fișierul text "proiecte.in" 
fin = open("proiecte.in") 
 
# lp = lista proiectelor în care un proiect este memorat 
# sub forma unui tuplu (denumire, termen limită, profit) 
lp = [] 
for linie in fin: 
    aux = linie.split() 
    lp.append((aux[0], int(aux[1]), float(aux[2]))) 
 
fin.close() 
 
# sortăm proiectele descrescător după profit 
lp.sort(key=cheieProfit, reverse=True) 
 
# calculăm numărul maxim de zile în care putem 
# să planificăm proiectele 
zi_max = max([p[1] for p in lp]) 
 
# planificarea optimă va fi construită folosind un dicționar 
# cu intrări de forma zi: proiect 
planificare = {k: None for k in range(1, zi_max+1)} 
 
# profit = profitul total al echipei 
profit = 0 

# parcurgem lista proiectelor și încercăm să planificăm 
# fiecare proiect într-o zi cât mai apropiată de termenul său limită 
for proiect in lp: 
    for z in range(proiect[1], 0, -1): 
        if planificare[z] is None: 
            planificare[z] = proiect 
            profit += proiect[2] 
            break 
 
# scriem soluția în fișierul text "proiecte.out" 
fout = open("proiecte.out", "w") 

compact = 0 # !!!

for z in planificare: 
    if planificare[z] != None: 
        fout.write("Ziua " + str(z - compact) + ": " + planificare[z][0] +  # !!!
       " " + str(planificare[z][2]) + "\n") 
    else: compact += 1 # !!!
fout.write("\nProfit maxim: " + str(profit)) 
         
fout.close()