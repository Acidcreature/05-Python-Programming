"""
3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, and then use the dictionary to 
write an encrypted version of the file’s contents to a second file. Each character in
the second file should contain the code for the corresponding character in the first file.
"""

#Encrypting and Decrypting function

def crypton():
    code_dict = {
        'A' : '%',
        'a' : '9',
        'B' : '@',
        'b' : '#',
        'C' : '$',
        'c' : '0',
        'D' : '&',
        'd' : '*'
    }
    #open file
    f = open(r"uncrypt.txt",'r')
    #read that file 
    line = f.readline().strip("\n")
    #make a list from the file
    text = []
    while line != '':
        text.append(line)
        #print(text)
        line = f.readline().strip("\n")
    #print(text)
    #close file
    f.close()
    #Encrypt the original text
    out_text = []
    for e in text:
        if e in code_dict.keys():
            out_text.append(code_dict[e])
    #print(out_text)
    #open new file
    new_f = open('encrypt.txt','w+')
    #Write encrypted code to file
    for e in out_text:
        new_f.write(e)
        new_f.write('\n')
        #print(e)
    #close file
    new_f.close()

    #open encrypted file
    #open file
    encrypted_f = open("encrypt.txt",'r')
    #read that file 
    encryptedline = encrypted_f.readline()
    while encryptedline != '':
        print(encryptedline, end = '')
        encryptedline = encrypted_f.readline()
    #Close file
    encrypted_f.close()

crypton()


