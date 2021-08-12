import requests

def get_traffic_data(lat, lon):
    traffic_api_key = "WyzLeVkyIi34SlO4nC2gt1yldAO76OMe"
    coordinates = str(lat) + "," + str(lon)
    params = {"key": traffic_api_key, "point": coordinates}
    trafficRequest = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json", params=params)
    trafficResponse = trafficRequest.json() #Converts into type 'dict'
    if 'error' in trafficResponse:
        traffic_dict = {
            "roadType": "FRC6",
            "currentRoadSpeed": 40,
            "currentFreeFlowSpeed": 40,
            "isRoadClosed": False
        }
        return traffic_dict

    else:
        allTrafficApiData = trafficResponse.get('flowSegmentData')

        # All data from the Traffic API
        roadType = allTrafficApiData.get('frc')
        currentRoadSpeed = allTrafficApiData.get('currentSpeed') # This is the speed at the time the API request was made.  This should be compared with free flow speed
        currentFreeFlowSpeed = allTrafficApiData.get('freeFlowSpeed') # This is the speed if everything was running under ideal conditions
        isRoadClosed = allTrafficApiData.get('roadClosure') #This indicates if the road is closed to traffic or not.

        traffic_dict = {
            "roadType": roadType,
            "currentRoadSpeed": currentRoadSpeed,
            "currentFreeFlowSpeed": currentFreeFlowSpeed,
            "isRoadClosed": isRoadClosed
        }

        return traffic_dict