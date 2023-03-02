import GUI

# function for encryption
def encrypt():
    # get the index of each character 
    # in the message from the regular alphabet
    indexMsg = []
    for i in msg:
        indexMsg.append(alphabet.index(i))

    # translate the index of each regular character
    # to the ciphered alphabet character
    cipherArray = []
    for i in indexMsg:
        cipherArray.append(cipherAlphabet[i])

    # join the cipherArray together to form the ciphertext as a string
    cipherText = ''.join(cipherArray)

    return(cipherText)

# function for decryption
def decrypt():
    # get the index of each character
    # in the message from the cipher alphabet 
    decryptMsg = []
    for i in msg:
        decryptMsg.append(cipherAlphabet.index(i))

    # translate the index of each ciphered character
    # to the regular alphabet character
    plainArray = []
    for i in decryptMsg:
        plainArray.append(alphabet[i])

    # join the plainArray together to form the plaintext as a string
    plainText = ''.join(plainArray) 

    return(plainText)

# explain the application
print("Welcome to CipherText!")
print("The best method of converting plaintext to ciphertext and ciphertext to plaintext!")

# gather inputs
message = input("Enter a message: ")
key = int(input("Enter a key: "))
operation = input("Enter encrypt or decrypt: ")

# output
outputMessage = ""

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
    outputMessage = encrypt()

elif operation == "decrypt":
    outputMessage = decrypt()

# catch invalid operation
else:
    print("invalid operation method")

print(outputMessage)
