import streamlit as st
import random
import string

# Common passwords blacklist
common_password = ["password", "password123", "123456", "qwerty", "admin"]

# Custom scoring weights
weights = {
    "length" : 0.3,
    "uppercase" : 0.2 ,
    "lowercase" : 0.2 ,
    "digits" : 0.2 ,
    "special_chars" : 0.1,
}

# Function to check if password is in the blacklist
def is_blacklisted(password):
    return password.lower() in common_password

# Function to calculate password strength
def calculate_strength(password):
    if is_blacklisted(password):
        return 0 , "Password is too common"
    score = 0

    if len(password)>= 8 :
        score += weights["length"]

            # Uppercase letters
    if any(c.isupper() for c in password):
        score += weights["uppercase"]

        # Lowercase letters
    if any(c.islower () for c in password):
        score +=weights["lowercase"]

          # Digits
    if any(c.isdigit() for c in password):
        score +=weights["digits"]
        # Special characters
    if any(c in string.punctuation for c in password):
        score += weights["special_chars"]

        # Normalize score to 0-100

    strength = int(score*100)
    if strength<40:
        return strength, "Weak"
    elif strength<70:
        return strength, "Moderate"
    else:
        return strength, "Strong"
    
# Function to generate a strong password
def gen_password(length = 16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI
def main():
    st.title("PASSWORD STRENGTH METER & GENERATOR")

    #Password Input

    password = st.text_input("Enter password to check strength:", type="password")

    if password:
        strength , feedback = calculate_strength(password)
        st.write(f"Passsword Strength : {strength} / 100 - {feedback}")

    #password generator

    if st.button("Generate Password"):
        gen_password = gen_password()
        st.write(f"Genrated Password : {gen_password}")

    # Custom weights adjustment

    st.sidebar.header = ("Custome Scoring Weights")
    weights["length"] = st.sidebar.slider("Length Weight" , 0.0 , 1.0, weights["length"])
    weights["uppercase"] = st.sidebar.slider("Uppercase Weight" , 0.0 , 1.0, weights["uppercase"])
    weights["lowercase"] = st.sidebar.slider("Lowercase Weight" , 0.0 , 1.0, weights["lowercase"])
    weights["digits"] = st.sidebar.slider("Digits Weight" , 0.0 , 1.0, weights["digits"])
    weights["special_chars"] = st.sidebar.slider("Special Characters Weight" , 0.0 , 1.0, weights["special_chars"])
    


if __name__ == "__main__":
    main()
