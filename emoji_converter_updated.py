"""Emoji Converter Updated"""
def convert_emoji(message):
    words = message.split(' ')
    emojis = {
    ":)": "🙂",
    ":(": "😔",
    ":D": "😀",
    ":|": "😐",
    "<3": "❤️",
    "xD": "😆",
    ";)": "😉"
    }


    converted_sentence = ""
    for word in words:
        converted_sentence += emojis.get(word, word) + " "
    return converted_sentence.strip()


user_input = input("> ")
result = convert_emoji(user_input)
print(result)
