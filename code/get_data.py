import requests

def get_launches_data(url):
    """
    Fetch launches data from dsci.isi.edu/api

    Args:
        url - string url indicating where to get the data

    Returns:
        data: orbital launches data fetched from our api
    """

    response = requests.get(url)

    data = response.json()

    return data

