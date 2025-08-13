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
   ```data```: containing DICT dataset for develop GNN model without and with TL, hERG dataset for develop pretrained model for fine-tuning, and example csv file for apply the optimal TL_GNN model to predict whether a given chemical (with SMILES) is cardiotoxic or not.     
   
   ```trained_models```: the optimal GNN model on DICT;   

   ```trf_learning_models```: the pretrained model based on hERG dataset and the optimal TL_GNN model on DICT;  

### Model     
   ```engine.py, model.py, utils.py```  : contain GNN models and helper functions;
   
   ```config.py``` : hyperparameters and constant variables;
   
   ```Hypers_tuning_and_train_GNN_models.ipynb``` : develop GNN models;
   
   ```Pretrained_TL_models.ipynb```: contains train and validation set for developing GNN models；    
   
   ```TL_models_under_different_strategies.ipynb``` : develop GNN models;
   
   ```Predict.ipynb```: contains train and validation set for developing GNN models；
   
   (Acknowledgments: The code origninated from previous reference: DOI: 10.1021/acs.jcim.3c00554)
