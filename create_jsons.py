import pandas as pd
import os
import json
import sys
from sklearn.model_selection import train_test_split

def convert_MMAR(df):
    path = None
    
    path = list(map(lambda x: x.split("/")[-1], df['Path']))
    label = list(df['Label'])
    ret_list = []
    for p, l in zip(path, label):
        
        if l == 0: 
            temp_map = {"image":p, "label":[1, 0, 0, 0, 0]}
        elif l == 1:
            temp_map = {"image":p, "label":[0, 1, 0, 0, 0]}
        elif l == 2:
            temp_map = {"image":p, "label":[0, 0, 1, 0, 0]}
        elif l == 3:
            temp_map = {"image":p, "label":[0, 0, 0, 1, 0]}
        elif l == 4: 
            temp_map = {"image":p, "label":[0, 0, 0, 0, 1]}
        else:
            print("Skipping")
            
        ret_list.append(temp_map)
    return ret_list

def convert_to_json(df, save_csv=True):
        train, valid = train_test_split(df, test_size=0.25, random_state=2021)
        valid, test = train_test_split(valid, test_size=0.5, random_state=2021)
        print(train["Label"].value_counts(), valid["Label"].value_counts())
        
        if save_csv:
            train.to_csv("train.csv")
            valid.to_csv("valid.csv")
            test.to_csv("test.csv")

        mmar_train = convert_MMAR(train)
        mmar_valid = convert_MMAR(valid)
        mmar_test = convert_MMAR(test)

        MMAR_train_valid = {"label_format":[1, 1, 1, 1, 1], "training":mmar_train, "validation":mmar_valid}
        MMAR_test = {"label_format":[1, 1, 1, 1, 1], "validation":mmar_valid}

        json_obj = json.dumps(MMAR_train_valid, indent=4)

        with open("train.json", 'w') as f:
            json.dump(MMAR_train_valid, f, indent=4)
            
        with open("test.json", 'w') as f:
            json.dump(MMAR_test, f, indent=4)
        
if __name__ == "__main__":
    if len(sys.argv) > 3:
        raise ValueError("Malformed command line. Please specify the path to your data csv")
    
    csv_path = sys.argv[1]
    print('Converting CSV to JSON')
    df = pd.read_csv(csv_path)
    convert_to_json(df)

        
    