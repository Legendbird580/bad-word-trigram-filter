putin = input()
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
