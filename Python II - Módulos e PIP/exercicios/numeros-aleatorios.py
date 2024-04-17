import random 
num = int(random.randint(1,15))

current_num=int(input("digite um numero:\n"))

while num != current_num:
  current_num = int(input("digite um numero:\n"))

print(f"parabens voce acertou  o numeor sorteado era {num}")
  