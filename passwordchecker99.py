import re
import streamlit as st

#page styling
st.set_page_config(page_title="password Strength",page_icon="😇",layout="centered")
# custum css
st.markdown(
    """
<style>
.main {text-align:center; }
.stTextInput {width: 60% !important; margin:auto; }
.stButton button {width: 50%; background-color #4CAF50;color: white; font-size:18px; }
.stButton button:hover { background-color: #4a049; }
</style>
""",unsafe_allow_html=True)

# page title and descriptions
st.title(" 🔐 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔍")

#  function to check password strength
def check_password_streangth(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1 #increase score by 1
    else:
        feedback.append("❌  password should be  **atleast 8 character long**.")
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ password should inculde **both uppercase (A-Z) and lowercase (a-z) letters**.") 
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ password should include **atleast one digit (0-9)**.")
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ include **atleast one special character (!@#$%^&*)**.")

    # display password strength results    # 
    if score == 4:
        st.success("✔️ **Strong Password ** -  Your Password is Secure**.")
    elif score == 3:
        st.info("**Moderate password** = Consider improving  security by adding more feature**")

    else:
        st.error("❌ **Week Password** - Follow the suggestion below to strength it.")
        # display feedback
    if feedback:
        with st.expander(" ** Improve Your Password** "):
            for item in feedback:
               st.write(item)
password = st.text_input("Enter Your password:", type="Password", help="Ensure your password is strong 🔐")

# button working
if st.button("Check Password Strength"):
    check_password_streangth(password)
else:
     st.warning("  ⚠️ Please enter a password first!") #show warning  if password empty



