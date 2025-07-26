class Menu:
    
    def selectDate(self):
        """
        FUNCTION: selectDate
        1.Requests date from user
        2.Requests time from user
        3.Returns date and time in UTC format
        PARAMETERS: None
        RETURNS: selected_date (str)
        """
        print("Please select a date:")

        selected_date = input("Enter date (YYYY-MM-DD): ")
        print("Please select a time:")
        selected_time = input("Enter time (HH:MM:SS): ")   
        selected_date += "T" + selected_time + "UTC"      
        print(f"Selected date and time: {selected_date}")
        return selected_date
    
    def selectStation(self):
        """FUNCTION: selectStation
        1.Requests station from user
        2.Returns station code
        PARAMETERS: None
        RETURNS: selected_station (str)
        """
        print("Please select a station:")
        print("1. Station Gabriel de Castilla")
        print("2. Station Juan Carlos I")
        choice = int(input("Enter the number of the station:"))
        if choice == 1:
            selected_station = "89070"
        elif choice == 2:
            selected_station = "89064"
        return selected_station
    
    def selectAggregationType(self):
        """
        FUNCTION: selectAggregationType
        1.Requests aggregation type from user
        2.Returns aggregation type
        PARAMETERS: None
        RETURNS: aggregation_type (str)
        """
        print("Please select an aggregation type:")
        print("0. None")    
        print("1. Daily")
        print("2. Hourly")
        print("3. Monthly")
        choice = int(input("Enter the number of the aggregation type:"))
        if choice == 1:
            aggregation_type = "Daily"
        elif choice == 2:
            aggregation_type = "Hourly"
        elif choice == 3:
            aggregation_type = "Monthly"
        else:
            aggregation_type = "None"
        return aggregation_type 