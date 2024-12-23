# Code Summarizer Project Documentation

## Overview
The Code Summarizer is a web application that allows users to input code either through direct text input or by uploading a file. The application utilizes the Langchain library and Google Gemini LLM to generate concise summaries of the provided code, making it easier for users to understand the purpose and functionality of the code.

## Features
- **Input Method Selection**: Users can choose to input code directly or upload a file.
- **Code Summarization**: The application generates a human-readable summary of the code.
- **User Friendly Interface**: Built with Bootstrap for a responsive design.
- **Markdown Support**: Summaries are formatted in Markdown for better readability.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python, Flask
- **AI Model**: Langchain with Google Generative AI
- **Environment Management**: dotenv for loading environment variables

## File Structure

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/gulshan-100/AI_Code_Summarizer
   cd AI_Code_Summarizer
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory and add your environment variables as needed.

4. Run the application:
   ```
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage
1. Select the input method (Direct Text Input or File Upload).
2. If using Direct Text Input, paste your code into the text area.
3. If using File Upload, select a file containing your code.
4. Click the "Summarize Code" button to generate the summary.
5. The summary will be displayed on the right side of the interface.

## Error Handling
- If no code is provided, the application will return an error message indicating that no code was submitted.
- Any exceptions during processing will return a generic error message.

