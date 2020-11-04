import base64
import math
import itertools as it

b64input = input("Enter b64: ")


#Return true if the b64 decoded only contains ascii from range 32 to 126
def isValidb64(b64):
    decoded = base64.b64decode(b64)
    for i in range(0,len(decoded)):
        if(decoded[i]<32 or decoded[i] > 126):
            return False    #Current letter is outside range, fail
    return True #All letters have passed and are valid


##Make sure b64 is padded to a multiple of 4 and split up into a list of 4 chunks
chunkList = []
b64length = len(b64input)

#Pad to multiple of 4 with =
b64input = b64input.ljust( (math.ceil(b64length/4))*4 ,"=")

#Create list of all 4 chunks
for i in range(0,b64length,4):
    chunkList.append(b64input[i:i+4])


#Loop through each chunks combinations checking for all valid cases
possibleB64 = []
print("\nPossible combinations:")
for chunk in chunkList:
    chunkPossibilities = []
    comboList = list(map(''.join, it.product(*zip(chunk.upper(), chunk.lower())))) #Make list of all case combos
    comboList = list(dict.fromkeys(comboList))  #Remove repeats due to non alphabetic characters
    comboList.reverse() #Reverse to check lower values first, more likely to be the proper result

    for combo in comboList: #Check all case combos for the current chunk till a valid one then add it to the result
        if(isValidb64(combo)):
            chunkPossibilities.append(base64.b64decode(combo).decode("utf-8"))
    possibleB64.append(chunkPossibilities)
    print(chunkPossibilities)

#Combine all lower guesses for the final output
finalGuess = ""
for i in range(0,len(possibleB64)):
    try:
        finalGuess += possibleB64[i][0] #If any have no values then invalid
    except IndexError:
        print("No full valid combinations")
        finalGuess = ""
        break
    
print("\nFinal guess: " + finalGuess)
