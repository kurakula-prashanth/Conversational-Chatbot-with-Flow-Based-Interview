# CSS styles for the application

def load_css():
    """Return the CSS styles for the application"""
    return """
    <style>
    .main {
        background-color: #0f1119; /* Dark background for the app */
    }
    .stTextInput>div>div>input {
        padding: 12px;
        font-size: 16px;
        background-color: #1e212e;
        color: white;
        border: 1px solid #333;
    }
    .chat-message {
        padding: 15px 15px 15px 35px; /* Increased left padding to make room for the arrow */
        border-radius: 10px;
        margin-bottom: 10px;
        display: flex;
        align-items: flex-start;
        position: relative;
        box-shadow: 0 3px 8px rgba(0,0,0,0.3);
    }
    .chat-message.user {
        background-color: #1a1f35; /* Dark blue background */
        border-left: 5px solid #0088ff; /* Bright blue border */
        color: #e6f7ff; /* Light blue text */
    }
    .chat-message.bot {
        background-color: #2d1a35; /* Dark purple background instead of green */
        border-left: 5px solid #9933ff; /* Bright purple border */
        color: #f2e6ff; /* Light purple text */
    }
    .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        object-fit: cover;
        margin-right: 10px;
    }
    /* Bright colored indicators with fixed positioning */
    .chat-message.user:before {
        content: "►";
        position: absolute;
        left: 10px;
        top: 15px; /* Align with the start of text */
        color: #0088ff; /* Bright blue for user indicator */
        font-weight: bold;
        font-size: 18px;
    }
    .chat-message.bot:before {
        content: "◄";
        position: absolute;
        left: 10px;
        top: 15px; /* Align with the start of text */
        color: #9933ff; /* Bright purple for bot indicator */
        font-weight: bold;
        font-size: 18px;
    }
    /* Names styling */
    .chat-message b {
        color: #00ddff; /* Bright cyan for user name */
        font-size: 15px;
        margin-right: 10px; /* Add space after the name */
        display: inline-block; /* Keep on same line */
    }
    .chat-message.bot b {
        color: #cc99ff; /* Light purple for bot name */
    }
    /* Message content styling */
    .chat-message-content {
        display: inline; /* Keep content on same line as name */
    }
    /* Send button styling */
    .stButton>button {
        background-color: #ff3b5c !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
        box-shadow: 0 3px 6px rgba(255,59,92,0.4) !important;
    }
    /* Reset button styling */
    .stButton:nth-of-type(2)>button {
        background-color: #333 !important;
        color: white !important;
        border: 1px solid #666 !important;
        box-shadow: none !important;
    }
    </style>
    """