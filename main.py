try:
    putin = input()
except UnicodeDecodeError as e:
    print(f"Error: {e}")
    print(f"Input: {sys.stdin.encoding}")
    print(f"Locale: {locale.getdefaultlocale()}")

trigrams = ("tes", "123")
greylist = []
whitelist = []

for word in putin.split():
    for item in trigrams:
        if item in word:
            greylist.append(word)
            break
    else:
        whitelist.append(word)

print(greylist, whitelist)
