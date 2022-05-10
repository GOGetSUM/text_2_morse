
def txt2mrse(text):
    # Dict created for alpha conversion, found online
    CODE_reversed = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
        '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
        '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
        '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '   ': 'SPACE'
    }
    # need to reverse dictionary code found online.
    inv_morse = {v: k for k, v in CODE_reversed.items()} #this can be used to reverse any dict. key/value

    # Creating List out of Phrase, ea char. "   " = SPACE
    string_list = []
    for let in phrase:
        if let == ' ':
            let = 'SPACE'
            string_list.append(let)
        else:
            string_list.append(let)
    # convert and return output message
    new_msg = []
    for i in string_list:
        a = inv_morse[i]
        new_msg.append(a)
    return print(*new_msg)


#------Input-------
phrase = input('Please enter the phrase you would like to convert: \n').upper()

#------Conversion Function------
txt2mrse(phrase)
