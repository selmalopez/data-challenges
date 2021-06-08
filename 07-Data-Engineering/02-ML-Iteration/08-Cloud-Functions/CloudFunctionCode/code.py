
import requests
from bs4 import BeautifulSoup

import json
import datetime

from google.cloud import storage


BUCKET_NAME = "le-wagon-data"  # 🚨 replace with your bucket name


def storage_upload(request):
    """
    cloud function entry point
    """

    pass  # YOUR CODE HERE

    # logs
    print("it works!")

    # response
    return "good"


def top_3_from_hackernews():
    """
    return top 3 news from hackernews
    """

    pass  # YOUR CODE HERE


if __name__ == '__main__':

    now, res = top_3_from_hackernews()
    print(now, res)
