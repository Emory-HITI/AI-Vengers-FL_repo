# Federated Learning (AI-Vengers Assemble)

## Phase 1: CXR

This document outlines the data and computational requirements for participating in the AI-Vengers Federated Learning effort. 

### Compute Requirements

1. Deep Learning Base AMI (Ubuntu 18.04)  
2. Test/Demo - t2.2xlarge   
3. 8 vCPU, 32GB memory, 100GB EBS disk, network performance “Moderate”   

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
1 - Asian  
2 - Hispanic (if reliable)  
3 - White  
4 - Indigenous Populations  

#### Data Preparation

1. Prepare a CSV file with two columns ["Path", "Race"]  
-add data preprocessing
2. Run the data preprocessing scripts which will output a JSON file for the train, test, and validation sets  
3. Copy these JSON files into the data directory of your client  
4. Symlink your JSON file to a file named dataset.json `ln -s [json file] dataset.json`  



