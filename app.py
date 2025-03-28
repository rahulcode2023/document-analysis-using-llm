import openai
import os
from flask import Flask, request, jsonify
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from rake_nltk import Rake
from flask_ngrok import run_with_ngrok

# add OpenAI API key here

app = Flask(__name__)
# run_with_ngrok(app)   # This will run the app at http://127.0.0.1:5000/ locally without using ngrok.

# Initialize OpenAI using LangChain's OpenAI wrapper
llm = OpenAI(temperature=0.6, openai_api_key=openai.api_key)

# Function to extract keywords using RAKE
def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()

# Function to summarize the document using LangChain
def summarize_document(document):
    prompt = PromptTemplate(
        input_variables=["document"],
        template="Please summarize the following document:\n{document}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.invoke({"document": document})
    return summary

# Function to extract the topic of the document using LangChain 
def extract_topic(document):
    prompt = PromptTemplate(
        input_variables=["document"],
        template="Please determine the main topic of the following document:\n{document}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    topic = chain.invoke({"document": document})  
    return topic

# Route to handle document input and analyze it
@app.route('/analyze_document', methods=['POST'])
def analyze_document():
    document = request.json.get('document')

    if not document:
        return jsonify({"error": "Document is required"}), 400

    # Step 1: Summarize the document
    summary = summarize_document(document)

    # Step 2: Extract the topic of the document
    topic = extract_topic(document)

    # Step 3: Extract keywords using RAKE
    keywords = extract_keywords(document)

    # Return the analysis results
    return jsonify({
        "summary": summary,
        "topic": topic,
        "keywords": keywords
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True) # Enable debug mode for detailed error messages during development
