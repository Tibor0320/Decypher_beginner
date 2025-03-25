# Alphabet list used for the Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    # Initialize the resulting cipher text
    cipher_text = ""

    # If decoding, reverse the shift amount
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Process each letter in the original text
    for letter in original_text:
        # If the letter is not in the alphabet, add it directly to the result
        if letter not in alphabet:
            cipher_text += letter
        else:
            # Calculate the new position and wrap around the alphabet if needed
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    # Print the final encoded or decoded message
    print(f'Here is the {encode_or_decode}d result: {cipher_text}')

# Flag to control the repetition of the program
repeat = True

while repeat:
    # Get user input for the direction, message, and shift amount
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Perform the Caesar cipher operation
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to continue
    restart = input('Do you want to continue? Y/N\n').upper()
    if restart == 'N':
        repeat = False
        print('Sayonara')