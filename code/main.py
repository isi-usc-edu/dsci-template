from get_data import get_launches_data

URL = 'https://dsci.isi.edu/api/launches'


if __name__ == '__main__':

    # get the orbital launches data first
    data = get_launches_data(URL)

    # analyze data

    import pdb
    pdb.set_trace()


    # visualize data
