allcharacter = [{"Name": "Eula", "Element": "Cryo", "Waepon Type": "Claymore", "Waepon": "Waster Greatsword", "ATK": 50},
                {"Name": "Raiden Shogun", "Element": "Electro", "Waepon Type": "Polearm", "Waepon": "Beginner's Protector", "ATK": 40},
                {"Name": "Sangonomiya Kokomi", "Element": "Hydro", "Waepon Type": "Catalyst", "Waepon": "Apprentice's Notes", "ATK": 30},
                {"Name": "Jean", "Element": "Anemo", "Waepon Type": "Sword", "Waepon": "Dull Blade", "ATK": 20},
                {"Name": "Mona", "Element": "Hydro", "Waepon Type": "Catalyst", "Waepon": "Apprentice's Notes", "ATK": 30},
                {"Name": "Kaedahara Kazuha", "Element": "Anemo", "Waepon Type": "Sword", "Waepon": "Dull Blade", "ATK": 20},
                {"Name": "Kamisato Ayaka", "Element": "Cryo", "Waepon Type": "Sword", "Waepon": "Dull Blade", "ATK": 50},
                {"Name": "Keqing", "Element": "Electro", "Waepon Type": "Sword", "Waepon": "Dull Blade", "ATK": 40}]
sword = [{"Name": "Mistsplitter Reforged", "ATK": 200},
         {"Name": "Aquila Favonia", "ATK": 200},
         {"Name": "Freedom-Sworn", "ATK": 100},
         {"Name": "Dull Blade", "ATK": 10}]
catalyst = [{"Name": "Everlasting Moonglow", "ATK": 300},
            {"Name": "Dodoco Tales", "ATK": 200},
            {"Name": "Solar Pearl", "ATK": 200},
            {"Name": "Apprentice's Notes", "ATK": 10}]
claymore = [{"Name": "Song of Broken Pines", "ATK": 300},
            {"Name": "Skyward Pride", "ATK": 200},
            {"Name": "Akuoumaru", "ATK": 100},
            {"Name": "Waster Greatsword", "ATK": 10}]
polearm = [{"Name": "Engulfing Lightning", "ATK": 300},
           {"Name": "Staff of Homa", "ATK": 250},
           {"Name": "The Catch", "ATK": 150},
           {"Name": "Beginner's Protector", "ATK": 10}]


def start():
    temp = []
    global allcharacter

    for i in range(len(allcharacter)):
        print('Id : ', i)
        print('Detail : ', allcharacter[i])
    print("---------------------------------------------------------------------------")
    print('Selamat Datang di Mini gensin Impact Game')
    print('Select 4 Character')

    return pilihHero(temp)


def pilihHero(value):
    hero = value
    try:
        if (len(hero) <= 3):
            id = int(input('Silahakan Masukan ID character yang akan anda gunakan : '))
            getName = allcharacter[id]['Name']
            print('berhasil menambahkan :', allcharacter[id]['Name'])
            if (cek(hero, getName)):
                hero.append(allcharacter[id])
                pilihHero(hero)
            else:
                print('you cant choose the same character twice')
                pilihHero(hero)
        else:
            menuGame(hero)
    except:
        print('inputan tidak benar')
        pilihHero(hero)


def cek(value, getName):
    data = value
    for i in range(len(data)):
        if (getName == data[i]['Name']):
            return False
    return True


def menuGame(value):
    data = value
    print('1. Check Party')
    print('2. Change Weapon')
    print('3. Fight boss')
    print('4. exit')

    try:
        masukan = int(input('Masukkan pilihan anda : '))
        if (masukan == 1):
            checkParty(data)
        elif (masukan == 2):
            changeWaepon(data)
        elif (masukan == 3):
            serangBos(data)
        elif (masukan == 4):
            exit(data)
    except:
        print('masukan anda tidak valid')
        menuGame(data)


