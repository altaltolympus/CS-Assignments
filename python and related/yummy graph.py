import matplotlib.pyplot as plot
folks = ["James Smith", "Charles Johnson", "John Williams", "Olivia Brown", "Ava Jones", "Charlotte Garcia", "Emma Miller", "Isabella Davis", "Joseph Rodriguez", "Mia Martinez", 
         "Sophia Hernandez", "Thomas Lopez", "Amelia Gonzalez", "Clarence Wilson", "David Anderson", "Edward Thomas", "Ellie Taylor", "Evelyn Moore", "George Jackson", "Luna Martin"]
import random
siblings = []
for x in range (len(folks)):
    siblings.append(random.randint(0,12))
plot.pie(siblings, labels=folks)
plot.title("folks and associates")
plot.show()