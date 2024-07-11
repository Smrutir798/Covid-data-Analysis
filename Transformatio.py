import pandas as pd

def load_data():
    url = "Dataset/WHO-COVID-19-global-data.csv"
    df = pd.read_csv(url)
    return df

def transform_data(df):
    df.loc[df['Country']=='Namibia','Country_code'] = 'NM'
    df.fillna({'New_cases': df['New_cases'].mean()}, inplace=True)
    df.fillna({'New_deaths': df['New_deaths'].mean()}, inplace=True)
    df[df['WHO_region'].isnull()]['Country'].unique()
    df.fillna({'WHO_region': 'OTHER'}, inplace=True)
    return df

def save_data(df):
    df.to_csv("Dataset/New_covid_19_DataSet.csv", index=False)
    return None

def main():
    df = load_data()
    df = transform_data(df)
    save_data(df)
    print("Data Transformation is done successfully")
    return None

main()