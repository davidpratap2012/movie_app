import os
import streamlit as st
import openai

# Load the OpenAI API key from environment variable
#openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI(api_key='sk-proj-YRGsUarSsoN3AUir5Yp8T3BlbkFJ2fNDvpG1CqdAlIRN2onj')

# Function to get movie recommendations from GPT-3.5/4
def get_movie_recommendations(prompt):
    try:
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can replace with "gpt-4" if available
            messages=messages,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        #recommendations = response.choices[0].text.strip()
        recommendations=response.choices[0].message.content
        return recommendations
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app interface
st.title("Movie Recommender")

st.write("Enter a movie name or genre to get recommendations:")

input_text = st.text_input("Movie/Genre", "")

if st.button("Get Recommendations"):
    if input_text:
        prompt = f"Provide a list of 10 movies recommended for someone who likes {input_text}."
        recommendations = get_movie_recommendations(prompt)
        st.write("Here are some movie recommendations for you:")
        st.write(recommendations)
    else:
        st.write("Please enter a movie name or genre.")
