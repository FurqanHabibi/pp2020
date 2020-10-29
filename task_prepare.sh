#!/bin/bash

# 1 --------------------------------
# download test set and development set
# get test datasets
wget http://data.csail.mit.edu/places/places365/val_large.tar

# get development set (trainig data of KonIQ-10k)
wget http://datasets.vqa.mmsp-kn.de/archives/koniq10k_512x384.zip

# 2 --------------------------------
# extract data from tar/zip balls
tar -xvf val_large.tar
unzip koniq10k_512x384.zip -d ./koniq10k_512x384/


# 3 --------------------------------
# pre-process development/test data
python preprocess_data.py

echo "preparation done!"
