class Home:
    
    list_rooms = []
    
    def __init__(self,home_name:str,num_rooms:int,number_beds:int):
        self.home_name = home_name
        self.num_rooms = num_rooms
        self.number_beds = number_beds 
        for i in range(self.num_rooms):
            Home.list_rooms.append([])
            for _ in range(self.number_beds):
                Home.list_rooms[i].append(False)
    
    