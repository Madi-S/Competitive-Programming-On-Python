'''

In this kata you have to write a simple Morse code decoder.
While the Morse code is now mostly superseded by voice and digital data communication channels,
it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes".
For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−.
The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code,
a single space is used to separate the character codes and 3 spaces are used to separate words.
For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

'''

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
              '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def decodeMorse(morse_code):
    if morse_code in MORSE_CODE:
        return MORSE_CODE[morse_code]
    return ''.join(list(map(lambda a: MORSE_CODE[a] if a != 'space' else ' ',  morse_code.replace('   ', ' space ').split()))).strip()


print(decodeMorse('   .   . '))
