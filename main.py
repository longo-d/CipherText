print("Welcome to CipherText!")
print("The best method of converting plaintext to ciphertext and ciphertext to plaintext!")

message = input("Enter a message: ")
key = int(input("Enter a key: "))
operation = input("Enter encrypt or decrypt: ")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"]

afterKey = alphabet[key:]
beforeKey = alphabet[:key]

cipherAlphabet = afterKey + beforeKey

print(alphabet)
print(cipherAlphabet)

msg = []

for char in message:
    msg.append(char)

print(msg)

indexMsg = []
for i in msg:
    indexMsg.append(alphabet.index(i))

print(indexMsg)

cipherArray = []
for i in indexMsg:
    cipherArray.append(cipherAlphabet[i])

print(cipherArray)
cipherText = ''.join(cipherArray)
print(cipherText)