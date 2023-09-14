# Import the necessary library and modules
import streamlit as st
from datetime import datetime

# Set the title and description for the Streamlit app
st.title("Simple Social Media Feed")
st.write("Welcome to the social media feed! Share your posts below.")

# Define a function to load existing posts from a file
def load_posts():
    try:
        # Attempt to open and read posts from "posts.txt" file
        with open("posts.txt", "r") as file:
            # Read each line, strip newline characters, and store in a list
            posts = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list
        posts = []
    return posts

# Define a function to save posts to a file
def save_posts(posts):
    with open("posts.txt", "w") as file:
        # Write each post to the "posts.txt" file followed by a newline character
        for post in posts:
            file.write(post + "\n")

# Load existing posts from the file
posts = load_posts()

# Create a text input box for the user to enter their post
# The user_post stores the information of the post written by the user
user_post = st.text_area(label="Share your post:")

# Create a button for the user to submit their post
if st.button("Post"):
    if user_post:
        # Get the current timestamp in the format "YYYY-MM-DD HH:MM"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        # Create a new post with the timestamp and user's input
        new_post = f"Posted on {timestamp} {user_post}"
        # Append the new post to the list of posts
        posts.append(new_post)
        # Save the updated list of posts to the file
        save_posts(posts)
        # Give a success message stating post has been approved/posted 
        st.success("Posted Successfully")

# Refresh Button to Refresh the UI
st.button("Refresh")

# Display the feed
st.text("Feed:")
for post in posts:
    # To remove unwanted spacing
    post = post.strip()
    # Split each post into parts using whitespace
    post_breakdown = post.split()
    # Display the post content (excluding the timestamp) followed by a separator
    st.write(' '.join(post_breakdown[4:]))
    # Display the timestamp and user who posted the content
    st.write('-' + ' '.join(post_breakdown[:4]))


