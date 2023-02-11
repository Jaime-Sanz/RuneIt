def runes(champion, number):
    champs = {
        'Annie': annie(number),
        'Olaf': olaf(number),
        'Galio': galio(number),
        'Twisted Fate': tf(number),
        'Xin Zhao': xz(number),
        'Urgot': urgot(number),
        'LeBlanc': lb(number),
        'Vladimir': vlad(number),
        'Fiddlesticks': fid(number),
        'Kayle': kayle(number),
        'Master Yi': yi(number),
        'Alistar': ali(number),
        'Ryze': ryze(number),
        'Sion': sion(number),
        'Sivir': sivir(number),
        'Soraka': soraka(number),
        'Teemo': teemo(number),
        'Tristana': trist(number),
        'Warwick': ww(number),
        'Nunu & Willump': nunu(number),
        'Miss Fortune': mf(number),
        'Ashe': ashe(number),
        'Tryndamere': trynd(number),
        'Jax': jax(number),
        'Morgana': morg(number),
        'Zilean': zil(number),
        'Singed': singed(number),
        'Evelynn': eve(number),
        'Twitch': twitch(number),
        'Karthus': karthus(number),
        "Cho'Gath": cho(number),
        'Amumu': amumu(number),
        'Rammus': rammus(number),
        'Anivia': anivia(number),
        'Shaco': shaco(number),
        'Dr.Mundo': mundo(number),
        'Sona': sona(number),
        'Kassadin': kass(number),
        'Irelia': irelia(number),
        'Janna': janna(number),
        'Gangplank': gp(number),
        'Corki': corki(number),
        'Karma': karma(number),
        'Taric': taric(number),
        'Veigar': veigar(number),
        'Trundle': trundle(number),
        'Swain': swain(number),
        'Caitlyn': cait(number),
        'Blitzcrank': blitz(number),
        'Malphite': mal(number),
        'Katarina': kat(number),
        'Nocturne': noc(number),
        'Maokai': mao(number),
        'Renekton': renek(number),
        'JarvanIV': jfour(number),
        'Elise': elise(number),
        'Orianna': ori(number),
        'Wukong': wu(number),
        'Brand': brand(number),
        'LeeSin': lee(number),
        'Vayne': vayne(number),
        'Rumble': rumble(number),
        'Cassiopeia': cass(number),
        'Skarner': skarner(number),
        'Heimerdinger': heim(number),
        'Nasus': nasus(number),
        'Nidalee': nid(number),
        'Udyr': udyr(number),
        'Poppy': poppy(number),
        'Gragas': gragas(number),
        'Pantheon': panth(number),
        'Ezreal': ez(number),
        'Mordekaiser': mord(number),
        'Yorick': yorick(number),
        'Akali': akali(number),
        'Kennen': kennen(number),
        'Garen': garen(number),
        'Leona': leo(number),
        'Malzahar': malz(number),
        'Talon': talon(number),
        'Riven': riven(number),
        "Kog'Maw": kog(number),
        'Shen': shen(number),
        'Lux': lux(number),
        'Xerath': xerath(number),
        'Shyvana': shy(number),
        'Ahri': ahri(number),
        'Graves': graves(number),
        'Fizz': fizz(number),
        'Volibear': voli(number),
        'Rengar': rengar(number),
        'Varus': varus(number),
        'Nautilus': naut(number),
        'Viktor': viktor(number),
        'Sejuani': sej(number),
        'Fiora': fio(number),
        'Ziggs': ziggs(number),
        'Lulu': lulu(number),
        'Draven': draven(number),
        'Hecarim': hec(number),
        "Kha'Zix": kha(number),
        'Darius': dar(number),
        'Jayce': jayce(number),
        'Lissandra': liss(number),
        'Diana': diana(number),
        'Quinn': quinn(number),
        'Syndra': syndra(number),
        'AurelionSol': asol(number),
        'Kayn': kayn(number),
        'Zoe': zoe(number),
        'Zyra': zyra(number),
        "Kai'sa": kaisa(number),
        "Seraphine": seraph(number),
        'Gnar': gnar(number),
        'Zac': zac(number),
        'Yasuo': yas(number),
        "Vel'Koz": vel(number),
        'Taliyah': tali(number),
        "Akshan": akshan(number),
        'Camille': cam(number),
        "Belveth": bel(number),
        'Braum': braum(number),
        'Jhin': jhin(number),
        'Kindred': kindred(number),
        'Zeri': zeri(number),
        'Jinx': jinx(number),
        'TahmKench': tahm(number),
        'Viego': viego(number),
        'Senna': senna(number),
        'Lucian': lucian(number),
        'Zed': zed(number),
        'Kled': kled(number),
        'Ekko': ekko(number),
        'Qiyana': qiyana(number),
        'Vi': vi(number),
        'Aatrox': aatrox(number),
        'Nami': nami(number),
        'Azir': azir(number),
        'Yuumi': yuumi(number),
        'Samira': samira(number),
        'Thresh': thresh(number),
        'Illaoi': illoai(number),
        "Rek'Sai": rek(number),
        'Ivern': ivern(number),
        'Kalista': kalista(number),
        'Bard': bard(number),
        'Rakan': rakan(number),
        'Xayah': xayah(number),
        'Ornn': ornn(number),
        'Sylas': sylas(number),
        'Rell': rell(number),
        'Neeko': neeko(number),
        'Aphelios': aphelios(number),
        'Pyke': pyke(number),
        "Sett": sett(number),
        "Vex": vex(number),
        "Yone": yone(number),
        "Gwen": gwen(number),
        "Lillia": lillia(number),
        "Renata": renata(number),
        "Nilah": nil(number),
        "KSante": ks(number)
    }
    return champs.get(champion)


