import streamlit as st
from transformers import pipeline

st.title("📘 Text Summarization & Q&A App")

task = st.radio("Choose an option:", ["Text Summarization", "Q&A"])

if task == "Text Summarization":
    text = st.text_area("Enter text to summarize:")

    if st.button("Summarize"):
        if text.strip():
            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
            st.write(summary[0]["summary_text"])
        else:
            st.warning("Please enter some text.")

else:
    context = st.text_area("Enter context text:")
    question = st.text_input("Enter your question:")

    if st.button("Answer"):
        if context.strip() and question.strip():
            qa = pipeline("question-answering")
            answer = qa(question=question, context=context)
            st.write(answer["answer"])
        else:
            st.warning("Please provide both context and question.")
