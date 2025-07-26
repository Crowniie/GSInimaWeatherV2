import requests
import pandas 
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
        RETURNS: Pandas DataFrame with the raw weather data
        """
        requestURL = self.URL.format(startDate=startDate, endDate=endDate, station=station) + f"?api_key={self.api_key}"
        #First request to get the data URL
        
        urlResponse = requests.get(requestURL)
        if urlResponse.status_code == 200:
            response = urlResponse.json()
            weatherDataURL = response['datos']
        else:
            raise Exception(f"Error fetching data URL: {urlResponse.status_code} - {urlResponse.text}")
        
        #Second request to get the actual weather data
        dataResponse = requests.get(weatherDataURL)
        print(f"Fetching data from: {weatherDataURL}")
        if dataResponse.status_code == 200:
            weatherData = dataResponse.json()
            df = pandas.DataFrame(weatherData)
            df_parsed = df[['nombre','fhora','temp','pres','vel']]
            df_parsed.rename(columns={
            'nombre': 'Station',
            'fhora': 'Datetime',
            'temp': 'Temperature (ºC)',
            'pres': 'Pressure (hPa)',
            'vel': 'Speed (m/s)'
        }, inplace=True)
            return df_parsed
        else:
            raise Exception(f"Error fetching weather data: {dataResponse.status_code} - {dataResponse.text}")