def checkParty(value):
    data = value
    for i in range(len(value)):
        print(data[i]['Name'] + ' - ' + data[i]['Waepon'], 'ATK', data[i]['ATK'])
    menuGame(data)


def changeWaepon(value):
    data = value
    mapHero = list(map(subHero, data))
    subMenu(mapHero)
    try:
        id_character = int(input('Pilih ID Hero : '))
        if (data[id_character]["Waepon Type"] == "Sword"):
            mapSword = list(map(listWeapon, sword))
            subMenu(mapSword)
            waepon = int(input('masukan ID Weapon : '))
            data[id_character]['Waepon'] = sword[waepon]['Name']
            hasil = hitungDMG(sword[waepon]['ATK'], data[id_character]['Element'])
            data[id_character]['ATK'] = hasil
            mapData = list(map(subHero, data))
            subMenu(mapData)
            masukan = input('apakah anda ingin mengganti lagi ? : (y/n)')
            if (masukan == 'y'):
                changeWaepon(data)
            elif (masukan == 'n'):
                menuGame(data)

        elif (data[id_character]["Waepon Type"] == "Catalyst"):
            mapCatalist = list(map(listWeapon, catalyst))
            subMenu(mapCatalist)
            waepon = int(input('masukan ID Weapon : '))
            data[id_character]['Waepon'] = catalyst[waepon]['Name']
            data[id_character]['ATK'] = catalyst[waepon]['ATK']
            hasil = hitungDMG(catalyst[waepon]['ATK'], data[id_character]['Element'])
            data[id_character]['ATK'] = hasil
            mapData = list(map(subHero, data))
            subMenu(mapData)
            masukan = input('apakah anda ingin mengganti lagi ? : (y/n)')
            if (masukan == 'y'):
                changeWaepon(data)
            elif (masukan == 'n'):
                menuGame(data)

        elif (data[id_character]["Waepon Type"] == "Polearm"):
            mapPolearm = list(map(listWeapon, polearm))
            subMenu(mapPolearm)
            waepon = int(input('masukan ID Weapon : '))
            data[id_character]['Waepon'] = polearm[waepon]['Name']
            hasil = hitungDMG(polearm[waepon]['ATK'], data[id_character]['Element'])
            data[id_character]['ATK'] = hasil
            mapData = list(map(subHero, data))
            subMenu(mapData)
            masukan = input('apakah anda ingin mengganti lagi ? : (y/n)')
            if (masukan == 'y'):
                changeWaepon(data)
            elif (masukan == 'n'):
                menuGame(data)
            else:
                return menuGame(data)

        elif (data[id_character]["Waepon Type"] == "Claymore"):
            mapClaymore = list(map(listWeapon, claymore))
            subMenu(mapClaymore)
            waepon = int(input('masukan ID Weapon : '))
            data[id_character]['Waepon'] = claymore[waepon]['Name']
            hasil = hitungDMG(claymore[waepon]['ATK'], data[id_character]['Element'])
            data[id_character]['ATK'] = hasil
            mapData = list(map(subHero, data))
            subMenu(mapData)
            masukan = input('apakah anda ingin mengganti lagi ? : (y/n)')
            if (masukan == 'y'):
                changeWaepon(data)
            elif (masukan == 'n'):
                menuGame(data)

    except:
        print('masukan salah')
        changeWaepon(data)


def listWeapon(value):
    return value['Name'], value['ATK']

def serangBos(value):
    data = value
    print("Bos Mana yang akan anda serang ?")
    print("1. serang Tartaglia")
    print("2. serang Andrius")
    print("3. serang Rhodeia's Rage")
    print("4. serang Azdaha")
    try:
        masukan = int(input('Masukkan pilihan anda : '))
        if (masukan == 1):
            attackTartaglia(data)
        elif (masukan == 2):
            attackAndrius(data)
        elif (masukan == 3):
            attackRhoderiaRage(data)
        elif (masukan == 4):
            attackAzdhana(data)
    except:
        print('masukan anda tidak valid')
        menuGame(data)

