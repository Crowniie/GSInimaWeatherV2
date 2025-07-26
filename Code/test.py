import pytest
import pandas
import request

class Test:
    
        
    def test_get_weather_success():
        """
        Test that get_weather returns a DataFrame with the expected columns
        when given valid parameters.
        """
        api_key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsYW5jZWxvdGdhbWVwbGF5czIwMTVAZ21haWwuY29tIiwianRpIjoiNjE1ZmQ1ZGQtYzNiMS00NjYyLTg0MDMtZDYxZGM1NGQ3MjZiIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3NTM0ODc2ODYsInVzZXJJZCI6IjYxNWZkNWRkLWMzYjEtNDY2Mi04NDAzLWQ2MWRjNTRkNzI2YiIsInJvbGUiOiIifQ.ZjkoMHnYrU4Ob_9IysOPiLcJ0zdXFfGFrz7dq9BVBck"
        start_date = "2023-01-01T00:00:00UTC"
        end_date = "2023-02-01T00:00:00UTC"
        station = "89070"
        request_instance = request.Request(api_key)
        
        df = request_instance.get_weather(start_date, end_date, station)
        assert isinstance(df, pandas.DataFrame)
        assert 'Station' in df.columns
        assert 'Datetime' in df.columns
        assert 'Temperature (ºC)' in df.columns
        assert 'Pressure (hPa)' in df.columns
        assert 'Speed (m/s)' in df.columns
    
    test_get_weather_success()