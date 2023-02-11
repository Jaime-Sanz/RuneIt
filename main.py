import requests
import json
import re
import clientData


def getapikey():
    k = open("C://Key.txt", "r")
    return k.read()


key = getapikey()


def getsummoner(name):
    summoner = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
    summonerUpdated = summoner + "?api_key=" + key
    summonerResp = requests.get(summonerUpdated)
    summonerInfo = summonerResp.json()
    summonerPuuid = summonerInfo["puuid"]
    return summonerPuuid


def getmatchhistory(Id):
    matches = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{Id}/ids?start=0&count=20"
    matchesUpdated = matches + "&api_key=" + key
    matchesResp = requests.get(matchesUpdated)
    matchesInfo = matchesResp.json()
    return matchesInfo


def getmatchdata(mid):
    data = f"https://americas.api.riotgames.com/lol/match/v5/matches/{mid}"
    dataUpdated = data + "?api_key=" + key
    dataResp = requests.get(dataUpdated)
    dataInfo = dataResp.json()
    return dataInfo


def main():
    cr = open("C://CR.txt", "w")
    dard = getsummoner("")
    dardMH = getmatchhistory(dard)
    for x in range(10):
        dardMD = getmatchdata(dardMH[x])
        for i in range(10):
            json_Champ = json.dumps(dardMD["info"]["participants"][i]["championName"])
            json_Runes = json.dumps(dardMD["info"]["participants"][i]["perks"])
            dardRunes = returnrunes(json_Runes)
            dardChamps = json_Champ
            cr.write(dardChamps + "\n" + str(dardRunes) + "\n")
    cr.close()

def returnrunes(jsonrunes):
    pattern = r"(?<!\S)@?(?=[A-Za-z\d]{1,4}\b)[A-Za-z]*\d[A-Za-z\d]*"
    connections = re.findall(pattern, jsonrunes)
    runesLimit = [x for x in connections if
                  len(x) >= 4]  # this line makes sure that the runes are larger than 3 or fewer digits
    onlyRunes = [x for x in runesLimit if not x.startswith('0') if not x.startswith('1') if not x.startswith('2')
                 # returns only the runes
                 if not x.startswith('3') if not x.startswith('4') if not x.startswith('6') if not x.startswith('7')]
    return onlyRunes


if __name__ == "__main__":
    main()
