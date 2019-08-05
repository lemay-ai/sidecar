''' 
    Author: Lemay.ai
    License: GPLv3
'''
from lemay_ai_sidecar import lemay_ai_sidecar
import os
import zipfile
import wget

# DEFINE PRETRAINED MODEL
fname_pretrained="crawl-300d-2M.vec"

if not os.path.exists(fname_pretrained):
    print("DOWNLOADING A PRETRAINED MODEL FROM FACEBOOK AI RESEARCH")
    wget.download("https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M.vec.zip")
    print("DOWNLOAD COMPLETE")
    print("UNZIPPING MODEL")
    with zipfile.ZipFile("crawl-300d-2M.vec.zip","r") as zip_ref:
        zip_ref.extractall(".")
    print("UNZIPPING COMPLETE. PROCEEDING TO TEST PRETRAINED MODEL CUSTOMIZATION USING SIDECAR LIBRARY")

#THE FASTTEXT MODEL FROM THE PAPER WAS TRAINED USING VECSIZE 100 AND WINDOWSIZE 2
model,fname_sidecar,fname_custom = lemay_ai_sidecar().extendEmbeddingModel(dataset_csv="dataset.csv",
                                                                           fname_pretrained=fname_pretrained)
