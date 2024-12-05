import pandas as pd
import random
import streamlit as st

# Load the Heisman and NFL MVP CSV files
heisman_file_path = "heisman.csv"  # Update with the correct file path for Heisman CSV
nflmvp_file_path = "nflmvp.csv"  # Update with the correct file path for NFL MVP CSV

heisman_data = pd.read_csv(heisman_file_path)
nflmvp_data = pd.read_csv(nflmvp_file_path)

# Convert data to dictionaries for quick lookup
heisman_dict = dict(zip(heisman_data["Year"], heisman_data["Name"]))
nflmvp_dict = dict(zip(nflmvp_data["Year"], nflmvp_data["Name"]))

# Function for Heisman Game
def heisman_game():
    st.title("🎖️ Heisman Trophy Guessing Game")
    st.write("Can you guess the Heisman Trophy winner for the given year? 🤔")
    st.write("Click 'Reset Year' to get a random year and start guessing!")

    # Initialize session state
    if "year" not in st.session_state:
        st.session_state.year = None
    if "score" not in st.session_state:
        st.session_state.score = 0

    # Start a new game
    if st.button("Reset Year"):
        st.session_state.year = random.choice(list(heisman_dict.keys()))
        st.session_state.feedback = ""
    
    if st.session_state.year:
        st.write(f"### Year: **{st.session_state.year}**")
        
        user_input = st.text_input("Enter the winner's name:", value="", key="user_guess")
        if st.button("Submit Guess"):
            correct_answer = heisman_dict[st.session_state.year]
            if user_input.strip().lower() == correct_answer.lower():
                st.session_state.score += 1
                st.session_state.feedback = "✅ Correct! Great job!"
            else:
                st.session_state.feedback = f"❌ Incorrect! The correct answer was **{correct_answer}**."

            st.session_state.year = None  # Reset the year after feedback
        
        st.write(st.session_state.feedback)
            # Display the score
    
    st.write(f"**Score:** {st.session_state.score}")

def nflmvp_game():
    st.title("🎖️ NFL MVP Guessing Game")
    st.write("Can you guess the NFL MVP winner for the given year? 🤔")
    st.write("Click 'Reset Year' to get a random year and start guessing!")

    # Initialize session state
    if "year" not in st.session_state:
        st.session_state.year = None
    if "score" not in st.session_state:
        st.session_state.score = 0

    # Start a new game
    if st.button("Reset Year"):
        st.session_state.year = random.choice(list(nflmvp_dict.keys()))
        st.session_state.feedback = ""
    
    if st.session_state.year:
        st.write(f"### Year: **{st.session_state.year}**")
        
        user_input = st.text_input("Enter the winner's name:", value="", key="user_guess")
        if st.button("Submit Guess"):
            correct_answer = nflmvp_dict[st.session_state.year]
            team = nflmvp_data.loc[nflmvp_data["Name"] == correct_answer, "Tm"].iloc[0]
            if user_input.strip().lower() == correct_answer.lower():
                st.session_state.score += 1
                st.session_state.feedback = "✅ Correct! Great job!  He played for the **{team}**."
            else:
                st.session_state.feedback = f"❌ Incorrect! The correct answer was **{correct_answer}**.  He played for the **{team}**."

            st.session_state.year = None  # Reset the year after feedback
        
        st.write(st.session_state.feedback)
            # Display the score
    
    st.write(f"**Score:** {st.session_state.score}")

# App UI
st.title("🏆 Sports Trophy Guessing Game")

game_option = st.selectbox("Select a game to play:", ["Heisman Trophy", "NFL MVP"])

if game_option == "Heisman Trophy":
    heisman_game()
elif game_option == "NFL MVP":
    nflmvp_game()
