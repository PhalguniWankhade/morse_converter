from morse_code_dict import MORSE_CODE_DICT, INTER_CHAR_SPACE

# Convert using the dictionary
def convert_char_to_morse(c):
    return MORSE_CODE_DICT.get(c.lower())

# Get user text input.
user_text = input("Input text to be converted.")
morse_code = ""
for char in user_text:
    if char == " ":
        morse_code += "00"
    else:
        code = convert_char_to_morse(char)
        if code is not None:
            morse_code += code
            morse_code += INTER_CHAR_SPACE

# Display result
print(f"Morse code is :\n {morse_code}")