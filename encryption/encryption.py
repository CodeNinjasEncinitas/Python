cypher = {
    "a": "4",
    "b": "8",
    "c": "₵",
    "d": "𝖉",
    "e": "3",
    "f": "ꟻ",
    "g": "₲",
    "h": "Ⓗ ",
    "i": "1",
    "j": "𝔍 ",
    "k": "𝕂 ",
    "l": "7",
    "m": "ℳ ",
    "n": "𝓝 ",
    "o": "0",
    "p": "q",
    "q": "𝕢 ",
    "r": "ℜ ",
    "s": "5",
    "t": "𝙏",
    "u": "v",
    "v": "\/",
    "w": "𝒲 ",
    "x": "𝖃 ",
    "y": "𝓨 ",
    "z": "𝓩",
    " ": " ",
    "!": "iii",
    ",": "_",
    ".": "-",
    "'": ";",
    "-": "="
}

while True:
    text = input("Enter text: ").lower()

    new_text = ""

    for letter in text:
        char = cypher[letter]
        new_text += char

    print(new_text)