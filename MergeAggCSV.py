import os

import pandas as pd
from pandas import DataFrame

result = []


def load_csv_files(folder):
    time = 0
    for filename in os.listdir(folder):
        sub_folders = os.path.join(folder, filename)
        for file in os.listdir(sub_folders):
            if file.endswith(".csv"):
                f = os.path.join(sub_folders, file)
                print("Working File: ", f)
                
                if time == 0:
                    col_names = extract_col_name(f)
                    time += 1
                save_current_data(f, col_names)

    return col_names


def save_current_data(f, column_name):
    global result
    df = pd.read_csv(f, sep='delimiter',
                     engine="python")

    list_data = df.values.tolist()
    data_1 = list_data[7:]
    gameId = f[:-35]
    gameId2 = gameId[-7:] 
    #data_2 = list_data[26:]
    game_name = (
        str(list_data[0]).replace('Game ID: ', '').replace(']', '').replace('[', '').replace('"', '').replace("'",'')).split(',')
    game_name = gameId2
    print(game_name)
    for i in range(len(data_1)):
        current_row = (str(data_1[i]).replace('[', '').replace(']', '').replace('"', '').replace("'", '')).split(',')
        current_row.insert(0,game_name)
        result.append(current_row)

        print(current_row)
    #for i in range(len(data_2)):
        #current_row = (str(data_2[i]).replace('[', '').replace(']', '').replace('"', '').replace("'", '')).split(',')
        #current_row.insert(0,game_name)

        #result.append(current_row)

        #print(current_row)


def extract_col_name(f):
    df = pd.read_csv(f, sep='delimiter',
                     engine="python")
    list_data = df.values.tolist()
    # print(list_data[0])

    column_names = (str(list_data[6]).replace('[', '').replace(']', '').replace('"', '').replace("'", '')).split(',')
    print(column_names)
    return column_names

    # Reading the desired data


path = "C:/Users/James Rhodes Gym 1/Documents/EPL Second Spectrum/Season 22-23/Aggs/Week 38"
col_name = load_csv_files(path)

print(len(result))

df_result = DataFrame(result)
col_name.insert(0, "Game ID")
df_result.columns = col_name
df_result.to_csv(r'Week_38.csv', index=False, header=True)

list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0