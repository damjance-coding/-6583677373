from tabels import *
 

ascii_table = ascii_table_encr()

decr_table = ascii_table_decr()

def encrypt(string):
    encrypted = ""
    for char in string:
        encrypted += f"{ascii_table[char]} "

    return encrypted

def decrypt(string):
    arr = string.split()
    decrypted = ""
    for i in arr:
        decrypted += f"{decr_table[int(i)]}"
           
    return decrypted



