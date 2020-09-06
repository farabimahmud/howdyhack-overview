import pandas as pd 

def get_scores():
    dataframe = pd.read_csv("https://raw.githubusercontent.com/farabimahmud/howdyhack-overview/master/overview/output.csv")
    results = dataframe.groupby(['prediction']).mean()
    # print(dataframe.groupby(['prediction']).mean() )
    return results['score'].values.tolist()

