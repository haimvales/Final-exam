import csv
from home import Home
# import home

def sort_csv(filename, sort_by, reverse=False):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        fieldnames = reader.fieldnames
    rows.sort(key=lambda x: int(x[sort_by]), reverse=reverse)
    output_file = f'sorted_numeric_{sort_by}.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f" ORDER BY {sort_by}")
  
  
def room_allocation_csv(filename):
    for_len = 0
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        fieldnames = reader.fieldnames
    if len(Home.list_rooms) <= len(rows):
        for i in Home.list_rooms:
            for_len += len(i)
    else:
        for_len = len(rows)
 
    result = 0
    for i in range(len(Home.list_rooms)):
        for j in range(len(Home.list_rooms[i])):
            rows[result]["is_it_assigned"] = True
            rows[result]["status"] = f"room:{i+1},bed:{j+1}"
            Home.list_rooms[i][j] = True
            result  += 1
    if len(rows) > len(Home.list_rooms):
        for i in range(for_len,len(rows)):
                rows[i]["is_it_assigned"] = False
                rows[i]["status"] = f"Waiting to be placed"            
    fieldnames.append('is_it_assigned')
    fieldnames.append('status')
    
    output_file = f'allocation.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames) 
        writer.writerows(rows)  
    
       
                
  
  
   














