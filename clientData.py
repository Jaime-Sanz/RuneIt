import json
import requests
import time
import championData

from lcu_driver import Connector


connector = Connector()

global runeType, subRuneType, keyStone, runeRowOne, runeRowTwo, runeRowThree, \
    subRuneRowOne, subRuneRowTwo, \
    statOne, statTwo, statThree, championName


def get_champions_name(_id):
    all_champion_id = {
        1: 'Annie',
        2: 'Olaf',
        3: 'Galio',
        4: 'Twisted Fate',
        5: 'Xin Zhao',
        6: 'Urgot',
        7: 'LeBlanc',
        8: 'Vladimir',
        9: 'Fiddlesticks',
        10: 'Kayle',
        11: 'Master Yi',
        12: 'Alistar',
        13: 'Ryze',
        14: 'Sion',
        15: 'Sivir',
        16: 'Soraka',
        17: 'Teemo',
        18: 'Tristana',
        19: 'Warwick',
        20: 'Nunu & Willump',
        21: 'Miss Fortune',
        22: 'Ashe',
        23: 'Tryndamere',
        24: 'Jax',
        25: 'Morgana',
        26: 'Zilean',
        27: 'Singed',
        28: 'Evelynn',
        29: 'Twitch',
        30: 'Karthus',
        31: "Cho'Gath",
        32: 'Amumu',
        33: 'Rammus',
        34: 'Anivia',
        35: 'Shaco',
        36: 'Dr.Mundo',
        37: 'Sona',
        38: 'Kassadin',
        39: 'Irelia',
        40: 'Janna',
        41: 'Gangplank',
        42: 'Corki',
        43: 'Karma',
        44: 'Taric',
        45: 'Veigar',
        48: 'Trundle',
        50: 'Swain',
        51: 'Caitlyn',
        53: 'Blitzcrank',
        54: 'Malphite',
        55: 'Katarina',
        56: 'Nocturne',
        57: 'Maokai',
        58: 'Renekton',
        59: 'JarvanIV',
        60: 'Elise',
        61: 'Orianna',
        62: 'Wukong',
        63: 'Brand',
        64: 'LeeSin',
        67: 'Vayne',
        68: 'Rumble',
        69: 'Cassiopeia',
        72: 'Skarner',
        74: 'Heimerdinger',
        75: 'Nasus',
        76: 'Nidalee',
        77: 'Udyr',
        78: 'Poppy',
        79: 'Gragas',
        80: 'Pantheon',
        81: 'Ezreal',
        82: 'Mordekaiser',
        83: 'Yorick',
        84: 'Akali',
        85: 'Kennen',
        86: 'Garen',
        89: 'Leona',
        90: 'Malzahar',
        91: 'Talon',
        92: 'Riven',
        96: "Kog'Maw",
        98: 'Shen',
        99: 'Lux',
        101: 'Xerath',
        102: 'Shyvana',
        103: 'Ahri',
        104: 'Graves',
        105: 'Fizz',
        106: 'Volibear',
        107: 'Rengar',
        110: 'Varus',
        111: 'Nautilus',
        112: 'Viktor',
        113: 'Sejuani',
        114: 'Fiora',
        115: 'Ziggs',
        117: 'Lulu',
        119: 'Draven',
        120: 'Hecarim',
        121: "Kha'Zix",
        122: 'Darius',
        126: 'Jayce',
        127: 'Lissandra',
        131: 'Diana',
        133: 'Quinn',
        134: 'Syndra',
        136: 'AurelionSol',
        141: 'Kayn',
        142: 'Zoe',
        143: 'Zyra',
        145: "Kai'sa",
        147: "Seraphine",
        150: 'Gnar',
        154: 'Zac',
        157: 'Yasuo',
        161: "Vel'Koz",
        163: 'Taliyah',
        166: "Akshan",
        164: 'Camille',
        200: "Belveth",
        201: 'Braum',
        202: 'Jhin',
        203: 'Kindred',
        221: 'Zeri',
        222: 'Jinx',
        223: 'TahmKench',
        234: 'Viego',
        235: 'Senna',
        236: 'Lucian',
        238: 'Zed',
        240: 'Kled',
        245: 'Ekko',
        246: 'Qiyana',
        254: 'Vi',
        266: 'Aatrox',
        267: 'Nami',
        268: 'Azir',
        350: 'Yuumi',
        360: 'Samira',
        412: 'Thresh',
        420: 'Illaoi',
        421: "Rek'Sai",
        427: 'Ivern',
        429: 'Kalista',
        432: 'Bard',
        497: 'Rakan',
        498: 'Xayah',
        516: 'Ornn',
        517: 'Sylas',
        526: 'Rell',
        518: 'Neeko',
        523: 'Aphelios',
        555: 'Pyke',
        875: "Sett",
        711: "Vex",
        777: "Yone",
        887: "Gwen",
        876: "Lillia",
        888: "Renata",
        895: "Nilah",
        897: "KSante"
    }
    return all_champion_id.get(_id)


@connector.ready
async def connect(connection):
    global summoner_Id
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    summoner_to_json = await summoner.json()
    summoner_Id = summoner_to_json['summonerId']


@connector.ws.register('/lol-champ-select/v1/current-champion', event_types=('CREATE', 'UPDATE',))
async def champ_select_changed(connection, event):
    currentChamp = await connection.request('get', '/lol-champ-select/v1/current-champion')
    currentChamp_to_json = await currentChamp.json()
    championName = get_champions_name(int(currentChamp_to_json))

    if championName != 0:
        runePageName = "RuneIt- {}".format(championName)
        runeType = championData.runes(championName, 7)  # 7
        subRuneType = championData.runes(championName, 10)  # 10
        keyStone = championData.runes(championName, 3)  # 3
        runeRowOne = championData.runes(championName, 4)  # 4
        runeRowTwo = championData.runes(championName, 5)  # 5
        runeRowThree = championData.runes(championName, 6)  # 6
        subRuneRowOne = championData.runes(championName, 8)  # 8
        subRuneRowTwo = championData.runes(championName, 9)  # 9
        statOne = championData.runes(championName, 2)  # 2
        statTwo = championData.runes(championName, 1)  # 1
        statThree = championData.runes(championName, 0)  # 0

        runePageBody = {
            "name": runePageName,
            "primaryStyleId": runeType,
            "subStyleId": subRuneType,
            "selectedPerkIds": [keyStone, runeRowOne, runeRowTwo, runeRowThree,
                                subRuneRowOne, subRuneRowTwo, statOne,
                                statTwo, statThree],
            "current": True
        }

        currentRunePage = await connection.request('get', '/lol-perks/v1/currentpage')
        currentRunePage_to_json = await currentRunePage.json()
        runePageId = currentRunePage_to_json['id']
        runePageAdd = await connection.request('put', f'/lol-perks/v1/pages/{runePageId}', data=runePageBody)
        print("Runes Added For: " + championName)


@connector.close
async def disconnect(connection):
    print('Finished task')


connector.start()