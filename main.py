# function to validate the value of the shift between 1 and 25
def shift_input():
    shift_value = int(input("Enter your shift value between 1 and 25: "))
    if 1 <= shift_value <= 25:
        return shift_value
    else:
        print("Enter a valid input.")


# function to encrypt a text
def encrypt(text, shift):
    cypher = ""
    for char in text:
        if char.islower():
            char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            cypher += char
        elif char.isupper():
            char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            cypher += char
        else:
            cypher += char
    return cypher

# input text to encrypt and value of shift
text = input("Enter your message to encrypt: ")
shift = shift_input()

# calling the encrypt function
encode_text = encrypt(text, shift)
print(encode_text)




