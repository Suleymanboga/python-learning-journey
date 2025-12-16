"""Emoji Converter"""
message = input("> ")
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
print(f"{converted_sentence.strip()}")
