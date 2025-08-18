### 📧 Smart Email Assistant

An AI-powered Streamlit application that connects to your Gmail inbox, summarizes unread emails, and generates polite, context-aware replies using OpenAI GPT.

### ✨ Features

🔑 Secure Gmail Authentication (OAuth2 with token refresh)

📩 Unread Email Fetching (sender, subject, snippet)

📝 AI Summarization (2 concise sentences per email)

🤖 Smart Reply Generator (drafts polite, relevant replies)

🖥️ Streamlit UI (interactive and minimal design)

## 🛠️ Tech Stack  
- **Python 3.10+**  
- **Streamlit** – UI  
- **OpenAI GPT** – Summarization & reply generation  
- **Google Gmail API** – Email access  
- **OAuth2** – Authentication  


🖼️ Demo


**1.Choose Google Account**  


<img width="1458" height="714" alt="Screenshot 2025-08-18 194823" src="https://github.com/user-attachments/assets/82cec854-8bc1-4cdb-bc78-d6fe18d9686b" />


**2.Grant Gmail read access** 





<img width="1422" height="821" alt="Screenshot 2025-08-18 195226" src="https://github.com/user-attachments/assets/d7ed48b8-5b2f-4381-be5c-98a45f236f9c" />


**3.Unread Inbox (Streamlit UI)**  




<img width="1781" height="687" alt="Screenshot 2025-08-18 200134" src="https://github.com/user-attachments/assets/fda55917-4287-4db5-a5f7-8cb740b73609" />


**4.Expanded Email → Summary & Draft Reply**  



<img width="1791" height="735" alt="Screenshot 2025-08-18 200149" src="https://github.com/user-attachments/assets/6431386c-4369-43cb-a5e6-2b5e1464e809" />



## ⚡ Installation  

### 1️⃣ Clone Repository

git clone https://github.com/your-username/Smart-Email-Assistant.git
cd Smart-Email-Assistant

2️⃣ Setup Virtual Environment
conda create -n smart_email_env python=3.9 -y
conda activate smart_email_env

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add OpenAI Key

Create a .env file in project root:

OPENAI_API_KEY=your_api_key_here

## 🔑 Gmail API Setup  

Follow these steps to connect Gmail with the Smart Email Assistant:  

### 1️⃣ Create a Google Cloud Project  
1. Go to [Google Cloud Console](https://console.cloud.google.com/).  
2. Click **New Project** → give it a name (e.g., `Smart Email Assistant`).  
3. Select your billing account (free tier works, no charges for Gmail API).  

---

### 2️⃣ Enable Gmail API  
1. In the project dashboard, go to **APIs & Services > Library**.  
2. Search for **Gmail API** → Click **Enable**.  

---

### 3️⃣ Configure OAuth Consent Screen  
1. Go to **APIs & Services > OAuth Consent Screen**.  
2. Choose **External** (so you can use your Gmail).  
3. Fill in the basic app details (App name, support email, developer email).  
4. **Important**: Under **Test Users**, click **Add Users** → enter your Gmail address (the one you’ll log in with).  
   - Only these accounts can use the app until you publish it.  
5. Save and Continue.  

---

### 4️⃣ Create OAuth Client ID Credentials  
1. Go to **APIs & Services > Credentials**.  
2. Click **Create Credentials > OAuth Client ID**.  
3. Application type → **Desktop App**.  
4. Name it (e.g., `Smart Email Assistant`).  
5. Download the JSON file → rename it to `credentials.json`.  
6. Place `credentials.json` in the **project root**.  

---

### 5️⃣ First Authentication  
1. Run the app once:  
   streamlit run app.py
2.A browser window will open → choose your Gmail → grant permissions.

3.This creates a token.pkl file in your project folder.

4.This is your saved login session, so you don’t need to log in every time.

5.If you delete token.pkl, you’ll be asked to log in again.

✅ Done! If you just enabled the API, wait 2–3 minutes for it to propagate before retrying.


### 🚀  Running Smart-Email-Assistant
streamlit run app.py


The Streamlit UI will open in your browser.

Authenticate Gmail (first run only).

Fetch and summarize unread emails.


### ⚠️ Troubleshooting

FileNotFoundError: 'credentials.json'
Ensure the file is named exactly credentials.json and is in the project root.

403: “Gmail API not used / disabled”
Enable Gmail API for the same project that produced credentials.json. Delete token.pkl and re-run to re-auth.

openai.OpenAIError: api_key must be set
Confirm .env exists in the root and contains OPENAI_API_KEY=....

Stale token
Delete token.pkl and re-run to trigger fresh OAuth.

Ensure you added your Gmail account as a Test User in Google Cloud OAuth screen.

### 🔒 Security Notes

Never commit .env, credentials.json, or token.pkl.

Add them to .gitignore.

### 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss.

