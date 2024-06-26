import streamlit as st
from summarize_text import scrape_text, summarize_text
from create_mindmap import generate_markmap
from streamlit_markmap import markmap

st.title("Illuminati")
st.write("Welcome to Illuminati - Your AI Article Summarizer and Mindmap Creator")

st.header("Submit Article URL")
article_url = st.text_input("Enter the URL of the article")

if st.button("Submit"):
    if article_url:
        text = scrape_text(article_url)
        summary = summarize_text(text)
        
        # Display Summary
        st.header("Summary")
        st.write(summary)
        
        # Generate and Display Mindmap
        st.header("Mindmap")
        data = generate_markmap(text)
        markmap(data, height=400)
    else:
        st.warning("Please enter the URL of the article.")

