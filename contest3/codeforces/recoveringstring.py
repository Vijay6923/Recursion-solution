def smallestword(encoded_sum):
    for i in range(1, 27):
        for j in range(1, 27):
            for k in range(1, 27):
                    if i + j + k  == encoded_sum:
                        return chr(i + 96) + chr(j + 96) + chr(k + 96) 

t = int(input())
for _ in range(t):
    encodedsum = int(input())
    word = smallestword(encodedsum)
    print(word)
