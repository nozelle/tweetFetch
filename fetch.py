import streamlit as st

import requests

def get_media_from_tweet_url(tweet_url):
    response = requests.get(tweet_url)
    if response.status_code == 200:
        media_url = response.json()["entities"]["media"][0]["media_url"]
        return media_url
    else:
        return None

if __name__ == "__main__":
    tweet_url = "https://twitter.com/elonmusk/status/1546850431785919424"
    media_url = get_media_from_tweet_url(tweet_url)
    st.title("Twitter Image and Tweet Text Extractor")
    st.image(media_url)

