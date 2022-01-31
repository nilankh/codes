def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    frequency = [0] * 256
    for i in range(len(string1)):
        ch = ord(string1[i])
        frequency[ch] += 1

    for i in range(len(string2)):
        ch = ord(string2[i])
        frequency[ch] -= 1
    for i in range(256):
        if frequency[i] != 0:
            return False
    return True
    






string1 = input().strip()
string2 = input().strip()

ans = isPermutation(string1, string2)
if ans:
    print("true")
else:
    print("false")
















