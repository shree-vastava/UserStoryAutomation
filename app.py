import streamlit as st
import requests

st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #4CAF50;  /* green color */
    color: white;
}
div.stButton > button:last-child {
    background-color: #2196F3;  /* blue color */
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("💼 Storyteller For Your Product")

st.write("\n\n")

st.markdown("""
Upload a PDF document or provide a Google Doc URL containing your product requirements, and let our AI-powered tool automatically generate detailed user stories with acceptance criteria and story points. Relax, the tool will add the stories to your Jira or Notion board.

- Quickly convert requirements into developer-ready user stories.
- Maintain clarity and consistency across all stories.
- Get your stories added to your Notion/Jira boards
- Save time and streamline your product development process.


""")
st.write("\n\n")
# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if st.button("Generate stories from file"):
    if uploaded_file is not None:
        st.write("Uploading file...")

        # Send to n8n Webhook
        webhook_url = "https://prakhar3012.app.n8n.cloud/webhook/82fdf5ec-6a19-4f97-b486-9d63347811d4"  # replace with your Webhook URL

        files = {"file": (uploaded_file.name, uploaded_file.read(), "application/pdf")}
        response = requests.post(webhook_url, files=files)

        if response.status_code == 200:
            st.success("File uploaded successfully!")
            st.json(response.json())  # Show JSON response from OpenAI
        else:
            st.error(f"Upload failed: {response.status_code}")
        
        uploaded_file = None
        
st.write("\n\n")   # adds a blank line
st.markdown("""
<div style="text-align: center; font-size: 24px; font-weight: bold; margin: 20px 0;">
OR
</div>
""", unsafe_allow_html=True)
st.write("\n\n")   # another blank line

doc_url = st.text_input("📄 Enter your Google doc URL:")
if st.button("Generate Stories from Google Doc"):
    webhook_url = "https://prakhar3012.app.n8n.cloud/webhook/4a6ee83e-b16a-4f1d-bc4b-529867aa1a95"  # replace with your Webhook URL

    if not webhook_url:
        st.error("Please enter a Webhook URL")
    else:
        try:
            payload = {"content": doc_url}
            response = requests.post(webhook_url, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                st.success(f" Success: {data.get('result', '')}")
            else:
                st.error(f" Workflow failed with status {response.status_code}")
        except Exception as e:
            st.error(f" Exception: {e}")
    