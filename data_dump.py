import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME ="aps"# client["neurolabDB"]
COLLECTION_NAME ="sensor"# dataBase['Products']



if __name__ =="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print((f"Rows and Columns :{df.shape}"))

    #convert dataframe to json so that we can dump these record in mongoDB

    df.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())
    # print(json_record[0])
     
    #insert converted json to mongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)











