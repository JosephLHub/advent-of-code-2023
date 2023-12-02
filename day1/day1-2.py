import re, sys
digits = ["one","two","three","four","five","six","seven","eight","nine"]
encrypted_codes = sys.stdin.read().split()
for x in range(len(encrypted_codes)):
    for num in digits:
        if encrypted_codes[x].find(num) != -1:
            encrypted_codes[x] = encrypted_codes[x].replace(num, (num[0] + str(digits.index(num) + 1) + num[-1]))
    encrypted_codes[x] = re.sub("[a-zA-Z]", "", encrypted_codes[x])
    if len(encrypted_codes[x]) == 1:
        encrypted_codes[x] = encrypted_codes[x] + encrypted_codes[x]
    elif len(encrypted_codes[x]) > 2:
        encrypted_codes[x] = encrypted_codes[x][0] + encrypted_codes[x][-1]
    encrypted_codes[x] = int(encrypted_codes[x])
print(sum(encrypted_codes))