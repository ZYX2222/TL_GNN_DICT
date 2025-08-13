SEED_NO = 0    #Setup on demand
DEVICE =  "cuda"
EPOCHS = 300   #Setup on demand
NUM_GRAPHS_PER_BATCH = 64
NUM_FEATURES=32
NUM_TARGET = 1
EDGE_DIM=11
PATIENCE = 10      #Setup on demand
N_SPLITS = 10      #Setup on demand

# Parameters for GNN models on DICT dataset
params_vertical_gnn = {'num_gin_layers': 1, 'num_graph_trans_layers': 2, 'hidden_size': 64, 'n_heads': 1, 'dropout': 0.1, 'learning_rate': 0.003}

#Parameters for TL_GNN models based on hERG dataset (which can be replaced with other source domains such as logKOW dataset )
best_params_vertical = {'num_gin_layers': 2, 'num_graph_trans_layers': 2, 'hidden_size': 128, 'n_heads': 1, 'dropout': 0.1, 'learning_rate': 0.001} #hERG

#best_params_vertical = {'num_gin_layers': 2, 'num_graph_trans_layers': 1, 'hidden_size': 256, 'n_heads': 2, 'dropout': 0.1, 'learning_rate': 0.001} #logKOW