n = 708779824646737390614738439729

# do I need to create code to find the prime factorization of n?
n = 689343651926443*1028195186342803 
phi_n = (689343651926443-1)*(1028195186342803-1)

e = 1292107475330115076780889

# private key
d = pow(e, -1, phi_n)

with open('encrypted.txt', 'r') as file:
    # read text by lines
    lines_c_text = file.readlines()
    for line in lines_c_text:
        message = pow(int(line), d, n)
        # convert the decrypted integers into their respective unicode characters
        print(chr(message), end = "")

with open("encrypted.txt", 'w') as file:
    message = "My name is Aaron Huang and my hometown is Andover, MA."
    for char in message:
        unicode = ord(char)
        c = pow(unicode, e, n)
        file.writelines(str(c) + '\n')
        





