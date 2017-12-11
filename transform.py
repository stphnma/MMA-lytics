import os
import json
import pandas as pd
from datetime import datetime

def extract():
    files = os.listdir(os.getcwd() + "/raw")
    totals = pd.DataFrame()
    fight_details = pd.DataFrame()
    sig_strikes = pd.DataFrame()
    fight_details = []

    for f in files:
        with open(os.getcwd() + "/raw/"+f) as json_data:
            js = json.load(json_data)

            for dd in js:

                totals_df = pd.DataFrame(dd['totals'])
                totals_df['url'] = dd['url']
                sig_strikes_df = pd.DataFrame(dd['sig_strikes'])
                sig_strikes_df['url'] = dd['url']


                dd['fight_details']['url'] = dd['url']
                dd['fight_details']['date'] = dd['date']

                for result in dd.get('fight_results',[]):
                    if result['result'] == "W":
                        dd['fight_details']['winner'] = result['name']
                    elif result['result'] == "L":
                        dd['fight_details']['loser'] = result['name']
                    else:
                        pass


                fight_details.append(dd['fight_details'])

                totals = pd.concat([totals, totals_df])
                sig_strikes = pd.concat([sig_strikes, sig_strikes_df])

    fight_details  = pd.DataFrame(fight_details)

    return totals, sig_strikes, fight_details

def transform_sig_stikes(df):

    df['body_strikes'] = df['body'].apply(lambda x: x.split(" of ")[0]).astype(int)
    df['body_attempts'] = df['body'].apply(lambda x: x.split(" of ")[1]).astype(int)
    df['ground_strikes'] = df['ground'].apply(lambda x: x.split(" of ")[0]).astype(int)
    df['ground_attempts'] = df['ground'].apply(lambda x: x.split(" of ")[1]).astype(int)
    df['head_strikes'] = df['head'].apply(lambda x: x.split(" of ")[0]).astype(int)
    df['head_attempts'] = df['head'].apply(lambda x: x.split(" of ")[1]).astype(int)
    df['leg_strikes'] = df['leg'].apply(lambda x: x.split(" of ")[0]).astype(int)
    df['leg_attempts'] = df['leg'].apply(lambda x: x.split(" of ")[1]).astype(int)
    df['distance_strikes'] = df['distance'].apply(lambda x: x.split(" of ")[0]).astype(int)
    df['distance_attempts'] = df['distance'].apply(lambda x: x.split(" of ")[1]).astype(int)
    df['clinch_strikes'] = df['clinch'].apply(lambda x: x.split(" of ")[0]).astype(int)
    df['clich_attempts'] = df['clinch'].apply(lambda x: x.split(" of ")[1]).astype(int)

    cols = ['url','name','round',
            'body_strikes','body_attempts','ground_strikes','ground_attempts','head_strikes','head_attempts','leg_strikes','leg_attempts',
            'distance_strikes','distance_attempts', 'clinch_strikes','clich_attempts'
    ]

    return df[cols]

def transform_totals(df):

    df['td_success'] = df['td'].apply(lambda x: x.split(" of ")[0]).astype(int)
    df['td_attempt'] = df['td'].apply(lambda x: x.split(" of ")[0]).astype(int)

    cols = ['url','name','round', 'td_attempt', 'td_success']
    return df[cols]


if __name__ == '__main__':


    totals, sig_strikes, fight_details = extract()

    sig_strikes_transformed = transform_sig_stikes(sig_strikes)


    # data = transform(totals, sig_strikes, fight_details)

    # byFight = data.groupby(['url','name','date','method','time']).sum().reset_index()

    # byFightShifted = pd.DataFrame()
    # for fighter, group in byFight.groupby('name'):
    #     group = group.set_index('date')
    #     byFightShifted = pd.concat([group.cumsum().shift(-1), byFightShifted])



