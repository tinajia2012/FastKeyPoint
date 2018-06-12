import sys
import os

def get_data(fold, fold_num =5, is_train=True, is_val=False):
  data_root = sys.argv[1]
  train_data = []; val_data = []
  for index, root in enumerate(os.listdir(data_root)):
    if index%FOLD_num == fold:
      val_data.append(root)
    else:
      train_data.append(root)
    

if __name__ == '__main__':
  
  train_data, val_data = get_data(1 , flod_num=5, is_train=True, is_val=False)
  net = get_net()
  train(train_data, val_data, net)