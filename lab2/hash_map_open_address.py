keys = ['LW293', 'AF721', 'AO434', 'NE073', 'WT433', 'TT315', 'LA599', 'WE969', 'FF595', 'CA346', 'IU407', 'HD179', 'AL439']
m = 19
hashMap = {}

def _hash(key, i):
    return (((7 * sum((ord(c) for c in key))) % 97) + i) % m

for key in keys:
    for i in range(m):
        hashedKey = _hash(key, i)
        if hashedKey not in hashMap:
            hashMap[hashedKey] = key
            break

print(hashMap)