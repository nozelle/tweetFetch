import streamlit as st
import tweepy
import requests
from io import BytesIO
from PIL import Image

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Twitter authentication and API setup
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to extract image and tweet text from the Twitter link
def extract_tweet_info(tweet_url):
    tweet_id = tweet_url.split('/')[-1]
    try:
        tweet = api.get_status(tweet_id, tweet_mode='extended')
        tweet_text = tweet.full_text
        if 'media' in tweet.entities:
            media_url = tweet.entities['media'][0]['media_url_https']
            image_response = requests.get(media_url)
            image = Image.open(BytesIO(image_response.content))
            return tweet_text, image
        else:
            return tweet_text, None
    except tweepy.TweepError as e:
        st.error(f"Error: {e}")
        return None, None

# Streamlit app
def main():
    st.title("Twitter Image and Tweet Text Extractor")
    st.write("Enter a Twitter link below to extract the image and tweet text.")

    tweet_url = st.text_input("Twitter URL", "")

    if st.button("Extract"):
        if tweet_url:
            tweet_text, image = extract_tweet_info(tweet_url)
            if tweet_text and image:
                st.image(image, caption=tweet_text, use_column_width=True)
            elif tweet_text:
                st.write(tweet_text)
            else:
                st.error("Failed to extract tweet information. Please check the URL.")
        else:
            st.warning("Please enter a Twitter URL.")

if __name__ == "__main__":
    main()
