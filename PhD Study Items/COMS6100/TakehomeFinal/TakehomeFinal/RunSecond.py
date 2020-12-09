import numpy as np

all_inputs = []

all_inputs_File = 'all_inputs.txt'

with open(tStepFile) as Curr:

with open(all_inputs_File) as Curr:
    all_inputs = [line.rstrip('\n').split(',') for line in Curr]

userInput = input("Enter the initial angle: >> ")

indexing = int(userInput)

print("The requirements for the initial angle of " + userInput + " are:")
print("Initial velocity:  " + all_inputs[indexing][1])
print("Timestep h: " + all_inputs[indexing][3])
print("TFinal:  " + all_inputs[indexing][2])
