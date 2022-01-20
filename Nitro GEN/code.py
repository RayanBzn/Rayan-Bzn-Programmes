import random
from time import sleep


nitros_number = ''
caractères = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','8','9','A','B','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print("Bienvenu dans le Rayan's NITROGENERATOR !!!")
sleep(2)
nitros_number = int(input(str("Combien de Nitros voulez vous generer ? -> : ")))
print("Chargement...")
sleep(2)
print("|                 |                 |")

for i in range(nitros_number):
    nitrocode = ''

    for i in range(16):
        nitrocode = f"{nitrocode}{random.choice(caractères)}"

    print(f"https://discord.gift/{nitrocode}")

    with open("nitros.txt", "a+") as nitroFile:

        nitroFile.write(f"https://discord.gift/{nitrocode}\n")

        nitroFile.close()
print("|                 |                 |")
print("FIN... ")
print("VOUS POUVEZ FERMER LE GENERATEUR ET RECUPERER VOS NITROS DANS LE FICHIER nitros.tkt")