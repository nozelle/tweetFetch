import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image

# Function to extract image and tweet text from the Twitter link using web scraping
def extract_tweet_info(tweet_url):
    try:
        response = requests.get(tweet_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            tweet_text = soup.find('div', {'class': 'tweet-text'}).text.strip()
            media_element = soup.find('div', {'class': 'AdaptiveMedia-photoContainer'})
            if media_element:
                media_url = media_element.find('img')['src']
                image_response = requests.get(media_url)
                image = Image.open(BytesIO(image_response.content))
                return tweet_text, image
            else:
                return tweet_text, None
        else:
            st.error("Failed to fetch tweet. Please check the URL.")
            return None, None
    except requests.exceptions.RequestException as e:
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
