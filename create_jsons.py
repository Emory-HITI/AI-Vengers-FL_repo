import pandas as pd
import os
import json
import numpy as np
import sys
from sklearn.model_selection import train_test_split



def convert_MMAR(df, possibleLabelCount):
    path = None
    path = list(map(lambda x: x.split("/")[-1], df["Path"]))
    label = list(df["Label"])
    ret_list = []
    for p, l in zip(path, label):
        
        if l < possibleLabelCount:
            temp_label = list(np.zeros((possibleLabelCount)).astype(int))
            temp_label[int(l)] = 1
            temp_map = {"image":p, "label":temp_label}

        else:
            print("Skipping Image: Invalid Label")
            
        ret_list.append(temp_map)
    return ret_list

def convert_to_json(df, possibleLabelCount, save_csv=True):
        train, valid = train_test_split(df, test_size=0.25, random_state=2021)
        valid, test = train_test_split(valid, test_size=0.5, random_state=2021)
        print(train["Label"].value_counts(), valid["Label"].value_counts())
        
        if save_csv:
            train.to_csv("train.csv")
            valid.to_csv("valid.csv")
            test.to_csv("test.csv")

        mmar_train = convert_MMAR(train, possibleLabelCount)
        mmar_valid = convert_MMAR(valid, possibleLabelCount)
        mmar_test = convert_MMAR(test, possibleLabelCount)

        MMAR_train_valid = {"label_format":list(np.ones(possibleLabelCount)), "training":mmar_train, "validation":mmar_valid}
        MMAR_test = {"label_format":list(np.ones(possibleLabelCount)), "validation":mmar_valid}

        json_obj = json.dumps(MMAR_train_valid, indent=4)

        with open("train.json", 'w') as f:
            json.dump(MMAR_train_valid, f, indent=4)
            
        with open("test.json", 'w') as f:
            json.dump(MMAR_test, f, indent=4)
        
if __name__ == "__main__":
    if len(sys.argv) > 3:
        raise ValueError("Malformed command line. Please specify the path to your data csv")
    
    possibleLabelCount = 14
    csv_path = sys.argv[1]
    print('Converting CSV to JSON')
    df = pd.read_csv(csv_path)
    convert_to_json(df, possibleLabelCount)

        
    