s = "abcdef"
indices = [1, 2, 5]

char_list = []
i = 0
while True:
    try:
        char_list += [s[i]]
        i += 1
    except IndexError:
        break

length = 0
for _ in char_list:
    length += 1

i = 0
while i < length:
    if i in indices:
        if 'a' <= char_list[i] <= 'z':
            char_list[i] = chr(ord(char_list[i]) - 32)
    i += 1

result = ""
j = 0
while j < length:
    result += char_list[j]
    j += 1

print(result)

