import pandas as pd
import redis


def create_dummy_df():
    print("Redis imported")
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [5, 10, 15]})
    print(df)
    return df


if __name__=='__main__':
    try:
        while True:
            df = create_dummy_df()
    except (KeyboardInterrupt, SystemExit):
        print('Exited on user request')
