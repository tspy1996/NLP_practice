import os
import torch
files = ['train', 'test']
# bert_model = 'pretrained_bert_models/bert-base-chinese/'
#roberta_model = 'pretrained_bert_models/chinese-roberta-wwm-ext/'
pretrained_model = 'experiments/pretrain/'
model_dir = 'experiments/pretrain/'

# 句子最長長度
max_length = 30

# 是否加載訓練好的模型
load_before = False

# 是否對整個BERT進行 fine tuning
full_fine_tuning = False

# hyper-parameter
learning_rate = 3e-5
weight_decay = 0.01
clip_grad = 5

batch_size = 16
epoch_num = 30
min_epoch_num = 5
patience = 0.0002
patience_num = 10

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

labels = ['疾病和診斷', '影像檢查', '實驗室檢驗', '手術', '藥物','解剖部位']

label2id = {
    "O": 0,
    "B-疾病和診斷": 1,
    "B-影像檢查": 2,
    "B-實驗室檢驗": 3,
    'B-手術': 4,
    'B-藥物': 5,
    'B-解剖部位': 6,
    "I-疾病和診斷": 7,
    "I-影像檢查": 8,
    "I-實驗室檢驗": 9,
    'I-手術': 10,
    'I-藥物': 11,
    'I-解剖部位': 12
}

id2label = {_id: _label for _label, _id in list(label2id.items())}