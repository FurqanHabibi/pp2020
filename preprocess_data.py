# this script is to extract test images for Pixel Privacy Task 2020 from
# Places365-Standard Data set.
from PIL import Image
import pandas as pd
from tqdm import tqdm
import os

places_data_path = './val_large/'
koniq10k_data_path = './koniq10k_512x384/512x384/'
test_save_path = './pp2020_test/'
val_save_path ='./pp2020_dev/'

if not os.path.exists(test_save_path):
    os.makedirs(test_save_path)

test_images = pd.read_csv('./MEPP20labels/MEPP20test.csv', header=None).values

for item in tqdm(test_images):
    img = Image.open(places_data_path + str(item[0])).convert('RGB')
    width, height = img.size
    new_width = 512
    new_height = 384
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    img = img.crop((left, top, right, bottom))

    img.save(test_save_path + str(item[0]).split('.')[0] + '.png')
    
if not os.path.exists(val_save_path):
    os.makedirs(val_save_path)
    
dev_images = pd.read_csv('./MEPP20labels/MEPP20dev.csv', header=None).values[:, 1]

for item in tqdm(dev_images):
    if item.split('.')[-1] == 'jpg':
        img = Image.open(koniq10k_data_path + item).convert('RGB')
        img.save(val_save_path + item)

