import pandas as pd

data = pd.read_csv("Machine Learning Intro\course_project\data manipulation\cycling_tdf.csv")
def create_rider_dict(df):
    rider_names = {}
    rinder_index = 1
    for name in set(df["name"].to_list()):
        rider_names[name]=rinder_index
        rinder_index += 1
    return rider_names
rider_enum = create_rider_dict(data)