def annie(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8112', '8126', '8138', '8135', '8100', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def olaf(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9104', '8299', '8000', '8345', '8410', '8300']
    thisRune = runes[number]
    return int(thisRune)


def galio(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8439', '8401', '8444', '8242', '8400', '8275', '8234', '8200']
    thisRune = runes[number]
    return int(thisRune)


def tf(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8124', '8126', '8138', '8106', '8100', '8316', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def xz(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9104', '8299', '8000', '8106', '8138', '8100']
    thisRune = runes[number]
    return int(thisRune)


def urgot(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8005', '9111', '9105', '8299', '8000', '8444', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def lb(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8112', '8143', '8138', '8106', '8100', '8226', '8237', '8200']
    thisRune = runes[number]
    return int(thisRune)


def vlad(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '8009', '9103', '8014', '8000', '8139', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def fid(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8369', '8313', '8321', '8347', '8300', '8126', '8106', '8100']
    thisRune = runes[number]
    return int(thisRune)


def kayle(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8008', '9111', '9104', '8014', '8000', '8236', '8233', '8200']
    thisRune = runes[number]
    return int(thisRune)


def yi(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8008', '9111', '9104', '8299', '8000', '8138', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def ali(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8214', '8226', '8210', '8237', '8200', '8453', '8473', '8400']
    thisRune = runes[number]
    return int(thisRune)


def ryze(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8230', '8226', '8210', '8236', '8200', '8451', '8473', '8400']
    thisRune = runes[number]
    return int(thisRune)


def sion(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8437', '8446', '8473', '8451', '8400', '8410', '8316', '8300']
    thisRune = runes[number]
    return int(thisRune)


def sivir(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8369', '8304', '8345', '8347', '8300', '8444', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def soraka(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8214', '8226', '8210', '8237', '8200', '8453', '8473', '8400']
    thisRune = runes[number]
    return int(thisRune)


def teemo(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8128', '8126', '8138', '8106', '8100', '8009', '8014', '8000']
    thisRune = runes[number]
    return int(thisRune)


def trist(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '9923', '8139', '8138', '8135', '8100', '8473', '8446', '8400']
    thisRune = runes[number]
    return int(thisRune)


def ww(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8005', '9111', '9104', '8299', '8000', '8138', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def nunu(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5007', '8230', '8224', '8210', '8232', '8200', '8473', '8453', '8400']
    thisRune = runes[number]
    return int(thisRune)


def mf(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8010', '8009', '9105', '8299', '8000', '8138', '8126', '8100']
    thisRune = runes[number]
    return int(thisRune)


def ashe(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '9923', '8126', '8136', '8106', '8100', '8345', '8410', '8300']
    thisRune = runes[number]
    return int(thisRune)


def trynd(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '9111', '9105', '8299', '8000', '8444', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def jax(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8437', '8446', '8444', '8242', '8400', '8345', '8304', '8300']
    thisRune = runes[number]
    return int(thisRune)


def morg(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8128', '8126', '8138', '8135', '8100', '8233', '8237', '8200']
    thisRune = runes[number]
    return int(thisRune)


def zil(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8112', '8139', '8138', '8135', '8100', '8224', '8236', '8200']
    thisRune = runes[number]
    return int(thisRune)


def singed(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8010', '9111', '9105', '8014', '8000', '8234', '8275', '8200']
    thisRune = runes[number]
    return int(thisRune)


def eve(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8112', '8143', '8138', '8105', '8100', '8233', '8236', '8200']
    thisRune = runes[number]
    return int(thisRune)


def twitch(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8008', '8009', '9104', '8017', '8000', '8139', '8105', '8100']
    thisRune = runes[number]
    return int(thisRune)


def karthus(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8128', '8139', '8138', '8135', '8100', '8014', '9111', '8000']
    thisRune = runes[number]
    return int(thisRune)


def cho(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8229', '8226', '8210', '8232', '8200', '8473', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def amumu(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8351', '8306', '8316', '8347', '8300', '8473', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def rammus(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8439', '8463', '8429', '8451', '8400', '9111', '9104', '8000']
    thisRune = runes[number]
    return int(thisRune)


def anivia(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5008', '8112', '8126', '8138', '8105', '8100', '8009', '8014', '8000']
    thisRune = runes[number]
    return int(thisRune)


def shaco(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5008', '8128', '8126', '8138', '8105', '8100', '8233', '8236', '8200']
    thisRune = runes[number]
    return int(thisRune)


def mundo(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9105', '8299', '8000', '8429', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def sona(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5007', '8214', '8226', '8210', '8236', '8200', '8429', '8453', '8400']
    thisRune = runes[number]
    return int(thisRune)


def kass(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8128', '8143', '8138', '8135', '8100', '8009', '8014', '8000']
    thisRune = runes[number]
    return int(thisRune)


def irelia(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9104', '8299', '8000', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def janna(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8351', '8304', '8345', '8347', '8300', '8134', '8120', '8100']
    thisRune = runes[number]
    return int(thisRune)


def gp(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8369', '8304', '8321', '8347', '8300', '8473', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def corki(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8369', '8304', '8345', '8347', '8300', '8139', '8106', '8100']
    thisRune = runes[number]
    return int(thisRune)


def karma(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8229', '8226', '8210', '8237', '8200', '8136', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def taric(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5002', '5005', '8351', '8304', '8345', '8347', '8300', '8106', '8136', '8100']
    thisRune = runes[number]
    return int(thisRune)


def veigar(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5003', '5007', '8124', '8139', '8138', '8105', '8100', '8226', '8210', '8200']
    thisRune = runes[number]
    return int(thisRune)


def trundle(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '9111', '9104', '8014', '8000', '8410', '8304', '8300']
    thisRune = runes[number]
    return int(thisRune)


def swain(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5007', '8112', '8126', '8138', '8135', '8100', '8304', '8316', '8300']
    thisRune = runes[number]
    return int(thisRune)


def cait(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8021', '8009', '9103', '8014', '8000', '8233', '8236', '8200']
    thisRune = runes[number]
    return int(thisRune)


def blitz(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5002', '5008', '8351', '8306', '8316', '8347', '8300', '8473', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def mal(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5007', '8437', '8463', '8429', '8451', '8400', '8210', '8226', '8200']
    thisRune = runes[number]
    return int(thisRune)


def kat(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8128', '8143', '8138', '8105', '8100', '8233', '8236', '8200']
    thisRune = runes[number]
    return int(thisRune)


def noc(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '9111', '9104', '8014', '8000', '8138', '8106', '8100']
    thisRune = runes[number]
    return int(thisRune)


def mao(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5007', '8230', '8275', '8210', '8232', '8200', '8126', '8105', '8100']
    thisRune = runes[number]
    return int(thisRune)


def renek(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8005', '9111', '9105', '8299', '8000', '8242', '8444', '8400']
    thisRune = runes[number]
    return int(thisRune)


def jfour(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9104', '8014', '8000', '8304', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def elise(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8128', '8143', '8138', '8135', '8100', '8233', '8232', '8200']
    thisRune = runes[number]
    return int(thisRune)


def ori(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8214', '8226', '8210', '8237', '8200', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def wu(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9105', '8299', '8000', '8345', '8304', '8300']
    thisRune = runes[number]
    return int(thisRune)


def brand(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8112', '8139', '8138', '8135', '8100', '8304', '8345', '8300']
    thisRune = runes[number]
    return int(thisRune)


def lee(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8010', '9111', '9104', '8299', '8000', '8444', '8453', '8400']
    thisRune = runes[number]
    return int(thisRune)


def vayne(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '9111', '9103', '8017', '8000', '8135', '8139', '8100']
    thisRune = runes[number]
    return int(thisRune)


def rumble(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8229', '8275', '8234', '8237', '8200', '8242', '8444', '8400']
    thisRune = runes[number]
    return int(thisRune)


def cass(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8010', '8009', '9105', '8299', '8000', '8429', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def skarner(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5007', '9923', '8126', '8138', '8106', '8100', '8226', '8210', '8200']
    thisRune = runes[number]
    return int(thisRune)


def heim(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8229', '8226', '8233', '8237', '8200', '8345', '8304', '8300']
    thisRune = runes[number]
    return int(thisRune)


def nasus(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5002', '5005', '8008', '9111', '9104', '8299', '8000', '8444', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def nid(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8128', '8143', '8138', '8135', '8100', '8210', '8232', '8200']
    thisRune = runes[number]
    return int(thisRune)


def udyr(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8010', '9111', '9105', '8299', '8000', '8429', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def poppy(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8230', '8275', '8234', '8232', '8200', '8347', '8306', '8300']
    thisRune = runes[number]
    return int(thisRune)


def gragas(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5008', '8010', '9111', '9104', '8014', '8000', '8304', '8321', '8300']
    thisRune = runes[number]
    return int(thisRune)


def panth(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8010', '9111', '9104', '8299', '8000', '8473', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def ez(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8112', '8139', '8138', '8135', '8100', '8304', '8345', '8300']
    thisRune = runes[number]
    return int(thisRune)


def mord(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9105', '8299', '8000', '8473', '8453', '8400']
    thisRune = runes[number]
    return int(thisRune)


def yorick(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5002', '5005', '8437', '8446', '8444', '8451', '8400', '8410', '8304', '8300']
    thisRune = runes[number]
    return int(thisRune)


def akali(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5002', '5007', '8230', '8275', '8234', '8232', '8200', '8306', '8321', '8300']
    thisRune = runes[number]
    return int(thisRune)


def kennen(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5002', '5007', '8351', '8306', '8321', '8347', '8300', '8242', '8444', '8400']
    thisRune = runes[number]
    return int(thisRune)


def garen(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8010', '9111', '9105', '8299', '8000', '8429', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def leo(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5002', '5005', '8351', '8306', '8316', '8347', '8300', '8473', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def malz(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5007', '8128', '8126', '8138', '8106', '8100', '8009', '8014', '8000']
    thisRune = runes[number]
    return int(thisRune)


def talon(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8010', '8009', '9105', '8299', '8000', '8345', '8304', '8300']
    thisRune = runes[number]
    return int(thisRune)


def riven(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8010', '9111', '9105', '8299', '8000', '8275', '8210', '8200']
    thisRune = runes[number]
    return int(thisRune)


def kog(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8008', '9111', '9103', '8299', '8000', '8429', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def shen(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8437', '8401', '8429', '8453', '8400', '9111', '9104', '8000']
    thisRune = runes[number]
    return int(thisRune)


def lux(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8229', '8275', '8210', '8237', '8200', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def xerath(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8229', '8226', '8210', '8237', '8200', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def shy(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8005', '9111', '9105', '8299', '8000', '8138', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def ahri(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8112', '8126', '8138', '8106', '8100', '8226', '8210', '8200']
    thisRune = runes[number]
    return int(thisRune)


def graves(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8021', '9111', '9104', '8299', '8000', '8136', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def fizz(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8112', '8143', '8138', '8135', '8100', '8014', '9111', '8000']
    thisRune = runes[number]
    return int(thisRune)


def voli(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8005', '9111', '9105', '8299', '8000', '8234', '8232', '8200']
    thisRune = runes[number]
    return int(thisRune)


def rengar(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8021', '9111', '9104', '8299', '8000', '8473', '8453', '8400']
    thisRune = runes[number]
    return int(thisRune)


def varus(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8229', '8226', '8210', '8237', '8200', '8304', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def naut(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5002', '5005', '8439', '8463', '8473', '8242', '8400', '8306', '8316', '8300']
    thisRune = runes[number]
    return int(thisRune)


def viktor(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8214', '8226', '8210', '8237', '8200', '8473', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def sej(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5002', '5005', '8230', '8275', '8210', '8232', '8200', '8126', '8106', '8100']
    thisRune = runes[number]
    return int(thisRune)


def fio(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5002', '5005', '8351', '8304', '8345', '8347', '8300', '8106', '8136', '8100']
    thisRune = runes[number]
    return int(thisRune)


def ziggs(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8229', '8226', '8233', '8232', '8200', '8139', '8106', '8100']
    thisRune = runes[number]
    return int(thisRune)


def lulu(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5007', '8214', '8226', '8210', '8236', '8200', '8429', '8453', '8400']
    thisRune = runes[number]
    return int(thisRune)


def draven(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8008', '8009', '9104', '8014', '8000', '8138', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def hec(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5007', '8010', '9111', '9105', '8299', '8000', '8453', '8444', '8400']
    thisRune = runes[number]
    return int(thisRune)


def kha(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8369', '8304', '8321', '8347', '8300', '8143', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def dar(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8010', '9111', '9104', '8299', '8000', '8444', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def jayce(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8230', '8226', '8233', '8236', '8200', '8304', '8345', '8300']
    thisRune = runes[number]
    return int(thisRune)


def liss(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8112', '8126', '8138', '8106', '8100', '8226', '8237', '8200']
    thisRune = runes[number]
    return int(thisRune)


def diana(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9104', '8014', '8000', '8304', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def quinn(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8005', '9111', '9103', '8014', '8000', '8139', '8138', '8100']
    thisRune = runes[number]
    return int(thisRune)


def syndra(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8369', '8304', '8345', '8347', '8300', '8226', '8210', '8200']
    thisRune = runes[number]
    return int(thisRune)


def asol(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8112', '8139', '8138', '8105', '8100', '8234', '8236', '8200']
    thisRune = runes[number]
    return int(thisRune)


def kayn(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5008', '8010', '9111', '9105', '8014', '8000', '8321', '8304', '8300']
    thisRune = runes[number]
    return int(thisRune)


def zoe(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8112', '8139', '8138', '8135', '8100', '8224', '8236', '8200']
    thisRune = runes[number]
    return int(thisRune)


def zyra(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8229', '8226', '8210', '8237', '8200', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def kaisa(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '8009', '9103', '8014', '8000', '8139', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def seraph(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8229', '8226', '8210', '8237', '8200', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def gnar(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8021', '9111', '9104', '8299', '8000', '8451', '8473', '8400']
    thisRune = runes[number]
    return int(thisRune)


def zac(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5007', '8010', '9111', '9105', '8299', '8000', '8138', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def yas(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '9111', '9104', '8299', '8000', '8473', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def vel(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8229', '8226', '8210', '8236', '8200', '8304', '8345', '8300']
    thisRune = runes[number]
    return int(thisRune)


def tali(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5008', '8128', '8126', '8138', '8135', '8100', '8226', '8210', '8200']
    thisRune = runes[number]
    return int(thisRune)


def akshan(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8005', '8009', '9104', '8014', '8000', '8139', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def cam(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8437', '8401', '8473', '8242', '8400', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def bel(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5008', '8010', '9111', '9104', '8014', '8000', '8304', '8321', '8300']
    thisRune = runes[number]
    return int(thisRune)


def braum(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5002', '5005', '8465', '8463', '8473', '8242', '8400', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def jhin(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8128', '8139', '8136', '8135', '8100', '8304', '8345', '8300']
    thisRune = runes[number]
    return int(thisRune)


def kindred(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8005', '9111', '9104', '8014', '8000', '8138', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def zeri(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '9101', '9104', '8014', '8000', '8473', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def jinx(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '8009', '9103', '8017', '8000', '8304', '8345', '8300']
    thisRune = runes[number]
    return int(thisRune)


def tahm(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5003', '5007', '8465', '8463', '8444', '8242', '8400', '8304', '8410', '8300']
    thisRune = runes[number]
    return int(thisRune)


def viego(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8010', '9111', '9105', '8299', '8000', '8304', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def senna(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5002', '5005', '8021', '8009', '9104', '8017', '8000', '8135', '8138', '8100']
    thisRune = runes[number]
    return int(thisRune)


def lucian(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8369', '8304', '8345', '8347', '8300', '8226', '8237', '8200']
    thisRune = runes[number]
    return int(thisRune)


def zed(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8112', '8139', '8138', '8106', '8100', '8210', '8275', '8200']
    thisRune = runes[number]
    return int(thisRune)


def kled(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9105', '8299', '8000', '8143', '8120', '8100']
    thisRune = runes[number]
    return int(thisRune)


def ekko(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8128', '8143', '8138', '8135', '8100', '9111', '9105', '8000']
    thisRune = runes[number]
    return int(thisRune)


def qiyana(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8369', '8304', '8316', '8347', '8300', '8451', '8444', '8400']
    thisRune = runes[number]
    return int(thisRune)


def vi(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8010', '9111', '9104', '8014', '8000', '8304', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def aatrox(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5008', '8010', '9111', '9104', '8299', '8000', '8444', '8446', '8400']
    thisRune = runes[number]
    return int(thisRune)


def nami(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8214', '8226', '8233', '8236', '8200', '8120', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def azir(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8010', '8009', '9104', '8014', '8000', '8226', '8237', '8200']
    thisRune = runes[number]
    return int(thisRune)


def yuumi(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8214', '8226', '8210', '8237', '8200', '8017', '8009', '8000']
    thisRune = runes[number]
    return int(thisRune)


def samira(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9103', '8299', '8000', '8143', '8135', '8100']
    thisRune = runes[number]
    return int(thisRune)


def thresh(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8351', '8313', '8345', '8347', '8300', '8473', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def illoai(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8010', '8009', '9105', '8299', '8000', '8429', '8453', '8400']
    thisRune = runes[number]
    return int(thisRune)


def rek(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9104', '8014', '8000', '8304', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def ivern(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5007', '8214', '8275', '8210', '8232', '8200', '8105', '8138', '8100']
    thisRune = runes[number]
    return int(thisRune)


def kalista(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '9111', '9104', '8299', '8000', '8135', '8139', '8100']
    thisRune = runes[number]
    return int(thisRune)


def bard(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5002', '5005', '8021', '9111', '9105', '8014', '8000', '8242', '8429', '8400']
    thisRune = runes[number]
    return int(thisRune)


def rakan(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '8465', '8463', '8473', '8242', '8400', '8106', '8136', '8100']
    thisRune = runes[number]
    return int(thisRune)


def xayah(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '8009', '9103', '8017', '8000', '8304', '8345', '8300']
    thisRune = runes[number]
    return int(thisRune)


def ornn(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8437', '8446', '8429', '8451', '8400', '8304', '8345', '8300']
    thisRune = runes[number]
    return int(thisRune)


def sylas(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5008', '8369', '8304', '8345', '8347', '8300', '8444', '8242', '8400']
    thisRune = runes[number]
    return int(thisRune)


def rell(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5002', '5007', '8351', '8306', '8321', '8347', '8300', '8242', '8444', '8400']
    thisRune = runes[number]
    return int(thisRune)


def neeko(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5001', '5008', '5005', '8005', '9111', '9103', '8299', '8000', '8429', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def aphelios(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8008', '9101', '9103', '8017', '8000', '8139', '8134', '8100']
    thisRune = runes[number]
    return int(thisRune)


def pyke(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5008', '9923', '8126', '8136', '8135', '8100', '9111', '9105', '8000']
    thisRune = runes[number]
    return int(thisRune)


def sett(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8021', '9111', '9105', '8299', '8000', '8444', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def vex(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8112', '8126', '8138', '8106', '8100', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def yone(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5008', '5005', '8008', '9111', '9104', '8299', '8000', '8444', '8451', '8400']
    thisRune = runes[number]
    return int(thisRune)


def gwen(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '8009', '9105', '8299', '8000', '8242', '8473', '8400']
    thisRune = runes[number]
    return int(thisRune)


def lillia(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8437', '8446', '8429', '8451', '8400', '8304', '8345', '8300']
    thisRune = runes[number]
    return int(thisRune)


def renata(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5002', '5005', '8465', '8463', '8473', '8453', '8400', '8136', '8105', '8100']
    thisRune = runes[number]
    return int(thisRune)


def nil(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5002', '5008', '5005', '8010', '9111', '9104', '8299', '8000', '8345', '8347', '8300']
    thisRune = runes[number]
    return int(thisRune)


def ks(number):
    # [Bottom, Middle, Top]    [Top, TopMiddle, BotMiddle, Bot, RuneType, subOne, subTwo, subType]
    runes = ['5003', '5002', '5007', '8437', '8446', '8473', '8451', '8400', '8226', '8210', '8200']
    thisRune = runes[number]
    return int(thisRune)
