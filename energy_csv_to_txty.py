
import csv
index = []
t = []
dem = []
win = []
sol = []
airtemp = []

with open('Y15_v4.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile,delimiter=' ')
    next(reader)  
    for row in reader:
        index.append((row[0]))  
        t.append(row[1])
        dem.append((row[2]))
        win.append((row[3]) ) 
        sol.append((row[4]) )
        airtemp.append((row[5])) 
        
    print(f"Time: {t[17519]}, Dem: {dem[17519]}, Win: {win[17519]}, Sol: {sol[17519]}, AirTemp: {airtemp[17519]}")

with open('A2_Operational_2015.txt', 'w') as file:

    file.write('D: [ ')
    
    # Write data for each row
    for i in range(911,1583):
        file.write(f" {dem[i]} ")
    
    file.write(f' ] \n')

    file.write('W_2015: [ ')
    
    # Write data for each row
    for i in range(911,1583):
        file.write(f" {win[i]} ")
    
    file.write(f' ] \n')

    file.write('S_2015: [ ')
    
    # Write data for each row
    for i in range(911,1583):
        file.write(f" {sol[i]} ")
    
    file.write(f' ] \n')




with open('A2_Planning_2015.txt', 'w') as file:

    file.write('D: [ ')
    
    # Write data for each row
    for i in range(0,17520):
        file.write(f" {dem[i]} ")
    
    file.write(f' ] \n')

    file.write('W_2015: [ ')
    
    # Write data for each row
    for i in range(0,17520):
        file.write(f" {win[i]} ")
    
    file.write(f' ] \n')

    file.write('S_2015: [ ')
    
    # Write data for each row
    for i in range(0,17520):
        file.write(f" {sol[i]} ")
    
    file.write(f' ] \n')


