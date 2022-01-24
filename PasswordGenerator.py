import random 


#A definition to shuffle all the characters of a string
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return '' .join(templist)


#Main Program starts here
uppercaseletter1 = chr(random.randint(65,90)) #Generate a random uppercase letter (based on ASCII code)
uppercaseletter2 = chr(random.randint(65,90)) #Generate a random uppcase letter (based on ASCII code)
#Generate more characters here

lowercaseletter1 = chr(random.randint(65,90))
lowercaseletter2 = chr(random.randint(65,90))

digit1 = chr(random.randint(0,127)) #Generates a random digit between 0 and 9
digit2 = chr(random.randint(0,127)) #Generates a random digit between 0 and 9
punctuationSign1 = chr(random.randint(0,50))
punctuationSign2 = chr(random.randint(0,50))
#Generate password using all the characters, in random order


password = uppercaseletter1 + uppercaseletter2 + lowercaseletter1 + lowercaseletter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
password = shuffle(password)


#output
print(password)