def attackTartaglia(value):
    data = value
    Tartaglia = 10000
    print("Azdhana - HP: {}\n".format(Tartaglia))
    print("Fight Begin\n")
    while Tartaglia > 0:
        mapHero = list(map(subHero, data))
        subMenu(mapHero)
        id_hero = int(input('Pilih ID hero yang akan menyerang : '))
        print()
        Tartaglia -= data[id_hero]['ATK']
        if Tartaglia > 0:
            print('Tartaglia - HP : ', Tartaglia, '-', 'Elemental Reaction ', data[id_hero]['Element'], '\n')
        else:
            Tartaglia = 0
            print("\nTartaglia - HP: {}\n".format(Tartaglia))
            print("Challange Success\n")
            print("selamat anda berhasil mengalahkan tartaglia")
            menuGame(data)

def attackRhoderiaRage(value):
    data = value
    Rage = 10000
    print("Azdhana - HP: {}\n".format(Rage))
    print("Fight Begin\n")
    while Rage > 0:
        mapHero = list(map(subHero, data))
        subMenu(mapHero)
        id_hero = int(input('Pilih ID hero yang akan menyerang : '))
        print()
        Rage -= data[id_hero]['ATK']
        if Rage > 0:
            print('Rage - HP : ', Rage, '-', 'Elemental Reaction ', data[id_hero]['Element'], '\n')
        else:
            Rage = 0
            print("\nRage - HP: {}\n".format(Rage))
            print("Challange Success\n")
            print("selamat anda berhasil mengalahkan tartaglia")
            menuGame(data)

def attackAndrius(value):
    data = value
    Andrius = 10000
    print("Azdhana - HP: {}\n".format(Andrius))
    print("Fight Begin\n")
    while Andrius > 0:
        mapHero = list(map(subHero, data))
        subMenu(mapHero)
        id_hero = int(input('Pilih ID hero yang akan menyerang : '))
        print()
        Andrius -= data[id_hero]['ATK']
        if Andrius > 0:
            print('Andrius - HP : ', Andrius, '-', 'Elemental Reaction ', data[id_hero]['Element'], '\n')
        else:
            Andrius = 0
            print("\nAndrius - HP: {}\n".format(Andrius))
            print("Challange Success\n")
            print("selamat anda berhasil mengalahkan tartaglia")
            menuGame(data)

def attackAzdhana(value):
    data = value
    Azdhana = 10000
    print("Azdhana - HP: {}\n".format(Azdhana))
    print("Fight Begin\n")
    while Azdhana > 0:
        mapHero = list(map(subHero, data))
        subMenu(mapHero)
        id_hero = int(input('Pilih ID hero yang akan menyerang : '))
        print()
        Azdhana -= data[id_hero]['ATK']
        if Azdhana > 0:
            print('Azdhana - HP : ', Azdhana, '-', 'Elemental Reaction ', data[id_hero]['Element'],'\n')
        else:
            Azdhana = 0
            print("\nAzdhana - HP: {}\n".format(Azdhana))
            print("Challange Success\n")
            print("selamat anda berhasil mengalahkan azdaha")
            menuGame(data)

def subHero(value):
    return value['Name'], value['Waepon'], value['ATK']


def subMenu(value):
    for i in range(len(value)):
        print('id : ', i, value[i])


def hitungDMG(value, elemen):
    if (elemen == 'Cryo'):
        return value * 5
    elif (elemen == 'Electro'):
        return value * 4
    elif (elemen == 'Hydro'):
        return value * 3
    elif (elemen == 'Anemo'):
        return value * 2

def exit(value):
    data = value
    print("Game di hentikan")
    pilih = input("apakah anda ingin bermain lagi ? (y/n)")
    if (pilih == 'y'):
        return menuGame(data)
    elif(pilih == 'n'):
        return 0

start()