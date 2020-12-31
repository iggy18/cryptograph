from english_words import english_words_set

def encrypt(phrase, shift):
    result = ""
    if shift > 26:
        shift -= 26
    for i in phrase:
        if i.isupper():
            i_index = ord(i) - ord('A')
            i_shifted = (i_index + shift) % 26 + ord('A')
            i_new = chr(i_shifted)
            result += i_new
        elif i.islower():
            i_index = ord(i) - ord('a') 
            i_shifted = (i_index + shift) % 26 + ord('a')
            i_new = chr(i_shifted)
            result += i_new
        elif i.isdigit(): 
            i_new = (int(i) + shift) % 10
            result += str(i_new)
        else:
            result += i
    return result

def decrypt(ciphertext, shift):
    decrypted = ""
    if shift > 26:
        shift -= 26
    for c in ciphertext:
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - shift) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_og_pos = (c_index - shift) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit(): 
            c_og = (int(c) - shift) % 10
            decrypted += str(c_og)
        else:
            decrypted += c
    return decrypted

def validate(word):
    return word in english_words_set

def crack(phrase):
    chop = phrase.split()
    order = sorted(chop, key=len)
    longest = order[-1]
    safety = order[-2]
    whoa_nelly = order[-3]
    compare = longest
    key = 1
    for i in range(1, 26):
        test = decrypt(compare, key)
        backup = decrypt(safety, key)
        seriously = decrypt(whoa_nelly, key)
        if validate(test) or validate(backup)or validate(seriously):
            break
        else:
            key += 1
    result = decrypt(phrase, key)
    return (result, key)



def interface():
    hello = input("\nwhat would you like to do? 'code','decode', 'crack'?\n > ").lower()

    if hello == "code":
        message = input("\ntype message you wish to code \n> ")
        key = int(input("\nenter key (number)\n> "))
        x = encrypt(message, key)
        print("your code is: ", x)
    elif hello == "decode":
        message = input("\ntype code you wish to break \n> ")
        secret_key = int(input("\nenter key (number)\n> "))
        y = decrypt(message, secret_key)
        print("your decoded message is: ", y)
    elif hello == "crack":
        message = input("\ntype code you wish to break \n> ")
        y = crack(message)
        print("your cracked message is: ", y)
    else:
        print("I don't understand. let's try that again")

def run():
    active = True
    while active:
        interface()
        x = (input("\nwould you like to go again? 'y' or 'n'?\n> "))
        if x == "n":
            active = False
    print("\nthanks for using the code makerbreakercracker 9000")

#remove comment from "run" to run command line interface
#run()