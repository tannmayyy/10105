import streamlit as st

# Your app content here
st.title("My Streamlit App")

# Custom CSS to adjust sidebar toggle position
st.markdown(
    """
    <style>
        /* Move sidebar toggle to banner area */
        div[data-testid="stSidebarUserContent"] {
            position: absolute;
            top: -1.5rem;  /* Adjust vertical position */
            left: 10px;    /* Adjust horizontal position */
            z-index: 999;  /* Ensure it's above other elements */
        }

        /* Optional: Customize the hamburger icon color */
        .st-emotion-cache-1cypcdb {
            color: #your_color;
        }

        /* Adjust main content area if needed */
        .st-emotion-cache-1v0mbdj {
            margin-left: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)