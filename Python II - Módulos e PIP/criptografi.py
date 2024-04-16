import hashlib 

# 1 -verificar os algoritims diponiveis
print(hashlib.algorithms_available)


# 2 - algoritimos disponiveis de acordo com SO
print(hashlib.algorithms_guaranteed)


# 3 utilizando sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro".encode()
algorithm.update(message)
print("SHA256")
print(algorithm.hexdigest())

#utilizando MD5
message = "A melhor forma de prever o futuro".encode()

md5 = hashlib.md5()
md5.update(message)
hash1 = md5.hexdigest()

# Calcular o hash novamente
md5 = hashlib.md5()
md5.update(message)
hash2 = md5.hexdigest()

# Comparar os hashes
print(hash1 == hash2)
print(hash1)
print(hash2)

