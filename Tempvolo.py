print "Calcolare il tempo di volo conoscendo la quantita'  di carburante e il consumo orario"
Carburante = input ("Carburante: ")
Consumo = input ("Consumo Orario: ")

#calcoliamo le ore
t_ore = Carburante / Consumo
ore = int(t_ore)

#calcoliamo i minuti
t_minuti = t_ore - ore
minuti = int(t_minuti * 60)

#calcoliamo i secondi
min = t_minuti * 60
t_secondi = min - minuti
secondi = int(t_secondi * 60)

if Carburante < 0 or Consumo < 0:
        print "Errore il carburante e l'orario devono essere valori positivi"
        
print "Il tempo di volo:", ore, "ore", minuti, "minuti", secondi, "secondi"
