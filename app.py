import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")
st.title("Number Guessing App! 🎮")
st.write("I'm thinking of a number between 1 and 10.")

# Initialize Session State to remember values between clicks
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 3
    st.session_state.game_over = False

# The Game Interface
if not st.session_state.game_over:
    st.write(f"**You have {st.session_state.attempts} guesses left.**")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)
    
    if st.button("Submit Guess"):
        if guess == st.session_state.secret_number:
            st.success(f"🎉 Congratulations! You guessed it! The number was {st.session_state.secret_number}.")
            st.balloons()
            st.session_state.game_over = True
            
        elif guess < st.session_state.secret_number:
            st.warning("Too low!")
            st.session_state.attempts -= 1
            
        else:
            st.warning("Too high!")
            st.session_state.attempts -= 1
            
        if st.session_state.attempts == 0 and not st.session_state.game_over:
            st.error(f"Game over! The secret number was {st.session_state.secret_number}.")
            st.session_state.game_over = True
            
        st.rerun()

# Restart Button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, 10)
        st.session_state.attempts = 3
        st.session_state.game_over = False
        st.rerun()