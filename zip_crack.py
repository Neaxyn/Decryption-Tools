import zipfile
import itertools


def bruteforce(path):
    with zipfile.ZipFile(path, 'r') as ziP:
        #comme le prof nous a dit que le mot de passe est court , on suppose
        #que sa taille ne dépasse pas de 6 caractères
        for tailleMdp in range(1, 6):
            
            for mdp in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=tailleMdp):
                try:
                    password = ''.join(mdp)
                    ziP.setpassword(password.encode("utf-8"))
                    ziP.extractall()
                    print(f'Le mot de passe est : {password}')
                    return password
                    break
                except:
                    continue
        print('Aucun mot de passe trouvé')
        return None