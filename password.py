# ASSIGNMENT 3
# PASSWORD STRENGHT METER

import streamlit as st
import re

# Web App Title
st.title("🔒 Password Strength Checker")

# User Input
password = st.text_input("Enter a password:", type="password")

# Function to check password strength
def check_password_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"\d", password):
        strength += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")

    return strength, suggestions

# Checking Password Strength
if password:
    strength, suggestions = check_password_strength(password)

    if strength == 4:
        st.success("✅ Strong Password")
    elif strength == 3:
        st.warning("⚠️ Moderate Password")
    else:
        st.error("❌ Weak Password")

    # Show suggestions if password is weak
    if suggestions:
        st.write("🔹 **Suggestions to Improve:**")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")

