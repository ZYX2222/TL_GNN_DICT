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
   ```data```: containing DICT dataset for develop GNN model without and with TL, hERG dataset for develop pretrained model for fine-tuning, and example csv file for apply the optimal TL_GNN model;     
   
   ```trained_models```: the optimal GNN model on DICT;   

   ```trf_learning_models```: the pretrained model based on hERG dataset and the optimal TL_GNN model on DICT.  

### Model     
   ```engine.py, model.py, utils.py```  : contain GNN models and helper functions;
   
   ```config.py``` : hyperparameters and constant variables;
   
   ```GNN_models.ipynb``` : Hyperparameter tuning and GNN model development;
   
   ```Pretrained_models.ipynb```: develop pretrained GNN models based on hERG dataset；    
   
   ```TL_models_under_different_strategies.ipynb``` : develop TL_GNN models and evaluate different stategies that affect model performance; the strategies including using different numbers of epochs for pre-training models, reducing learning rates, and appointing different numbers of training epochs before triggering the early stopping mechanism. 
   
   ```Predict.ipynb```: apply the optimal TL_GNN model to predict whether a given chemical (with SMILES) is cardiotoxic or not；
   
   (Acknowledgments: The code origninated from previous reference: DOI: 10.1021/acs.jcim.3c00554)
