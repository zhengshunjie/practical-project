#-*- coding: utf-8 -*-
'''
直接处理没有整理过的图像数据
'''
import glob
import os.path
import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile

#原始输入数据的目录，这个目录下有5个子目录，每个子目录底下保存属于该类别的所有图片
INPUT_DATA='D:\program\python\flower_photos'
#输出文件地址。将整理后的图片通过numpy的格式保存。
OUTPUT_FILE='D:\program\python\flower_photos\flower_processed_data.npy'

#测试数据和验证数据比例
VALIDATION_PERCENTAGE=10
TEST_PERCENTAGE=10

#读取数据并将数据分割成训练数据、验证数据和测试数据
def create_image_lists(sess,testing_percentage,validation_percentage):
  sub_dirs=[x[0] for x in os.walk(INPUT_DATA)]
  is_root_dir=True

  #初始化各个数据集
  training_images=[]
  training_labels=[]
  testing_images=[]
  testing_labels=[]
  validation_images=[]
  validation_labels=[]
  current_label=0

  #读取所有的子目录
  for sub_dir in sub_dirs:
    if is_root_dir:
      is_root_dir=False
      continue
    


