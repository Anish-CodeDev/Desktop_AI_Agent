---

# 🧠 AI Agent – Your Personal Desktop Assistant

## 📌 Overview

The **AI Agent** is an intelligent desktop automation tool capable of handling a wide range of tasks, from file management to document creation and even application control.
It acts as your **digital co-pilot**, automating repetitive work, securely managing files, and streamlining day-to-day operations.

---

## 🚀 Features

### 📂 File Operations

* Create, copy, move, rename file or files using a pattern and rename folders
* Search files and folders efficiently
* Open files with their default applications
* List the files and folders in a specific directory

### 🔒 File Encryption

* Encrypt files using secure algorithms
* Maintain confidentiality and integrity of sensitive data
* This is done using the cryptography library

### 📊 Document & Presentation Generation

* **Microsoft Word**: Generate `.docx` files with headings, subheadings, tables, and formatting
* **PowerPoint**: Create presentations with text and custom formatting options(background,text color)
* Convert documents to PDF for sharing

### 🖥 Program & CLI Control

* Open installed programs and control them
* Execute CLI commands directly through the agent
* Automate workflows in terminal/command prompt style

### 🗂 Folder & Program Management

* Open specific folders instantly
* Launch applications on demand
* Control program windows (minimize, maximize, close)

---

## 🛠 Installation

### **1. Clone the Repository**

```bash
git clone https://github.com/Anish-CodeDev/System_AI_Agent/
cd System_AI_Agent
```
### **2. Setup Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```



---

## ⚙️ Usage
This AI Agent's backend relies on the `system_agent` mcp server. To check the source code of that go to: https://github.com/Anish-CodeDev/mcp_servers/

The `generated_documents` folder is a sample of the documents **generated** by this AI Agent.
The `encrypted_documents` folder is a sample of the documents **encrypted** by this AI Agent

### **Run the AI Agent**

```bash
python app.py
```

### **Example Commands**

```plaintext
> create file report.txt
> encrypt file secrets.docx
> generate presentation "Applications of AI" named presentation.pptx
> open folder Documents
> generate a word document on the topic "World Models" named world_model.docx
> open program "Notepad", copy all the text
```

---

## 🔐 Security Notes

* The AI Agents does'nt have the authority to delete any file, it can only create,copy and move files
* The AI Agent only executes commands you authorize

---

## 📦 Requirements

* **Python 3.9+**
* Libraries:
  * `load_dotenv` - Loads the API Keys from the .env file
  * `cryptography` – Encryption/Decryption
  * `python-docx` – Word document generation
  * `docx2pdf` - Converting a word document to a pdf file
  * `pandas` - Generating data frames for the spreasheets
  * `python-pptx` – PowerPoint creation
  * `pyautogui` – GUI automation
  * `subprocess` – CLI execution
  * `os`, `shutil` – File operations
  * `google-genai` - Provides access to Gemini 2.5 LLM's
  * `langgraph` - Manages the agentic workflow
  * `mcp` - Provides an interface between the MCP Client and the MCP Server
  * `pyside6` - Provides a GUI interface for the user to interact with the AI Agent

---

## 📜 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute it.

---

## 💡 Future Improvements

* Voice command support
* Cloud storage integration
* AI-powered task suggestions
* Real-time activity monitoring
---
