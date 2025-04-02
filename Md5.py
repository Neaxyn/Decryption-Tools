import hashlib

def md5Hash(string):
    md5 = hashlib.md5(string.encode())
    return md5.hexdigest()

def decrypterMd5(Hash):
    with open('rockyou.txt','r', encoding ="latin-1") as f:
           for line in f.readlines():
            password = line.strip()
            if md5Hash(password) == Hash:
                return password
                break
    return "Mot de passe pas trouvé"
    
mess = '5a74dd4eef347734c8a0a9a3188abd11'
#télécharge le gros fichier rokyou.txt sur le net
print("le mot de passe est: " + decrypterMd5(mess))