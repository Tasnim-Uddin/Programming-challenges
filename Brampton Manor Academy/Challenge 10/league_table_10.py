import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")


def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents


def process_results(rows):
    dictionary = {}
    for row in rows:
        home, away, homegoals, awaygoals, winner = row[1], row[2], row[3], row[4], row[5]

        if home not in dictionary:
            dictionary[home] = [0,0]
        if away not in dictionary:
            dictionary[away] = [0,0]

        if winner == "D":
            dictionary[home][0] += 1
            dictionary[away][0] += 1

        elif winner == "H":
            dictionary[home][0] += 3
            dictionary[away][0] += 0

        elif winner == "A":
            dictionary[home][0] += 0
            dictionary[away][0] += 3
        
        dictionary[home][1] = dictionary[home][1] + int(homegoals) - int(awaygoals)
        dictionary[away][1] = dictionary[away][1] + int(awaygoals) - int(homegoals)
        
    return dictionary

def sorting_tuple():
    new_dictionary = {key: value for key, value in sorted(results.items(),key = lambda value: value[1], reverse = True)} 
    return new_dictionary
    
def output_table(new_dictionary):
    print("PREMIER LEAGUE 16-17 SEASON")
    print()
    print(f'{"Teams":<16} {"Points":<16} {"Goal Difference":<16}')
    for i in new_dictionary:
            print(f'{i:<16} {new_dictionary[i][0]:<16} {new_dictionary[i][1]:<16}')
    
    
if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    results = process_results(file_contents)
    new_dictionary = sorting_tuple()
    output_table(new_dictionary)
    


