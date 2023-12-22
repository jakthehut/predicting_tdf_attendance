import pandas as pd
from sklearn.preprocessing import MinMaxScaler


"""Preprocessing of data by
- Dropping confusing or non relevant columns
- Data normalization
- Providing one Hot encoding mehtod for later
"""
df = pd.read_csv("C:/Users/hutte/Documents/CEU-University-Coding/ceu/Machine Learning Intro/course_project/data manipulation/cleaned_cycling_tdf.csv", index_col=0)

df = df.drop("name", axis=1)  # more confusing than not, riders can be idetified by indices
df = df.drop("pcs points", axis=1)  #regression shows this is more misleading
df = df.drop("uci points", axis=1)  #regression shows this is more misleading


def one_hot_encode_teams(dataframe):
    '''One Hot encode one categorical column of dataframe and reutrn whole encoded dataframe and list of team names'''
    one_hot = pd.get_dummies(dataframe["team"], prefix="team_")
    local_df = dataframe.drop("team",axis = 1)
    team_names = one_hot.columns.to_list()
    return local_df.join(one_hot), team_names
df, columns_team_names = one_hot_encode_teams(df)


def normalize_data(df):
    '''Give one-hot encoded dataframe, returned normalized'''
    non_binary_columns = df.select_dtypes(exclude=['bool']).columns.tolist()
    non_binary_columns = non_binary_columns[1:] # season is later needed for test, train split
    
    # Normalize non-binary columns using MinMaxScaler
    scaler = MinMaxScaler()
    df[non_binary_columns] = scaler.fit_transform(df[non_binary_columns])
    return df

df = normalize_data(df)

def remove_team_columns(dataframe):
    return dataframe.drop(columns_team_names)

df.to_csv("preprocessed_cycling_tdf.csv")


