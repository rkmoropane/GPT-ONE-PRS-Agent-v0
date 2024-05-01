# ABOUT THIS AI AGENT PROJECT:
__
WORKING ON AGENTS CODE

### Objective: The objective of this project is to create an AI agent.

### Project Instructions:
PRS:
1. Requirements:
- It must be written in python using OOP
- It must customizable using a config variable (dictionary)
  * model(use more than just openai llm, even local)
  * tools
  * behavior
  * response format: image/text/json/...
  * ...
- can be configured from conversation to task completion via config variable:
  * conversation agent: involved in a conversation style with context and based on set behavior, can also take in context
  * task driven agent: given a task, it must take all necessary steps to complete that task
- multimodal agent: handle files: text/image/audio
- can work with other angents

2. Constrains:
- must be called from a single object(might have many object in it)
- must be a single script without importing from local script (other libraries acceptable)
- ...
__

### Prerequisites

- Python 3.x
- Rquired Modules: which is in the requirements.txt file ready for installation

### File Structure

├── README.md
├── requirements.txt
├── .gitignore
└── agent.py

### Installation and Setup

- Create a virtual environment:
 * `python -m venv myenv`

- Navigate into your virtual env:
 * `cd myenv`

- Activate the virtual environment:
 * On Windows:
    `.\Scripts\activate`

 * On macOS/Linux:
    `source bin/activate`

- Clone this repository to your local machine.
 * `git clone https://github.com/rkmoropane/GPT-ONE-PRS-Agent-v0.git`

- Navigate to the repo.
 * `cd GPT-ONE-PRS-Agent-v0/`

- Install dependencies:
 * `pip install -r requirements.txt`

- Install the setup.py file to import the get_pull_requests function as a module
 * `python setup.py develop`


### Add OPENAI API KEY & SERPER API KEY:
- Create a new shell script and name it `credentials.sh`. In this script, you will define the secret environment variable `OPENAI_API_KEY` and `SERPER_API_KEY` and store them within it. 
- Copy and paste the following contents into your shell script:
```
#!/bin/sh

export OPENAI_API_KEY='your_generated_openai_api_key_here'
export SERPER_API_KEY='your_generated_serper_api_key_here'

# include your current working directory below:
export PYTHONPATH=/path/from/home/to/GPT-ONE-PRS-Agent-v0:$PYTHONPATH
```

- Create your [OpenAI account](https://platform.openai.com) and Generate a OPENAI API KEY from your OpenAI API Keys [settings](https://platform.openai.com/api-keys), copy the key and paste it into your shell file.

- Create your [Serper account](https://serper.dev/) and Generate a SERPER API KEY from your Serper API Keys [settings](https://serper.dev/api-key), copy the key and paste it into your shell file.

- Run your shell script:
 * for permisssions:
    `chmod +x credentials.sh`  
 * run it:
    `source credentials.sh`
    
### Run your python script in the terminal:
- `python app.py`

### Author
Kholofelo Moropane

kholofelo@fcb.ai
License
Copyright © 2024 Kholofelo Moropane.
