# 🎀 BuildMate

### Your AI-Powered Creative Workspace

**BuildMate** is a personal AI-powered content creation and engagement assistant built using Python and Streamlit.

It helps creators and developers discover trending topics, create engaging content, and generate thoughtful replies to comments — all in one workspace.

*Dream it. Build it. Keep growing.* 💗

---

## ✨ Features

- **🏡 Dashboard** – View saved posts, replies, approval status, and quick actions.
- **☁️ Trending Topics** – Discover topics to inspire your next post.
- **✨ AI Content Studio** – Generate content with Google Gemini.
- **🎀 Create Post** – Write and save posts manually.
- **💌 Reply Assistant** – Generate professional, contextual replies to comments using AI.
- **📖 Content History** – View saved posts and replies and manage their approval status.

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- SQLite
- Pandas
- Feedparser
- Requests
- Pillow

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shreyabpatel632008-sudo/BuildMate.git
cd BuildMate
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a file named `.env` in the project folder and add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your own API key.

**Important:** Never upload your `.env` file or share your API key publicly.

### 5. Run BuildMate

```bash
streamlit run app.py
```

The application will open in your browser.

## 📁 Project Structure

```text
BuildMate/
│
├── assets/
│   └── shreya.jpg
│
├── app.py
├── content_agent.py
├── database.py
├── gemini_agent.py
├── image_agent.py
├── reply_agent.py
├── trend_agent.py
├── requirements.txt
└── .gitignore
```

## 🔐 Privacy & Safety

- API credentials are stored in a local `.env` file.
- Local database files and generated images are excluded from Git.
- Posts and replies are saved for review.
- Content is not automatically published to social media; users remain in control.

## 👩‍💻 About the Creator

**Shreya Patel**

Founder & Creator of BuildMate  
Computer Engineering Student

Built as a personal project to explore AI, automation, Python, and creative technology.

---

⭐ If you find BuildMate interesting, feel free to explore the repository!

**Made with ♡ and a little magic ✨**
