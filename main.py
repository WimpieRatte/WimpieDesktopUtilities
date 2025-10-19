import streamlit as st
from wimpielibrary.my_string_stuff import replace_numbers_preserve_length
# from app_content import content as c

st.title("Wimpie Desktop Utilities")

with st.form("my_form"):
    st.subheader('Randomise things')

    numbers_to_randomise = st.text_input("Randomise the numbers")

    submitted = st.form_submit_button("Submit")

if submitted:
    #st.write(number_to_randomise)
    randomised_numbers = replace_numbers_preserve_length(numbers_to_randomise)
    st.markdown(f"New number: {randomised_numbers}")
else:
    st.write("Please submit")