# sidecar
Sidecar: Augmenting Word Embedding Models With Expert Knowledge


# The data for the paper was pulled from https://cloud.google.com/bigquery/public-data/stackoverflow
# Example queries: 
## SELECT title, tags  FROM [bigquery-public-data:stackoverflow.posts_questions] where tags = 'php' LIMIT 10000
## SELECT body, tags  FROM [bigquery-public-data:stackoverflow.posts_questions] where tags = 'c++' LIMIT 1000
