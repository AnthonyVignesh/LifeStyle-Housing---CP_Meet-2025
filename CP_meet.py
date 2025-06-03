
import streamlit as st

st.set_page_config(page_title="Event Registration", layout="centered")

st.title("📝 Event Registration Form")

# Registration Type
registration_type = st.selectbox("Registration Type", ["Individual", "Company"])

# Dynamic label for name field
name_label = "Full Name" if registration_type == "Individual" else "Company Name"
full_name = st.text_input(name_label, placeholder=f"Enter your {name_label.lower()}")

# Number of Guests
guest_count = st.number_input("Number of Guests", min_value=0, max_value=10, step=1)

# Guest Details with Name & Mobile
guest_info = []
if guest_count > 0:
    st.subheader("Guest Details")
    for i in range(guest_count):
        col1, col2 = st.columns(2)
        with col1:
            guest_name = st.text_input(f"Guest {i+1} Name", key=f"guest_name_{i}")
        with col2:
            guest_mobile = st.text_input(f"Guest {i+1} Mobile", key=f"guest_mobile_{i}")
        guest_info.append({"name": guest_name, "mobile": guest_mobile})

# Submit Button
if st.button("Submit"):
    if not full_name:
        st.error(f"Please enter your {name_label.lower()}.")
    else:
        st.success("✅ Registration Submitted Successfully!")
        st.write("### 📄 Registration Summary")
        st.write(f"**{name_label}:** {full_name}")
        st.write(f"**Registration Type:** {registration_type}")
        
        if guest_info and any(g['name'] for g in guest_info):
            st.write("**Guest Details:**")
            for i, guest in enumerate(guest_info, start=1):
                if guest['name'] or guest['mobile']:
                    st.write(f"{i}. Name: {guest['name']} | Mobile: {guest['mobile']}")
        else:
            st.write("No guests registered.")
