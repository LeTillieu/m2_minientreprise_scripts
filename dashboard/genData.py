from pymongo import MongoClient
import random
from datetime import datetime,timedelta
import time
import pytz

wait_time=20 # time interval between two generations of datas
initial_datas=180 # numbre of datas generated at the beginning (180==1 hour of datas)
#Connect to DB
session = MongoClient("192.168.2.12:27017",username= "root",password="JRTKSjqdO4d5")  
db = session.dashboard

#init data

matrice_ca={
    "1":
        {
        "moy":9000,
        "min":0.97,
        "max":1.2
        },
    "2":
        {
        "moy":6000,
        "min":0.95,
        "max":1.1 
        },
    "3":
        {
        "moy":3000,
        "min":0.90,
        "max":1.05 
        },
    "4":
        {
        "moy":1000,
        "min":0.90,
        "max":1.0 
        }
}


matrice_avis={
    "1":
        {
        "moy":9,
        "min":0.97,
        "max":1.2 
    },
    "2":
        {
        "moy":6,
        "min":0.95,
        "max":1.1 
        },
    "3":
        {
        "moy":3,
        "min":0.90,
        "max":1.05 
        },
    "4":
        {
        "moy":1,
        "min":0.90,
        "max":1.0 
        }
    }


#datas generation
date=datetime.utcnow()
for sec in range(initial_datas):
    #Get Param : 
    f=open("/home/user/Documents/Scenarii_Projet_MiniEntreprise/dashboard/conf.txt")
    lines=f.readlines()
    f.close()
    i=0
    param=[]
    while i<len(lines):
        line=lines[i]
        splitArr=line.split(":")
        param.append([splitArr[0],splitArr[1].strip()])
        i+=1
    ca_moy=matrice_ca[param[0][1]]["moy"]
    avis_moy=matrice_avis[param[1][1]]["moy"]
    ca_min=matrice_ca[param[0][1]]["min"]
    avis_min=matrice_avis[param[1][1]]["min"]
    ca_max=matrice_ca[param[0][1]]["max"]
    avis_max=matrice_avis[param[1][1]]["max"]

    cur_date = date - timedelta(seconds=20*sec)

    value_ca=ca_moy*random.uniform(ca_min,ca_max)
    db.datas.insert_one({"timestamp":cur_date,"value":value_ca,"name":"CA"})

    value_avis=avis_moy*random.uniform(avis_min,avis_max)
    db.datas.insert_one({"timestamp":cur_date,"value":value_avis,"name":"AVIS"})


while(True):
    #Get Param : 
    f=open("/home/user/Documents/Scenarii_Projet_MiniEntreprise/dashboard/conf.txt")
    lines=f.readlines()
    f.close()
    i=0
    param=[]
    while i<len(lines):
        line=lines[i]
        splitArr=line.split(":")
        param.append([splitArr[0],splitArr[1].strip()])
        i+=1


    
    ca_moy=matrice_ca[param[0][1]]["moy"]
    avis_moy=matrice_avis[param[1][1]]["moy"]
    ca_min=matrice_ca[param[0][1]]["min"]
    avis_min=matrice_avis[param[1][1]]["min"]
    ca_max=matrice_ca[param[0][1]]["max"]
    avis_max=matrice_avis[param[1][1]]["max"]

    #insert Data in Db
    
    date=datetime.utcnow()
   
        #generate for CA
    value_ca=ca_moy*random.uniform(ca_min,ca_max)
    db.datas.insert_one({"timestamp":date,"value":value_ca,"name":"CA"})

        #generate for AVIS
    value_avis=avis_moy*random.uniform(avis_min,avis_max)
    db.datas.insert_one({"timestamp":date,"value":value_avis,"name":"AVIS"})

    time.sleep(wait_time)

