

![My first design (1) (1)](https://github.com/ArchismwanChatterjee/demo/assets/115975340/29f321e6-110a-4134-b37c-12053e2ff2fc)


# VoiceGenius : A new way to interact with AI

![License](https://badgen.net/github/license/micromatch/micromatch)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

VoiceGenius is a voice based GPT where the user will be able to ask questions using their voice. The output will be available in both audio and text format. Also it features the functionality where the user will be able to download the conversion.

Check out the demo [here](https://www.youtube.com/watch?v=5EmjwMVLDiE&t=12s)


## How to use:
1. Go through the disclaimer ⚠️ and imp information for best results.
2. Click on START to start the gpt
3. Ask any question of your choice
4. Wait for the question to be detected and it will be updated
5. Wait a bit for output generation and See the ✨Magic ✨ Happen
6. Like this the process will continue if you want to STOP then simply click on STOP after that if you feel like you can download the file


## Installation:

- clone this repository

- VoiceGenius requires [Python](https://www.python.org/) v3.9+ to run.

- Install the dependencies.

```python
pip install -r requirements.txt
```

- Make sure to create your own generative-ai api-key using Google Cloud Console or Google Makersuite and replace it.

```python
genai.configure(api_key=os.getenv("MY_SECRET_KEY")) # Replace with your own api-key by creating .env file
```
or 
```python
genai.configure(api_key="YOUR APIKEY")  # Replace YOUR APIKEY with the actual value of your apikey 
```

- To run the server
```python
streamlit run "your_file_name"
```

- For Deploying your application refer [Streamlit Community Cloud](https://docs.streamlit.io/streamlit-community-cloud/get-started)

## Development:

Want to contribute? Great!

VoiceGenius uses streamlit and other python libraries.

checkout *Installation* above to set it up locally.

make sure all changes you make are in the testing branch. 
