from lemay_ai_sidecar import lemay_ai_sidecar
import os

# DEFINE PRETRAINED MODEL
fname_pretrained="crawl-300d-2M.vec"

if not os.path.exists(fname_pretrained):
    !wget https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M.vec.zip
    !unzip crawl-300d-2M.vec.zip

#THE FASTTEXT MODEL FROM THE PAPER WAS TRAINED USING VECSIZE 100 AND WINDOWSIZE 2
model,fname_sidecar,fname_custom = lemay_ai_sidecar().extendEmbeddingModel(dataset_csv="dataset.csv",
                                                                           fname_pretrained=fname_pretrained)