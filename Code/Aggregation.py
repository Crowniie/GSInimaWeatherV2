import pandas
class Aggregation:
    """
    CLASS: Handles data aggregation from the requests 
    based on time frames.
    """
    def aggregate_data(self, df, time_frame):
        """
        FUNCTION: aggregate_data
        Aggregates the weather data based on the specified time frame.
        PARAMETERS: df (DataFrame), time_frame (str)
        """
        df['Datetime'] = pandas.to_datetime(df['Datetime'],errors='coerce')
        df.set_index('Datetime', inplace=True)
        
        numerical_df = df.select_dtypes(include=['number'])
        string_df = df.select_dtypes(exclude=['number'])
        
        map = {
            'Daily': 'D',
            'Hourly': 'H',
            'Monthly':'M'
        }
        aggregated_numerical = numerical_df.resample(map[time_frame]).sum()
        aggregated_strings = string_df.resample(map[time_frame]).first()
        aggregated_df = aggregated_numerical.join(aggregated_strings)
        

        return aggregated_df