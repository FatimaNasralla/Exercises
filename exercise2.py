def count_words(text):
    dct = {}
    text=text.lower()
    words=text.split()
    for x in words:
        if x not in dct:
            dct[x] = 1
        else:
            dct[x] += 1

    return(dct)

print(count_words("AI is the future. The future is now."))



