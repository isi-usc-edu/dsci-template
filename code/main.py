from get_data import get_launches_data
from analyze_data import analyze

URL = 'https://dsci.isi.edu/api/launches?interval=date'


if __name__ == '__main__':

    # get the orbital launches data first
    data = get_launches_data(URL)

    # get a pandas data frame
    df = analyze(data)

    print(df.describe())


    # visualize data
