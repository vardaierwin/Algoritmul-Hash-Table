import random

f1 = open("Fete.txt", 'r')
f2 = open("Baieti.txt", 'r')
f3 = open("Nume.txt", 'r')
# f = open("CNP.txt", 'w') #
file = open("populatie.txt", "r")

def Generare_CNP(number: int):
    populatie = file.readlines()
    judet = 1
    nr = 0  
    fete = f1.read().split()
    baieti = f2.read().split()
    numeFamilie = f3.read().split()
    with open("CNP.txt", "w") as cnp_file:
        for iteratii in range(number):
            for i in populatie:
                aux = (number * int(i)) // 20000000
                if judet == 53:
                    break
                for item in range(aux):
                    if nr >= number:  
                        return  
                    CNP = []
                    verifica = 0
                    sex1 = random.randint(1, 100)
                    an1 = random.randint(0, 100)
                    if sex1 <= 45 and an1 > 24:
                        sex = 1
                    elif sex1 <= 45 and an1 <= 24:
                        sex = 5
                    elif sex1 > 45 and an1 > 24:
                        sex = 2
                    else:
                        sex = 6
                    if sex in [1, 2]:
                        an = random.randint(0, 99)
                    else:
                        an = random.randint(0, 24)
                    if an < 10:
                        an = f'0{an}'
                    luna = random.randint(1, 12)
                    if luna < 10:
                        luna = f'0{luna}'
                    if int(luna) in [1, 3, 5, 7, 8, 10, 12]:
                        ziua = random.randint(1, 31)
                    elif int(luna) in [4, 6, 9, 11]:
                        ziua = random.randint(1, 30)
                    else:
                        ziua = random.randint(1, 28)
                    if ziua < 10:
                        ziua = f'0{ziua}'
                    judet_str = f"{judet:02}"
                    NNN = random.randint(1, 999)
                    if NNN < 10:
                        NNN = f'00{NNN}'
                    elif NNN < 100:
                        NNN = f'0{NNN}'
                    else:
                        NNN = str(NNN)
                    cnp = f'{sex}{an}{luna}{ziua}{judet_str}{NNN}'
                    constant = "279146358279"
                    for i in range(12):
                        verifica += int(cnp[i]) * int(constant[i])
                    verifica_digit = verifica % 11
                    if verifica_digit == 10:
                        verifica_digit = '1'
                    cnp = cnp + str(verifica_digit)
                    CNP_nume = [cnp]
                    if sex % 2 == 0:
                        CNP_nume.append(random.choice(fete))
                    else:
                        CNP_nume.append(random.choice(baieti))
                    CNP_nume.append(random.choice(numeFamilie))
                    complet = " ".join(CNP_nume)
                    cnp_file.write(f"{complet}\n")
                    nr += 1  
                judet += 1


def Generare_Hash(cnp):
    cod_hash = 0
    for caracter in cnp:
        cod_hash *= 3
        cod_hash += ord(caracter)
    cod_hash %= 1000
    return cod_hash

def Hash():
    Lista = []
    with open("CNP.txt", "r") as f:

        for line in f:
            l1 = line.split()
            l1[1] += ' ' + l1[2]
            l1.pop()
            Lista.append(l1)
    final_list = [[] for i in range(1000)]
    for elm in Lista:
        cnp = elm[0]
        h = Generare_Hash(cnp)
        final_list[h].append(elm)

    return final_list

def Cautare_CNP(cnp, hash):
    h = int(Generare_Hash(cnp))
    for i in range(len(hash[h])):
        Nume = hash[h][i]
        if Nume[0] == cnp:
            print(f"CNP-ul:{cnp} se afla pe pozitia {i} din tabela de Hash : "
                  f" {h} cu numele {Nume[1]}")
            return i + 1

def Selecteaza(filename: str, num_cnp: int, hash_table: list):
    with open(filename, 'r') as f:
        all_cnps = [line.split()[0] for line in f]  
    selected_cnps = random.sample(all_cnps, num_cnp)  
    total_iterations = 0
    for cnp in selected_cnps:
        iterations = Cautare_CNP(cnp, hash_table)  
        total_iterations += iterations if iterations else 0  
    print(f"Total iterations for finding {num_cnp} CNPs: {total_iterations}")


if __name__ == '__main__':
    # Generare_CNP(1000000) #
    # f.close() #
    hash = Hash()
    # iteratie = Cautare_CNP('2451208019485', hash)
    # print(f"{iteratie} iteratii au fost necesare pentru gasirea CNP-ului")
    Selecteaza("CNP.txt", 1000, hash)  # Select and find iterations for 1000 CNPs



