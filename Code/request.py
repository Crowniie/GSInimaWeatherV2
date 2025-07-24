import requests

class Request:
    def __init__(self, api_key):
        holder = None
        self.URL = "https://opendata.aemet.es/opendata/api/antartida/datos/fechaini/{startDate}/fechafin/{endDate}/estacion/{station}"
        self.api_key = api_key
    
    def get_weather(self, startDate,endDate,station):
        """
        FUNCTION: get_weather
        Fetches 10 minute intervals of weather data from Antartica 
        using AEMET's API with the following parameters
        PARAMETERS: startDate, endDate, station
        """
        requestURL = self.URL.format(startDate=startDate, endDate=endDate, station=station) + f"?api_key={self.api_key}"
        print(f"Requesting weather data from: {requestURL}")
        #First request to get the data URL
        urlResponse = requests.get(requestURL)
        if urlResponse.status_code == 200:
            response = urlResponse.json()
            weatherDataURL = response['datos']
        else:
            raise Exception(f"Error fetching data URL: {urlResponse.status_code} - {urlResponse.text}")
        
        #Second request to get the actual weather data
        dataResponse = requests.get(weatherDataURL)
        if dataResponse.status_code == 200:
            print("Data fetched successfully")
        return 
