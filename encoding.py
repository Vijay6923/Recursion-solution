def decode_string(encoded):
    
    r = ''.join(sorted(set(encoded)))

    mapping = {}
    n = len(r)
    for i in range(n):
        mapping[r[i]] = r[n - 1 - i]
    
    
    decoded = ''.join(mapping[char] for char in encoded)
    return decoded


t = int(input())
for _ in range(t):
    
    encoded = input().strip()
    print(decode_string(encoded))
