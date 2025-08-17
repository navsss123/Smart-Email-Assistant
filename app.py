import streamlit as st
from email_utils import authenticate_gmail, get_unread_emails
from summarizer import summarize_email
from reply_gen import generate_reply

st.set_page_config(page_title="📧 Smart Email Assistant", layout="wide")
st.title("📬 Smart Email Assistant")

st.write("Fetch, summarize, and auto-reply to unread emails with AI 🤖")

# Authenticate and get unread emails
service = authenticate_gmail()
emails = get_unread_emails(service)

if not emails:
    st.success("✅ No unread emails found.")
else:
    for i, email in enumerate(emails, 1):
        with st.expander(f"📨 Email #{i}: {email['subject']}", expanded=False):
            st.markdown(f"**From:** {email['from']}")
            st.markdown(f"**Snippet:** {email['snippet']}")

            with st.spinner("Summarizing..."):
                summary = summarize_email(email["snippet"])
            st.success(f"🧠 Summary: {summary}")

            with st.spinner("Generating reply..."):
                reply = generate_reply(email["snippet"])
            st.info(f"✍️ Suggested Reply:\n\n{reply}")
