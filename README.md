# AI Interview Chatbot

This is an AI-powered interview chatbot named **Monika**, designed to conduct interviews for the **Frontend Developer** role. It follows a structured decision tree to navigate conversations and assess candidates based on predefined conditions.

## Features
- Loads a **tree-based conversation structure** from a JSON file.
- Uses **Gemini 2.0 Flash** from Google Generative AI for intelligent responses.
- Evaluates user input conditions to **progress through interview steps**.
- **Handles user responses dynamically** based on predefined conditions.
- Includes a **conversation history** for tracking interactions.
- The **user interface** is built using **Streamlit** for a seamless and interactive experience.
- The app is deployed using **Vercel** for easy access and scalability.

## Prerequisites
- Python 3.8+
- API key for **Google Generative AI** (stored in `.env`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/ai-interview-chatbot.git
   cd ai-interview-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your **Google API key**:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
4. Add a **tree.json** file defining the interview conversation structure.

## Usage
Run the chatbot with:
```bash
python chatbot.py
```

## Project Structure
```
├── chatbot.py         # Main chatbot script
├── tree.json          # JSON structure defining the conversation tree
├── .env               # Environment file for storing API keys
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
```

## Example Tree Structure (tree.json)
```json
[
    {
        "nodeId": "node1",
        "rootNode": true,
        "prompt": "Ask if the user is John",
        "edges": [
            {
                "condition": "user is John",
                "targetNodeId": "node2"
            },
            {
                "condition": "user is not John",
                "targetNodeId": "node8"
            }
        ]
    }
]
```

## Notes
- The chatbot **strictly follows the decision tree**.
- It **does not generate additional questions** outside the structure.
- Debugging logs are enabled to track conditions and responses.

## Outputs

## 1. User is John and Ready

![alt text](image.png)

## 2. User is John but Not Ready

![alt text](image-1.png)

## 3. User is not John

![alt text](image-2.png)


## License
MIT License
