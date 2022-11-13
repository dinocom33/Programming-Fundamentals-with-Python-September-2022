input_message = input().split(" | ")

morse_code_dic = {'..-.': 'F', '-..-': 'X',
                  '.--.': 'P', '-': 'T', '..---': '2',
                  '....-': '4', '-----': '0', '--...': '7',
                  '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                  '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                  '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                  '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                  '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                  '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

final_message = ""

for code in input_message:
    word = ""
    for letter in code.split():
        final_message += morse_code_dic[letter]
    final_message += " "
print(final_message.upper())
