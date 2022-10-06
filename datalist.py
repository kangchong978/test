#import pyautogui as py
#import time
#import keyboard
import pandas as pd


sheet_id = "1bIHYc0NOyRqCvoCRPJMrwQhy9vkpq3Id"
sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df=pd.read_csv(url)

#print (list(df["room_noC"]))



def list_room(choose):
    
    if choose == 'a':
        choose_list=list(df["room_noA"])
    elif choose == 'b':
        choose_list=list(df["room_noB"])
    elif choose == 'c':
        choose_list=list(df["room_noC"])
    elif choose == 'd':
        choose_list=list(df["room_noD"])
    elif choose == 'e':
        choose_list=list(df["room_noE"])
    elif choose == 'f':
        choose_list=list(df["room_noF"])
    elif choose == 'g':
        choose_list=list(df["room_noG"])
    elif choose == 'h':
        choose_list=list(df["room_noH"])
    elif choose == 'j':
        choose_list=list(df["room_noJ"])
    elif choose == 'k':
        choose_list=list(df["room_noK"])
    elif choose == 'l':
        choose_list=list(df["room_noL"])
    elif choose == 'm':
        choose_list=list(df["room_noM"])
    elif choose == 'n':
        choose_list=list(df["room_noN"])
    
    
    
    room_num=[x for x in choose_list if pd.isnull(x) ==False]
    
    lst=[]
    
    for each in room_num:
        lst.append(str(each).split('.')[0])
    final_list = [int(i) for i in lst]
    
    return final_list


#print(df.columns)




