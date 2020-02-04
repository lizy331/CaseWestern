import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression


def histogram_intersection(a, b):
    v = np.minimum(a, b).sum().round(decimals=1)
    return v


def main():
    train_data = pd.read_csv('./train_sak_geo.csv').astype(str)
    # train_data['success_outcome'] = 0
    #
    # train_data.loc[train_data['Disposition'] != ' ', 'success_outcome'] = 1
    # train_data.loc[train_data['Jurisdiction_Prosecutor'] != ' ', 'success_outcome'] = 1
    # train_data.loc[train_data['Grand_Jury_ever'] == '1', 'success_outcome'] = 1
    # train_data.loc[train_data['Pros_county_accept'] == '1', 'success_outcome'] = 1
    # train_data.loc[train_data['Prosacceptcharges'] == '1', 'success_outcome'] = 1
    # train_data.loc[train_data['Arrestmade'] == '1', 'success_outcome'] = 1
    # train_data.loc[train_data['CasetoPros'] == '1', 'success_outcome'] = 1
    #
    #
    # train_data.loc[train_data['lack_V_foll_up'] == '1', 'success_outcome'] = 0
    # train_data.loc[train_data['V_uncoop_cannot_contact'] == '1', 'success_outcome'] = 0
    # train_data.loc[train_data['ReasonGiven_Closing_recoded'] == '1', 'success_outcome'] = 0
    # train_data.loc[train_data['ReasonGiven_Closing_recoded'] == '3', 'success_outcome'] = 0
    # train_data.loc[train_data['ReasonGiven_Closing_recoded'] == '6', 'success_outcome'] = 0
    # train_data.loc[train_data['ReasonGiven_Closing_recoded'] == '7', 'success_outcome'] = 0
    # train_data.loc[train_data['ReasonGiven_Closing_recoded'] == '10', 'success_outcome'] = 0
    # train_data.loc[train_data['ReasonGiven_Closing_recoded'] == '11', 'success_outcome'] = 0
    #
    # train_data.loc[train_data['forensic_aware'] != '0', 'forensic_aware'] = 1
    # train_data.to_csv('./train_sak_geo.csv')
    goodv = []
    with open('./catagories.csv', 'r', encoding='utf-8') as f:
        to_explain = f.read().splitlines()
    df = train_data[to_explain]
    for category in to_explain:
        df.loc[df[category] == '-999', category] = np.nan
        df.loc[df[category] == '999', category] = np.nan
        df.loc[df[category] == ' ', category] = np.nan
    df = df.dropna()
    print(df.corr(method='spearman'))
    x = df.drop(columns=['success_outcome'])
    # x = df.drop(columns=['credibility_issue_exist'])
    # y = df['ReasonGiven_Closing_recoded']
    y = df['success_outcome']

    logreg = LogisticRegression()
    rfe = RFE(logreg, 20)
    rfe = rfe.fit(x, y.values.ravel())
    print(rfe.support_)
    print(rfe.ranking_)


if __name__ == '__main__':
    print('start program')
    main()
    print('end program')