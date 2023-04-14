emoji_dict = {":)": "😊", ":(": "😢", ":D": "😀", ":P": "😛", ";)": "😉", "XD": "😆"}

def emoji_converter(text):
    for emoji in emoji_dict:
        text = text.replace(emoji, emoji_dict[emoji])
    return text

print(emoji_converter("I'm feeling :D today!"))
