import json
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from config import MODEL_NAME, TREE_PATH

class ChatbotBackend:
    def __init__(self, tree_path=TREE_PATH):
        """
        Initialize the chatbot with the tree structure and LLM.
        """
        self.tree = self.load_tree(tree_path)
        self.llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME, 
            temperature=0, 
            max_tokens=None, 
            timeout=None, 
            max_retries=2
        )
        
    def load_tree(self, path):
        """
        Load and parse the JSON tree structure.
        """
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            st.error(f"Error: File '{path}' not found.")
            return []
        except json.JSONDecodeError:
            st.error(f"Error: Invalid JSON in '{path}'.")
            return []

    def find_root_node(self):
        """
        Find and return the root node of the tree.
        """
        for node in self.tree:
            if node.get("rootNode", False):
                return node
        st.error("Error: No root node found in the tree.")
        return None
        
    def get_node_by_id(self, node_id):
        """Get a node by its ID"""
        return next((n for n in self.tree if n["nodeId"] == node_id), None)

    def generate_response(self, prompt, history):
        """
        Generate a chatbot response using the LLM with both prompt and history.
        """
        system_prompt = f"""
        You are Monika, an AI interviewer for the Frontend Developer role.
        Use the conversation history and the current prompt to generate a short, clear response.
        
        **Conversation History**: {history}
        **Current Prompt**: {prompt}
        """
        try:
            response = self.llm.invoke(system_prompt)
            return response.content.strip()
        except Exception as e:
            return f"Error generating response: {str(e)}"

    def evaluate_condition(self, current_node_prompt, user_input, condition):
        """
        Evaluate if the user's input matches a condition using the LLM.
        """
        if condition == "always proceed":
            return True  # Automatically proceed without user input
        elif condition == "user provides any answer":
            return True  # Accept any user input

        condition_eval_prompt = f"""
        The chatbot previously asked: "{current_node_prompt}".
        Does the user's response below mean "{condition}"?  

        User Input: "{user_input}"  

        Answer ONLY 'yes' or 'no'. Do NOT explain.
        """
        try:
            response = self.llm.invoke(condition_eval_prompt)
            return "yes" in response.content.lower()
        except Exception:
            return False