# explain the application
print("Welcome to CipherText!")
print("The best method of converting plaintext to ciphertext and ciphertext to plaintext!")

# gather inputs
message = input("Enter a message: ")
key = int(input("Enter a key: "))
operation = input("Enter encrypt or decrypt: ")

# alphabet sequence
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"]

# special characters
specialChars = [" ", ",", "!", "@", "#","$", "%", "^", "&", "*", 
              "(", ")", "-", "_", "+", "=", "'", '"', ";", ":",
              ".", "?", "<", ">", "/", "\\", "[", "]", "{", "}"]

# form the rotation alphabet with the use of the key
afterKey = alphabet[key:]
beforeKey = alphabet[:key]

# the cipherText alphabet
cipherAlphabet = afterKey + beforeKey + specialChars

# include the special characters onto the alphabet
# special characters are not to be rotated
alphabet += specialChars

# print(alphabet)
# print(cipherAlphabet)

# empty array to take in each character of the message
msg = []

# loop through the message, append each character into the msg array
for char in message:
    msg.append(char)

# print(msg)
if operation == "encrypt":
    # get the index of each character 
    # in the message from the regular alphabet
    indexMsg = []
    for i in msg:
        indexMsg.append(alphabet.index(i))

    # print(indexMsg)

    # translate the index of each regular character
    # to the ciphered alphabet character
    cipherArray = []
    for i in indexMsg:
        cipherArray.append(cipherAlphabet[i])

    # print(cipherArray)

    # join the cipherArray together to form the ciphertext as a string
    cipherText = ''.join(cipherArray)
    print(cipherText)

elif operation == "decrypt":
    # get the index of each character
    # in the message from the cipher alphabet 
    decryptMsg = []
    for i in msg:
        decryptMsg.append(cipherAlphabet.index(i))

    # print(decryptMsg)

    # translate the index of each ciphered character
    # to the regular alphabet character
    plainArray = []
    for i in decryptMsg:
        plainArray.append(alphabet[i])

    plainText = ''.join(plainArray) 
    print(plainText)

else:
    print("invalid operation method")

