# Sidecar: Augmenting Word Embedding Models With Expert Knowledge

![Results High Level Summary](https://github.com/lemay-ai/sidecar/images/accuracy.png)

This repository was released by Lemay.ai as open source software under the license specified in this repository (GPLv3), and represents the work product described in the research paper "Sidecar: Augmenting Word Embedding Models With Expert Knowledge"

# Installation

First off, the current version of fasttext is not playing nicely with pip, and so you must, before installing this package, install fasttext via the command line. All other dependencies will auto-install. And so please begin by installing fasttext as follows:
```
pip3 install fasttext
```
Now, the following commands sholud get you the rest of the software:

```
git clone https://github.com/lemay-ai/sidecar.git
cd sidecar/
python3 setup.py install
```

# Testing

Test the library using the test data supplied in the repository as follows. It takes about 10 to 25 minutes to run the test:

```
python3 test.py
```

# Testing Data Origin
The data for the paper was pulled from https://cloud.google.com/bigquery/public-data/stackoverflow

Example queries: 
```SQL
SELECT title, tags  FROM [bigquery-public-data:stackoverflow.posts_questions] where tags = 'php' LIMIT 10000
SELECT body, tags  FROM [bigquery-public-data:stackoverflow.posts_questions] where tags = 'c++' LIMIT 1000
```
