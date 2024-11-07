def all_variants(text):
    for x in range(len(text)):
        for y in range(x + 1, len(text) + 1):
            yield text[x:y]


a = all_variants("abc")
for i in sorted(a, key=len):
    print(i)
