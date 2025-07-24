import request
import os
class main:
    
        request_instance = request.Request(os.getenv('API_KEY'))
        start = "2023-01-01T00:00:00UTC"
        end = "2023-01-02T00:00:00UTC"
        station = "89070"
        try:
            request_instance.get_weather(start, end, station)
        except Exception as e:
            print(f"An error occurred: {e}")