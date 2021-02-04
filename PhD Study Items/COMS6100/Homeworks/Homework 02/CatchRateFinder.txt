from sys import argv
import csv

script, file = argv

with open(file, newline='') as csvfile:                 ## Open file, import the data to a list
    data = list(csv.reader(csvfile))

 ## print(f"{file} has been successfully opened.\n")    ## This line is used in testing
print(f"Please enter a Pokemon Name:")
Pokemon = input(">>")                                   ## Asks the use to input a Pokemon

PokemonIDIndex = []
PokemonNameIndex = []
PokemonRateIndex = []

for row in data:
  PokemonIDIndex.append(row[0])                         ## Grabs the first column (Pokemon number)
  PokemonNameIndex.append(row[1])                       ## Grabs the second column (Pokemon name)
  PokemonRateIndex.append(row[2])                       ## Grabs the third column (Pokemon catch rate)

if Pokemon in PokemonNameIndex:
    print('Pokemon found.')
    PokemonLocation = PokemonNameIndex.index(Pokemon)   ## Gets the location of the Pokemon
    print(Pokemon ,' has a catch rate of ', PokemonRateIndex[PokemonLocation], '.')
if Pokemon not in PokemonNameIndex:
    print('Pokemon not found.')
