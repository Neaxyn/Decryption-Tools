import binascii
from PIL import Image

#On ouvre le fichier en mode binaire et on lis les bits
with open('encrypted_file_simple.jpg', 'rb') as fichier :
    bits = fichier.read()

#Parcours tous les valeurs possible d'un octet
for k in range(0,256):
    #Un tableau qui va contenir le resultat xor entre
    #les élément contenu dans le fichier crypter et la valeur k
    xor = [] 
    
    for i in range(0,len(bits)): #Parcours les bits et xor chauqe élément
        xor.append(bits[i]^k)

    #On ecrit le resultat de l'opération dans un fichier     
    with open('decrypted.jpg', 'wb') as fich :
        fich.write(bytearray(xor))

    #On essaye de l'ouvrir, si sa fonctionne on arrete
    #sinon on continue notre boucle        
    try :
        find = Image.open('decrypted.jpg')
        find.show()
        break
    except Exception :
        pass
    

def getKey_hard(fichier1, fichier2):
    #on ouvre et on lit les 16 premiers octets du fichier
    cles=[]
    with open(fichier1, 'rb') as f1, open(fichier2, 'rb') as f2:
        octets1 = f1.read(16)
        octets2 = f2.read(16)
        
    #on utilise une boucle pour xor les octets correspondant et les insérer dans une liste qui sera la clé
    for i in range (16):
        cles.append(octets1[i] ^ octets2[i])
    print(cles)
    return cles


def xor_decrypt_hard(fichier, cles):
    with open(fichier, 'rb') as f:
        data = f.read()
    #On utilise bytearray pour stocker dans une liste les octets qu'on va xor avec la clé
    octetsXor = bytearray()
    indiceCle = 0 
    
    #On utilise une boucle pour stocker les octets xorés et des qu'on arrive au 17e 
    #indice de la clé , on revient à l'indice 0 de la clé
    for i in range(len(data)):
        octetsXor.append(data[i] ^ cles[indiceCle])
        indiceCle += 1
        if indiceCle == len(cles) : 
            indiceCle = 0
    #écriture de la liste d'octets dans le fichier decrypté 
    with open('decrypted_file_hard.jpg', 'wb') as f:
        f.write(octetsXor)


key = getKey_hard("encrypted_file_hard.jpg", "decrypted.jpg")
xor_decrypt_hard("encrypted_file_hard.jpg", key)
