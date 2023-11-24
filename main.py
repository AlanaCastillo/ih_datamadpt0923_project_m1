from acquisition import bicimad_dataframe
from acqisition import bicipark_dataframe
from wrangling import parsing
from fuzzywuzzy import process

def main():
    args = parsing() 
    print("args---", args, sep="\n")


    if args.bicimad:
        df_bicimad = bicimad_dataframe()
        print("df_bicimad----->", df_bicimad,sep="\n")

        if args.todas:
            return df_bicimad
        else:
            match = process.extractOne(args.lugar, df_bicimad['templo'])
            print("match------", match[0], sep="\n")
            place_especific = df_bicimad.loc[df_bicimad['templo'] == match[0]]
            print("BICIMAD RESULT----")
            print(place_especific.to_csv('./data/bicimad_result.csv', index=False, encoding= 'utf-8'))

    elif args.bicipark:
        df_bicipark = bicipark_dataframe()
        print("df_bicipark-------", df_bicipark, sep="\n")

        if args.todas:
            return df_bicipark
        else:
            match = process.extractOne(args.lugar, df_bicipark['templo'])
            print("match------", match, sep="\n")
            place_especific = df_bicipark.loc[df_bicipark['templo'] == match[0]]
            print("BICIPARK RESULT----")
            place_especific.to_csv('./data/bicipark_result.csv', index=False, encoding= 'utf-8')


if __name__ == '__main__':
    main()
