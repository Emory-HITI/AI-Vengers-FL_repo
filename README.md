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

0 - American Indian or Alaska Native     
1 - Asian  
2 - Black or African American   
3 - Hispanic or Latino  
4 - Native Hawaiian or Other Pacific Islander    
5 - White   

#### Data Preparation
1. Extract metadata and pngs from your DICOMs using Niffler PNG Extaction found here https://github.com/Emory-HITI/Niffler/tree/master/modules/png-extraction  
2. Prepare a CSV file with two columns ["Path", "Race"]  
3. Run the data preprocessing scripts which will output a JSON file for the train, test, and validation sets  
   `python create_jsons.py [path/to/csv]`
4. Copy these JSON files into the data directory of your client  
5. Symlink your JSON file to a file named dataset.json `ln -s [json file] dataset.json`  



