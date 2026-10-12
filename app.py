import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")
st.title("Number Guessing App! 🎮")
st.write("I'm thinking of a number between 1 and 10.")

# Initialize Session State
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 3
    st.session_state.game_over = False
    st.session_state.message = ""

# Show the feedback message from the previous guess
if st.session_state.message:
    if "Congratulations" in st.session_state.message:
        st.success(st.session_state.message)
        st.balloons()
    elif "Game over" in st.session_state.message:
        st.error(st.session_state.message)
    else:
        st.warning(st.session_state.message)

# The Game Interface
if not st.session_state.game_over:
    st.write(f"**You have {st.session_state.attempts} guesses left.**")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)
    
    if st.button("Submit Guess"):
        # Set the feedback message instead of printing it directly
        if guess == st.session_state.secret_number:
            st.session_state.message = f"🎉 Congratulations! You guessed it! The number was {st.session_state.secret_number}."
            st.session_state.game_over = True
            
        elif guess < st.session_state.secret_number:
            st.session_state.message = "Too low!"
            st.session_state.attempts -= 1
            
        else:
            st.session_state.message = "Too high!"
            st.session_state.attempts -= 1
            
        if st.session_state.attempts == 0 and not st.session_state.game_over:
            st.session_state.message = f"Game over! The secret number was {st.session_state.secret_number}."
            st.session_state.game_over = True
            
        # Refresh the page to update the attempts counter and show the saved message
        st.rerun()

# Restart Button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, 10)
        st.session_state.attempts = 3
        st.session_state.game_over = False
        st.session_state.message = ""
        st.rerun()