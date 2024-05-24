# Flask Web App

This is a sample web app using the Flask Python module. The app utilizes the Azure AI Translator API to translate user text to multiple languages.

## Dependencies

To run this web app, you'll need to set up a virtual environment and install the following dependencies:

- Flask
- Azure Translator Text

## Setting up a Virtual Environment

1. Open a terminal and navigate to the project directory:


2. Create a virtual environment:
    ```
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - For macOS/Linux:
      ```
      source venv/bin/activate
      ```
    - For Windows:
      ```
      venv\Scripts\activate
      ```

4. Install the dependencies:
    ```
    pip3 install -r requirements.txt
    ```

 ## Updating the .env File
Update the .env file with the appropriate values from the Azure Translator resource.
  
## Running the Web App

1. Make sure your virtual environment is activated.

2. Start the Flask development server:
    ```
    flask run
    ```

3. Open your web browser and navigate to `http://localhost:5000` to access the web app.

