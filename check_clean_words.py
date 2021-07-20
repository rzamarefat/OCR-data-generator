import os


path = os.path.join(os.getcwd(), "cleaned_words.txt")


with open(path, "r") as f:
    all_chars = []
    content = f.readlines()

    for line in content:
        chars = list(line)
        for char in chars:
            if char == 'ﺭ':
                print(line)
            all_chars.append(char)

all_chars = set(all_chars)
print(all_chars)
print(len(all_chars))


