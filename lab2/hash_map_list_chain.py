keys = [28, 90, 33, 58, 88, 68, 92, 10, 45, 17, 43, 94, 84, 76, 85, 31, 42, 64, 4, 81, 69, 97, 52]
m = 7
hashMap = {}

def _hash(key):
    return key % m

for key in keys:
    hashedKey = _hash(key)
    if hashedKey not in hashMap:
        hashMap[hashedKey] = [key]
    else:
        hashMap[hashedKey].append(key)

print(hashMap)