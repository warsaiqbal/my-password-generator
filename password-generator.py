import streamlit as st
import random
import string

st.title("Password Generator")

length = st.slider("Password Length", min_value=8, max_value=32, value=12)

include_uppercase = st.checkbox("Include Uppercase Letters")
include_lowercase = st.checkbox("Include Lowercase Letters", value=True)
include_numbers = st.checkbox("Include Numbers", value=True)
include_special_chars = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
        
    if not characters:
        st.error("Please select at least one character type")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        st.success("Generated Password: " + password) 