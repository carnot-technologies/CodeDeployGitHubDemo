import pandas as pd


def create_dummy_df():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 8, 12]})
    print(df)
    return df


if __name__=='__main__':
    try:
        while True:
            df = create_dummy_df()
    except (KeyboardInterrupt, SystemExit):
        print('Exited on user request')
