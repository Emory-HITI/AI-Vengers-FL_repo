# Federated Learning (AI-Vengers Assemble)

## Phase 1: CXR

This document outlines the data and computational requirements for participating in the AI-Vengers Federated Learning effort. 

### Compute Requirements

1. Deep Learning Base AMI (Ubuntu 18.04)  
2. Test/Demo - t2.2xlarge   
3. 8 vCPU, 32GB memory, 100GB EBS disk, network performance “Moderate”
4. At least 1 GPU

### Data Requirements

Mandatory Fields:
- Self Reported Race  
- Gender  
- Age 

Optional Fields:
- Scanner Type
- Finding vs No Finding

#### Label Format

0 - Black   
1 - Asian Taiwanese  
2 - Asian Vietnamese  
3 - Asian Pakistani  
4 - Asian Korean  
5 - Asian Laotian  
6 - Asian Indian  
7 - Asian Chinese  
8 - Asian Filipino  
9 - Asian Japanese  
10 - Asian Other  
11 - White  
12 - American Indian or Alaska Native  
13 - Native Hawaiian or Other Pacific Islander  

#### Data Preparation

1. Prepare a CSV file with two columns ["Path", "Race"]  
2. Run the data preprocessing scripts which will output a JSON file for the train, test, and validation sets  
   `python create_jsons.py [path/to/csv]`
4. Copy these JSON files into the data directory of your client  
5. Symlink your JSON file to a file named dataset.json `ln -s [json file] dataset.json`  



