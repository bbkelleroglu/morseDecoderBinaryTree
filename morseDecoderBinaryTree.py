

letters = "-ETIANMSURWDKGOHVF*L*PJBXCYZQ**54*3***2**+****16=/*****7***8*90"

def check(index):
    
    if(index > len(morse)):
        print("Invalid Morse Code at the "+str(index)+"'th position of the code array")
        exit()

def morseToString(morse):
    index = 1
    message = ""
    for i in range(len(morse)):

        if i <len(morse)-1:
            if morse[i] == " ":
                message += letters[index-1]
                index = 1
            elif morse[i] == "." :
                index = 2*index
                check(index)
            elif morse[i] == "-":
                index = 2*index + 1
                check(index)
        else:
            if morse[i] == "." :
                index = 2*index
                check(index)
            elif morse[i] == "-":
                index = 2*index + 1
                check(index)
            message += letters[index-1]
            index = 1
    return message.replace("*"," ")

morse = ".-- .. - .... .-.- -- -.-- .-.- -... . ... - .-.- .-- .. ... .... . ..."

decoded = morseToString(morse)
print(decoded)        
        