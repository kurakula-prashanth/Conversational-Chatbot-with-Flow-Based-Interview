import streamlit as st

def display_message(sender, message):
    """Add a message to the chat history"""
    if sender == "AI":
        st.session_state.history.append({"AI": message})
    else:
        st.session_state.history.append({"User": message})

def display_chat_history():
    """Display the chat history with styled messages"""
    for message in st.session_state.history:
        if "User" in message:
            with st.container():
                st.markdown(f"""
                <div class="chat-message user">
                    <div>
                        <b>You:</b>
                        <span class="chat-message-content">{message["User"]}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            with st.container():
                st.markdown(f"""
                <div class="chat-message bot">
                    <div>
                        <b>Monika:</b>
                        <span class="chat-message-content">{message["AI"]}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

def setup_ui_components():
    """Set up the user interface components"""
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            "Your response:", 
            disabled=not st.session_state.conversation_started or st.session_state.interview_completed, 
            key="user_input"
        )
    
    with col2:
        if not st.session_state.conversation_started:
            start_button = st.button("Start Interview", type="primary")
        else:
            if not st.session_state.interview_completed:
                send_button = st.button("Send", type="primary")
    
    # Reset button at the bottom
    if st.session_state.conversation_started:
        reset_button = st.button("Reset Interview")
        
    return user_input