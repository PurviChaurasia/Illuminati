import streamlit as st
#from your_functions import generate_summary, make_mindmap

# Landing Page
st.title("Illuminati")
st.write("Welcome to Illuminati - Your AI Article Summarizer and Mindmap Creator")

# Form Section
st.header("Submit Article URL")
article_url = st.text_input("Enter the URL of the article")
if st.button("Submit"):
    if article_url:
        # Generate Summary
        summary = "This is your summary"
        #generate_summary(article_url)
        
        # Display Summary
        st.header("Summary")
        st.write(summary)
        
        # Generate and Display Mindmap
        st.header("Mindmap")
        #mindmap_html = make_mindmap(summary)
        #st.components.v1.html(mindmap_html, width=700, height=500)
    else:
        st.warning("Please enter the URL of the article.")

