hoogte = int(input("Voer de hoogte in: "))
breedte = int(input("Voer de breedte in: "))

for rij in range(hoogte):
    regel = ""
    for kolom in range(breedte):
        regel = regel + "*"
    print(regel)