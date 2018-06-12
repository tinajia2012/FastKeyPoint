import sys
import os

def get_data(data_root, is_train=True, is_val=False):
  dataset = [file for file in os.listdir(data_root)]
    

if __name__ == '__main__':
  data_root = sys.argv[1]
  train_data, val_data = get_data(data_root, is_train, is_val)
  net = get_net()
  train(train_data, val_data, net)