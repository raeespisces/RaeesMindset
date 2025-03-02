import streamlit as st
import random

st.set_page_config(page_title="Growth Mindset Project", page_icon="🌱")
st.title("Growth Mindset AI Project")

st.header("Welcome to Your Growth Journey")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements!")

# Quote section
st.header("Today's Growth Mindset Quote")
quotes = [
    "Success is not an accident, success is a choice.",
    "Mistakes are proof that you are trying.",
    "A journey of a thousand miles begins with a single step.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Growth and comfort do not coexist.",
]
st.write(random.choice(quotes))

# Reflection Section
st.header("Daily Reflection")
reflection = st.text_area("What did you learn today that challenged you?")
if st.button("Save Reflection"):
    st.success("Reflection saved! Keep growing!")

# Challenge Yourself Section
st.header("Challenge Yourself")
challenges = [
    "Try learning something completely new today!",
    "Step outside your comfort zone and take on a new task.",
    "Practice gratitude by writing down three things you're grateful for.",
    "Turn a mistake into a learning opportunity.",
    "Encourage someone else to adopt a growth mindset.",
]
st.write(random.choice(challenges))

# Progress Tracking
st.header("Track Your Progress")
progress = st.slider("How do you rate your growth mindset today?", 1, 10, 5)
st.write(f"You rated your growth mindset as {progress}/10 today. Keep improving!")
