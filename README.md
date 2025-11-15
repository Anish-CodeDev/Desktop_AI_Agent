# 🧠 AI Agent – Your Intelligent Desktop Co-Pilot

## 📌 Overview

The **AI Agent** is an intelligent desktop automation tool designed as a **goal-oriented agent** capable of handling a wide range of tasks, from file management to document creation and even application control. It acts as your **digital co-pilot**, automating repetitive work, securely managing files, and streamlining day-to-day operations. Leveraging **Agentic AI and Large Language Models (LLMs)**, this agent understands and executes complex instructions, bridging the gap between natural language commands and system actions.

This **AI Agent** also accepts instructions via **speech**, enabling hands-free operation of your computer. This showcases an early form of **Embodied AI Agents** within a desktop environment, allowing for more natural **Human-Agent Collaboration**.

---

## 🚀 Features: An Agentic Perspective

### 📂 File Operations: Core Agentic Capabilities

*   **Plan Execution:** Create, copy, move, rename files/folders based on intricate patterns, demonstrating **Agentic AI Planning and Reasoning**.
*   **Information Retrieval:** Search files and folders efficiently, a fundamental aspect of agent information gathering.
*   **Action Execution:** Open files with their default applications, a basic tool utilization for agents.
*   **State Awareness:** List files and folders in a specific directory, crucial for an agent to understand its environment.

### 🔒 File Encryption: Agent Security and Trust

*   **Secure Operations:** Encrypt files using secure algorithms, demonstrating **Agent Ethics and Safety** by maintaining data confidentiality.
*   **Integrity Assurance:** Maintain confidentiality and integrity of sensitive data.
*   **Tool Integration:** This is accomplished using the `cryptography` library, highlighting **Tools and Frameworks for Agentic AI**.

### 📊 Document & Presentation Generation: Agentic AI Applications

*   **Content Creation Automation:** Generate `.docx` files with advanced formatting, `.pptx` presentations with custom styles, and convert documents to PDF. This exemplifies **Agentic AI Applications** in content creation.
*   **LLM-Powered Generation:** This feature is enhanced by **Agentic AI and Large Language Models (LLMs)**, enabling the agent to understand and generate content based on complex prompts.

### 🖥 Program & CLI Control: Agentic Interaction with the Environment

*   **Environment Interaction:** Open installed programs and control them, execute CLI commands directly through the agent. This showcases an agent's ability to interact with its digital environment.
*   **Workflow Automation:** Automate workflows in terminal/command prompt style, demonstrating **Agentic AI for Complex Problem Solving**.

### 🗂 Folder & Program Management: Agentic Environmental Manipulation

*   **Environmental Access:** Open specific folders instantly, launch applications on demand.
*   **Window Control:** Control program windows (minimize, maximize, close), further enhancing the agent's interaction with the desktop environment.

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

## ⚙️ Usage: Interacting with an Agentic System

The AI Agent's backend relies on the `system_agent` mcp server. For insights into its underlying architecture and the development of such **Agentic AI Architectures**, explore: https://github.com/Anish-CodeDev/mcp_servers/

The `generated_documents` folder showcases outputs from our agent's generative capabilities. The `encrypted_documents` folder demonstrates its security-focused operations.

### **Run the AI Agent**

```bash
python app.py
```

### **Example Agent Commands**

These examples illustrate the agent's ability to interpret and execute instructions, a key aspect of **Agentic AI Planning and Reasoning**.

```plaintext
> create file report.txt
> encrypt file secrets.docx
> generate presentation "Applications of AI" named presentation.pptx
> open folder Documents
> generate a word document on the topic "World Models" named world_model.docx
> open program "Notepad", copy all the text
```

---

## 🔐 Security Notes: Agent Ethics and Safety

*   **Constrained Actions:** The AI Agent is designed with safety constraints; it does not possess the authority to delete any file, focusing only on creation, copying, and moving. This reflects a commitment to **Agent Ethics and Safety**.
*   **Authorization Protocols:** The AI Agent only executes commands you explicitly authorize, ensuring user control and preventing unintended actions, a crucial aspect of **Human-Agent Collaboration**.

---

## 📦 Requirements: The Agent's Toolkit

*   **Core System:** Python 3.9+
*   **Agentic Libraries:**
    *   `load_dotenv` - For secure loading of API Keys.
    *   `cryptography` – For robust Encryption/Decryption, underpinning agent security.
    *   `python-docx` – For Word document generation, an **Agentic AI Application**.
    *   `docx2pdf` - For converting documents to PDF, enhancing agent output usability.
    *   `pandas` - For data manipulation, supporting complex agent tasks.
    *   `python-pptx` – For PowerPoint creation, another **Agentic AI Application**.
    *   `pyautogui` – For GUI automation, enabling the agent to interact with the visual interface.
    *   `subprocess` – For CLI execution, a fundamental **Tool for Agentic AI**.
    *   `os`, `shutil` – For file operations, core to an agent's environmental interaction.
    *   `google-genai` - Provides access to Gemini 2.5 LLM's, powering **Agentic AI and Large Language Models (LLMs)**.
    *   `langgraph` - Manages the agentic workflow, crucial for **Agentic AI Architectures** and complex reasoning.
    *   `mcp` - Provides an interface for **Agent Communication and Coordination** between client and server components.
    *   `pyside6` - Provides a GUI interface for user interaction, facilitating **Human-Agent Collaboration**.

---

## 📜 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute it, fostering open development in **Tools and Frameworks for Agentic AI**.

---

## 💡 Future Improvements: Towards More Sophisticated Agents

*   **Advanced Reasoning & Planning:** Enhance **AI Agent Planning and Reasoning** for more complex, multi-step tasks.
*   **Voice Command Integration:** Further develop **Embodied AI Agents** by refining voice command support for seamless interaction.
*   **Cloud Storage Integration:** Expand agent capabilities to interact with cloud-based data stores.
*   **AI-Powered Task Suggestions:** Implement **Self-Improving AI Agents** that can suggest tasks based on user patterns and context.
*   **Real-time Activity Monitoring:** Develop sophisticated **Agent Ethics and Safety** features through real-time monitoring.
*   **Multi-Agent System Development:** Explore the potential for **Multi-Agent Systems**, enabling agents to collaborate on tasks.
*   **Enhanced Learning Capabilities:** Integrate **Learning in Agentic AI** to adapt and improve performance over time.
*   **Robust Evaluation Metrics:** Define and implement **Agentic AI Evaluation Metrics** to quantify agent performance and progress.

---
