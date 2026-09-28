hoogte = int(input("Voer de hoogte in: "))

for rij in range(1, hoogte+1):
    regel = ""
    for i in range(rij):
      regel = regel + "*"
    print(regel)

    
