import pandas as pd
import datetime


def get_scores():
    dataframe = pd.read_csv(
        "https://raw.githubusercontent.com/farabimahmud/howdyhack-overview/master/overview/output.csv")
    results = dataframe.groupby(['prediction']).mean()
    # print(dataframe.groupby(['prediction']).mean() )
    return results['score'].values.tolist()


def get_daywise_score():
    df = pd.read_csv("https://raw.githubusercontent.com/farabimahmud/howdyhack-overview/master/overview/daily_data.csv")

    mean_scores = df.groupby(['prediction', 'date']).mean()
    mean_scores = mean_scores.reset_index()


    df[['date']] = mean_scores['date'].apply(get_date)
    scores = {}

    cutoff_date = datetime.date(2020, 9, 1)

    topics = ['football', 'covid', 'BLM', 'student', 'online', 'dog']
    for i in range(len(topics)):
        filter_before_cutoff = df['date'] < cutoff_date
        filter_same_class = df['prediction'] == i+1
        scores[topics[i]] = df[filter_same_class][filter_before_cutoff]['score'].values.tolist()
    return scores


def get_date(s):
    try:
        l = []
        if '-' not in s:
            l = [int(x) for x in s.split('/')]
            return datetime.date(l[2], l[1], l[0])
        l = [int(x) for x in s.split('-')]
    except:
        print(s)
        pass
    return datetime.date(l[0], l[1], l[2])

def get_name_range_for_dates():
    n = 31
    m = 8
    dates = []
    for i in range(n):
        dates.append("{:02}-{:02}".format(m, i+1))
    return dates


def formatted_data_for_chart(scores):
    '''
    label: 
                // backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data:  {{ }}
    '''
    data = list()
    topics = ['football', 'covid', 'BLM', 'student', 'online', 'dog']
    colors = [
        'rgb(255, 99, 132)',
        'rgb(0, 99, 100)',
        'rgb(100, 99, 0)',
        'rgb(255, 0, 132)',
        'rgb(255, 0, 255)',
        'rgb(100, 100, 132)',
    ]
    for i in range(len(topics)):
        data.append(
            {
                'label': topics[i],
                'borderColor' : colors[i],
                'data' : scores[topics[i]],
                'fill' : 'false',
            }
        )
        
    return data 

# print(get_daywise_score())
# print(len(get_daywise_score()))
# from pprint import pprint

# pprint(formatted_data_for_chart(get_daywise_score()))

