import sys
import os

if __name__ == '__main__':
  data_root = sys.argv[1]
  train_data, val_data = get_data(data_root)
  net = get_net()
  train(train_data, val_data, net)