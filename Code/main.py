import request
import os
import Menu
import Aggregation
from dotenv import load_dotenv
class main:
        #Environment loading for API key retrieval
        load_dotenv()
        
        #Class instantiation
        menu_instance = Menu.Menu()
        request_instance = request.Request(os.getenv('API_KEY'))
        aggregation_instance = Aggregation.Aggregation()
        
        print("Welcome to the Antarctica Weather Data Aggregator!")
        
        print("Please introduce the start date")
        start = menu_instance.selectDate()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("Please introduce the end date")
        end = menu_instance.selectDate()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        station = menu_instance.selectStation()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        aggregationType = menu_instance.selectAggregationType()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("Fetching weather data...")
        try:
          weatherResponse =  request_instance.get_weather(start, end, station)
        except Exception as e:
            print(f"An error occurred: {e}")
            
        if aggregationType != "None":
          aggregatedData = aggregation_instance.aggregate_data(weatherResponse, aggregationType) 
        else:
          aggregatedData = weatherResponse
        print(aggregatedData) 
