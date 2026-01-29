# Question_Answering_and_Text_Summarization
### Project Overview
This project is a Streamlit-based NLP web application that allows users to perform two different natural language processing tasks:
1.	Text Summarization

2.	Question Answering (Q&A)

The user selects the task, enters text into the input box, and the app automatically processes the text using pretrained NLP models.

### Aim of the Project
The aim of this project is to create a simple and user-friendly interface that lets anyone use advanced AI language models without coding.
It helps users:
●	Quickly summarize large text into shorter, meaningful content

●	Ask a question based on a given paragraph and get an accurate answer

●	Run these tasks easily through a clean Streamlit UI

●	Demonstrate how modern NLP models can solve real problems

### Models Used in the Project
The project uses Hugging Face Transformers pipelines with pretrained models:
#### 1. BART (facebook/bart-large-cnn)
Used for text summarization
●	It’s a transformer encoder–decoder model

●	Trained on the CNN/Daily Mail news dataset

●	Can turn long paragraphs into concise summaries

#### 2. DistilBERT / BERT (default model for question-answering pipeline)
Used for extractive question answering
●	The pipeline automatically picks a pretrained QA model (often distilbert-base-cased-distilled-squad)

●	Trained on SQuAD (Stanford Question Answering Dataset)

●	It extracts the most relevant answer from provided text

### How the System Works
Step 1 — User Input
The user selects a task:
●	Summarization → provides a long paragraph

●	Q&A → provides a context + a question

Step 2 — Model Selection
The app loads the appropriate Hugging Face pipeline:
●	Summarizer model for summaries

●	QA model for questions

Step 3 — Processing
●	The text is passed through the transformer model

●	The model analyses the text using learned patterns from training data

●	It generates either:

○	a short summary (for summarization)

○	a specific answer extracted from the context (for Q&A)

Step 4 — Output Display
Streamlit shows the result instantly on the UI:
●	A summary

●	An extracted answer
