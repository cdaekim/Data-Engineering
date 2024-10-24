import json
import csv
import urllib
import time


class APIError(Exception):
    pass

class DataError(Exception):
    pass


matchid_list = []

#update file name for puuid list
with open('matchid_eun1.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        for i in range(1,len(row)):
            matchid_list.append(row[i])

matchid_list = list(set(matchid_list))

api_key = "YOUR API KEY"
region = "YOUR REGION"
platform = "YOUR PLATFORM"

def create_data_row(j,matchid):
    URL = "https://"+platform+".api.riotgames.com/lol/match/v5/matches/"+matchid+"?api_key="+api_key        
    
    try:
        request = urllib.request.urlopen(URL)
        
    except urllib.error.HTTPError as e:
        print(f"\n{e.reason} on record {j}")
        raise APIError
    
    else:
        try:
            data = json.loads(request.read())
            data_row = []
            data_row.append(j)
            data_row.append(data['metadata']['matchId'])
            data_row.append(data['info']['gameCreation'])
            data_row.append(data['info']['gameMode'])
            data_row.append(data['info']['gameType'])
            data_row.append(data['info']['gameVersion'])
            data_row.append(data['info']['mapId'])
            data_row.append(data['info']['queueId'])
            #data_row.append(data['info']['tournamentCode'])
            for i in range(0,10):
                data_row.append(data['info']['participants'][i]['puuid'])
                data_row.append(data['info']['participants'][i]['championName'])
                data_row.append(data['info']['participants'][i]['win'])
            return data_row
        except Exception as e:
            print(f"\n{e} on record {j}")
            raise DataError
            


#reduce delay based on performance - start with 1.2 and go down to lowest without bombing after 100 records
delay = 0.8

#adjust start index if restarting; 0 for first run
start = 0

with open('matchdata_eun1.csv', 'a+', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the data
    for i in range(start,200000):
        print(f"\rprocessing {i} of {len(matchid_list)}",end="\r")
        try:
            writer.writerow(create_data_row(i,matchid_list[i]))  
            time.sleep(delay)
        except APIError:
            print("\nretrying in 130s")
            time.sleep(130)
            try:
                writer.writerow(create_data_row(i,matchid_list[i]))  
                time.sleep(delay)
            except:
                print(f"\nskipping record {i}")
                pass
        except DataError:
            print(f"\nskipping record {i}")
            time.sleep(delay)
            pass
