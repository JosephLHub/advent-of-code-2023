import re, sys
encrypted_codes = sys.stdin.read().split()
for x in range(len(encrypted_codes)):
    encrypted_codes[x] = re.sub("[a-zA-Z]", "", encrypted_codes[x])
    if len(encrypted_codes[x]) == 1:
        encrypted_codes[x] = encrypted_codes[x] + encrypted_codes[x]
    elif len(encrypted_codes[x]) > 2:
        encrypted_codes[x] = encrypted_codes[x][0] + encrypted_codes[x][-1]
    encrypted_codes[x] = int(encrypted_codes[x])
print(sum(encrypted_codes))