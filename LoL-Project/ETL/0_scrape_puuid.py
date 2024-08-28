#import http.client
import json
import csv
from urllib.request import urlopen
import time

##update file name for initial matchlist
##sample script execution
filepath = r"data/canisback/matchlist_eun1.json"
matchlist = json.load(open(filepath))

#update api key,region,platform (asia, americas, europe)
api_key = "YOUR_OWN"
region = "YOUR_REGION"
platform = "REGIONS_PLATFORM"

#below is the metadata and structure from the API
'''
metadata
    dataVersion
*   matchId
    participants (list of 10 puuid)

info
*   gameCreation (unix timestamp)
    gameDuration
    gameId
*   gameMode
    gameName
    gameStartTimestamp
*   gameType
*   gameVersion
*   mapId
    platformId (EUN1, etc.)
*   queueId (ranked or not)
    teams (bans, objective, etc.)
*   tournamentCode
    participants (list of 10)    

info->participants
    assists
    baronKills
    bountyLevel
    champExperience
    championId
*   championName
    championTransform
    champLevel
    cosumablesPurchased
    damageDealtToBuildings/Objectives/Turrets
    damageSelfMitigated
    deaths
    detectorWardsPlaced
    double/triple/quadra/pentaKills
    dragonKills
    firstBloodAssist/Kill
    firstTowerAssist/Kill
    gameEndedInSurrender/EarlySurrender
    goldEarned/Spent
    IndividualPostion
    inhibitor/turretKills/Lost/Takedowns
    item[0-6]
    itemPurchased
    killingSprees
    kills
    lane
    largestCriticalStrike
    largestKillingSpree
    largestMultiKill
    longestTimeSpentLiving
    magic/physical/trueDamageDealt/DealtToChampions/Taken
    neytralMinionsKilled
    nexusKills/Lost/Takedowns
    objectiveStolen/StolenAssists
    participantId
    perks
    profileIcon
*   puuid
    riotIdName/IdTagline
    role
    sightWardsBoughtInGame
    spell[1-4]Casts
    summoner[1-2]Casts/Id
    summonerId/Level/Name
    teamEarlySurrendered
    teamId
    teamPosition
    timeCCingOthers
    timePlayed
    totalDamageDealt/DealtToChampions/ShieldedOnTeammates/Taken
    totalHeal/HealsOnTeammates
    totalMinionsKilled
    totalTimeCCDealt
    totalTimeSpentDead
    totalUnitsHealed
    unrealKills
    visionScore
    visionWardsBoughtInGame
    wardsKilled/Placed
 *  win (bool)
 '''

def scrape_puuid(j,matchid):
    #update region (asia/americas/europe)
    URL = "https://"+platform+".api.riotgames.com/lol/match/v5/matches/"+region+"_"+matchid+"?api_key="+api_key        
    request = urllib.request.urlopen(URL)
    data = json.loads(request.read())
    
    #init open list and append the idx number of the canisback matchlist
    data_row = []
    data_row.append(j)

    ##how to access player id according to API data strucutre :
    ##info -> participants -> [list of 10 elements with zero index (0-9)] -> puuid 
    for i in range(0,10):
        data_row.append(data['info']['participants'][i]['puuid'])
    return data_row

#reduce delay based on performance - start with 1.2 and go down to lowest without bombing after 100 records
delay = 0.2

#adjust start index if restarting; 0 for first run
start = 0

with open(f'puuid_{region}.csv', 'a+', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    #iterate through canisback matchlist
    for i in range(start,len(matchlist)):
        print(f"\rprocessing {i}",end="\r")
        try:
            writer.writerow(scrape_puuid(i,str(matchlist[i])))  
            time.sleep(delay)
        except:
            print("\rerror, retrying in 120s",end="\r")
            time.sleep(120)
            try: 
                writer.writerow(scrape_puuid(i,str(matchlist[i])))  
                time.sleep(delay)
            except:
                pass
        
     
