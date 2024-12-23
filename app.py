from flask import Flask, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
import os
from dotenv import find_dotenv, load_dotenv
from markdown import markdown

# Load environment variables
load_dotenv(find_dotenv())


app = Flask(__name__)

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.3,
)

# Create prompt template for code summarization
summarize_prompt = PromptTemplate(
    input_variables=["code"],
    template="""
    You are an advanced AI assistant skilled in summarizing code. Your task is to analyze the
    input code provided and generate a concise, clear, and human-readable summary that explains 
    the purpose and functionality of the code. Your summary should be beginner-friendly but 
    also informative for experienced developers. Avoid including unnecessary details such as 
    specific variable names unless they are critical to understanding the code.

    Instructions:

    Identify the programming language of the code.
    Explain the purpose of the code or function.
    Describe the main logic and flow of the code concisely.
    Highlight any notable algorithms, design patterns, or libraries used.

    Code:
    {code}

    Summary:
    
    """
)

# Create the chain
summarize_chain = LLMChain(llm=llm, prompt=summarize_prompt)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_code():
    try:
        input_type = request.form.get('input_type')
        
        if input_type == 'text':
            code = request.form.get('code')
        else:  # file input
            file = request.files['file']
            code = file.read().decode('utf-8')
        
        # Validate input
        if not code or len(code.strip()) == 0:
            return jsonify({
                'error': 'No code provided'
            }), 400
        
        # Generate summary using Langchain
        summary = summarize_chain.run(code)
        
        # Wrap the summary in asterisks for emphasis
        formatted_summary = f"**{summary}**"
        
        # Convert Markdown to HTML
        html_summary = markdown(formatted_summary)
        
        return jsonify({
            'summary': html_summary
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)