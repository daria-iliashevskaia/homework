

def hash(word):
    hash_value = 0
    table_size = 1000
    for i in word:
        hash_value += ord(i)
        hash_value = (hash_value * ord(i)) % table_size

    return hash_value



# print(hash('appllle'))