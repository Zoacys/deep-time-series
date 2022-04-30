from models.seq2seq import Informer, Autoformer, Transformer, GruAttention, Gru, Lstm, GAU
from models import Gdnn, TCN, TPA, Trans, DeepAR, BenchmarkLstm, BenchmarkMlp, LSTNet
from data.data_loader import Dataset_ETT_hour, Dataset_ETT_minute, Dataset_Custom, Dataset_Pred, SDWPFDataSet, MyDataSet, ToyDataset
from models.informer1.model import Informer as Infomer1
dataset_dict = {
'ETTh1':Dataset_ETT_hour,
'ETTh2':Dataset_ETT_hour,
'ETTm1':Dataset_ETT_minute,
'ETTm2':Dataset_ETT_minute,
'WTH':Dataset_Custom,
'ECL':Dataset_Custom,
'Solar':Dataset_Custom,
'custom':Dataset_Custom,
'Mydata':MyDataSet,
"SDWPF":SDWPFDataSet,
'Toy': ToyDataset,
}

model_dict = {
'edlstm': Lstm,
'edgru': Gru,
'edgruattention':GruAttention,
'informer':Informer,
'informer1':Infomer1,
'transformer': Transformer,
'autoformer': Autoformer,
'mlp':BenchmarkMlp,
'lstm':BenchmarkLstm,
'tcn':TCN,
'tpa':TPA,
'trans':Trans,
'lstnet':LSTNet,
'gated':Gdnn,
'deepar':DeepAR,
'gau':GAU
}