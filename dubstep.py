def restore_original_song(n):
    words = n.split("WUB")
    original_song = " ".join(filter(lambda x: x != "", words))
    return original_song
n = input()
print(restore_original_song(n))
