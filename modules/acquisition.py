import pandas as pd


def bicimad_dataframe():
    #print("Esta es la estación de BICIMAD")
    df_mad_final = pd.read_csv('./data/bicimad_project.csv')
    #print(df_mad_final)
    return df_mad_final

bicimad_dataframe()


def bicipark_dataframe():
    #print("Esta es la estación de BICIPARK")
    df_park_final = pd.read_csv('./data/bicipark_project.csv')
    #print(df_park_final)
    return df_park_final

bicipark_dataframe()
    

