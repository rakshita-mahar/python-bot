import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Classic"},
    {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
    {"title": "The Fault in Our Stars", "author": "John Green", "genre": "Romance"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    {"title": "Harry Potter", "author": "J.K. Rowling", "genre": "Fantasy"},
]

def preprocess_input(text):
  tokens = word_tokenize(text.lower())
  stop_words = set(stopwords.words("english"))
  tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
  return tokens

def recommend_books(preferences):
  recommendations = []
  for book in books:
    if any(pref in book["genre"].lower() for pref in preferences):
      recommendations.append(book)
    elif any(pref in book["title"].lower() for pref in preferences):
      recommendations.append(book)
  return recommendations

def main():
    st.title("Book Recommendation Chatbot 📚")
    st.write("Tell me what kind of books you like, and I'll recommend something for you!")

    user_input = st.text_input("Enter your preferences (e.g., 'fantasy', 'romance', or a specific title):")
    if st.button("Get Recommendations"):
        if user_input:
            try:
                preferences = preprocess_input(user_input)
                recommendations = recommend_books(preferences)
                if recommendations:
                    st.success("Here are some recommendations:")
                    for book in recommendations:
                        st.write(f"📖 *{book['title']}* by {book['author']} (Genre: {book['genre']})")
                else:
                    st.warning("Sorry, I couldn't find any recommendations based on your preferences.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter your preferences!")
if __name__ == "_main_":
   main()