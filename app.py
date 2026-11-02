
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")

# NASA APOD API URL
API_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/"

# Streamlit page configuration
st.set_page_config(
    page_title="NASA Space Astronomy",
    page_icon="🌌"
)

# Application title
st.title("🌌 NASA Space Astronomy")
st.write("Explore NASA's Astronomy Picture of the Day!")

# Select a date
selected_date = st.date_input("Choose a date")

# Explore button
if st.button("Explore"):

    if not API_KEY:
        st.error("NASA API key not found. Check your .env file.")

    else:
        params = {
            "api_key": API_KEY,
            "date": selected_date.isoformat()
        }

        try:
            # Send request to NASA API
            response = requests.get(
                API_URL,
                params=params,
                timeout=20
            )

            response.raise_for_status()
            data = response.json()

            # Handle list response
            if isinstance(data, list):
                if len(data) == 0:
                    st.error("No astronomy picture found for this date.")
                    st.stop()

                data = data[0]

            # Display astronomy information
            st.subheader(data["title"])
            st.write("Date:", data["date"])
            st.write(data["explanation"])

            # Display image or video
            if data["media_type"] == "image":
                st.image(data["hdurl"], width="stretch")

            elif data["media_type"] == "video":
                st.write("This APOD is a video.")
                st.link_button("Watch on NASA", data["permalink"])

        except requests.exceptions.RequestException as error:
            st.error(f"NASA API connection error: {error}")

        except (KeyError, ValueError, IndexError, TypeError):
            st.error("The NASA API returned an unexpected response.")
