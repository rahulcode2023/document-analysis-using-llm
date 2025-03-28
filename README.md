<<<<<<< HEAD
# Document Analysis for Summary, Topic, and Keyword Extraction
=======
# Document Analysis for Summary, Topic and Keyword Extraction
>>>>>>> bc7dbd9 (updated readme and add app.py)

This is a **Flask**-based application that analyzes documents using **LangChain** and **OpenAI's GPT** model. It provides features such as summarization, sentiment analysis, and keyword extraction.

## Installation for macOS

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rahulcode2023/document-analysis-using-llm.git
   cd document-analysis-using-llm
<<<<<<< HEAD

2. Check Python version: Ensure you're using Python 3:
   ``` python3 --version

3. If Python 3 is not installed, you can install it using Homebrew:
   ``` brew install python3

4. Create and activate a virtual environment:
   ```python3 -m venv venv
      source venv/bin/activate  # For macOS/Linux

5. Install dependencies: Install the required Python packages:
   ``` pip install flask langchain langchain-community transformers rake-nltk flask-ngrok torch openai

6. Set the OpenAI API Key: Set the OPENAI_API_KEY environment variable (for secure access to the API key:
   ``` export OPENAI_API_KEY="your-openai-api-key-here"

## Running the App
Run the Flask application: Start the Flask development server:
   ```python app.py
This will start the Flask development server locally at http://127.0.0.1:5000.

## **Testing the API**
You can test the API using Postman or curl by sending a POST request to: http://127.0.0.1:5000/analyze_document

Example JSON Request for Postman:
``` {
      "document": "The global economy is facing significant challenges as inflation continues to rise in many countries. The ongoing pandemic has led to disruptions in the supply chain, making it difficult for businesses to meet consumer demand. On top of that, geopolitical tensions and the rise of energy costs are adding further strain. In particular, the tech industry has been heavily impacted by these issues, with many companies adjusting their strategies to adapt to the new environment. As businesses navigate these challenges, government intervention may be necessary to stabilize the economy and ensure continued growth."
   }

Example curl Command:
You can also use curl to test the endpoint directly:

```curl -X POST http://127.0.0.1:5000/analyze_document \
      -H "Content-Type: application/json" \
      -d '{"document": "The global economy is facing significant challenges as inflation continues to rise in many countries. The ongoing pandemic has led to disruptions in the supply chain, making it difficult for businesses to meet consumer demand. On top of that, geopolitical tensions and the rise of energy costs are adding further strain. In particular, the tech industry has been heavily impacted by these issues, with many companies adjusting their strategies to adapt to the new environment. As businesses navigate these challenges, government intervention may be necessary to stabilize the economy and ensure continued growth."}'

This will help you verify if the server is running properly and responding as expected.

## **Stopping the Flask Server**
To stop the Flask server running locally, press Ctrl+C in the terminal where the Flask application is running.
=======
2. Check Python version: Ensure you're using Python 3:
   ```bash
   python3 --version
3. If Python 3 is not installed, you can install it using Homebrew:
   ```bash 
   brew install python3
4. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For macOS/Linux
5. Install dependencies: Install the required Python packages:
   ```bash 
   pip install flask langchain langchain-community transformers rake-nltk flask-ngrok torch openai
6. Set the OpenAI API Key: Set the OPENAI_API_KEY environment variable (for secure access to the API key:
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"

## Running the App
7. Run the Flask application: Start the Flask development server:
   ```bash
   python app.py
This will start the Flask development server locally at http://127.0.0.1:5000.
.

## Testing the API
8. You can test the API using Postman or curl by sending a POST request to: http://127.0.0.1:5000/analyze_document

   Example JSON Request for Postman:
   ```bash
    {
         "document": "The global economy is facing significant challenges as inflation continues to rise in many countries. The ongoing pandemic has led to disruptions in the supply chain, making it difficult for businesses to meet consumer demand. On top of that, geopolitical tensions and the rise of energy costs are adding further strain. In particular, the tech industry has been heavily impacted by these issues, with many companies adjusting their strategies to adapt to the new environment. As businesses navigate these challenges, government intervention may be necessary to stabilize the economy and ensure continued growth."
      }

   Example curl Command:
   You can also use curl to test the endpoint directly:

   ```bash 
   curl -X POST http://127.0.0.1:5000/analyze_document \
         -H "Content-Type: application/json" \
         -d '{"document": "The global economy is facing significant challenges as inflation continues to rise in many countries. The ongoing pandemic has led to disruptions in the supply chain, making it difficult for businesses to meet consumer demand. On top of that, geopolitical tensions and the rise of energy costs are adding further strain. In particular, the tech industry has been heavily impacted by these issues, with many companies adjusting their strategies to adapt to the new environment. As businesses navigate these challenges, government intervention may be necessary to stabilize the economy and ensure continued growth."
   }'

This will help you verify if the server is running properly and responding as expected.

## Stopping the Flask Server
11. To stop the Flask server running locally, press `Ctrl+C` in the terminal where the Flask application is running.
>>>>>>> bc7dbd9 (updated readme and add app.py)

