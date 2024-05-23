def process_string(s: str) -> str:
    vowels = set("aoyeuiAOYEUI")
    result = []
    for char in s:
        if char not in vowels:
            
            result.append('.' + char.lower())
    return ''.join(result)

s=input()
print(process_string(s))