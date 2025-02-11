putin = input().encode('latin1').decode('utf-8', errors='ignore')

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
