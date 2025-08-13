# TL_GNN_DICT

## Environment

The most important python packages are:   

python == 3.9.15   
pytorch == 1.12.1  
rdkit == 2022.09.5   
scikit-learn == 1.2.0   
optuna == 3.1.0   
numpy == 1.23.5   
pyvis == 0.3.2   

To replicate or devleop or apply models more conveniently, the environment file <environmental.yml> is provided to install environment directly.    


```
conda env create -f environment.yaml
```   


## Main
### Folder   
   ```data```: hERG dataset with 13818 SMILES and pIC50 values, which is used to develop XGBoost-CECFP model;  
   
   ```trained_models```: hERG dataset with 13890 SMILES, pIC50 values, and two source informantion, which is used to develop XGBoost-CECFP-S model;   

   ```trf_learning_models```: hERG dataset with 6952 SMILES and pIC50 values from ChEMBL, which is used to develop XGBoost-CECFP-C model;  

### Model     
   ```engine.py, model.py, utils.py```  : contain GNN models and helper functions;
   
   ```config.py``` : hyperparameters and constant variables;
   
   ```Hypers_tuning_and_train_GNN_models.ipynb``` : develop GNN models;
   
   ```Pretrained_TL_models.ipynb```: contains train and validation set for developing GNN models；    
   
   ```TL_models_under_different_strategies.ipynb``` : develop GNN models;
   
   ```Predict.ipynb```: contains train and validation set for developing GNN models；
   
   (Acknowledgments: The code origninated from previous reference: DOI: 10.1021/acs.jcim.3c00554)
