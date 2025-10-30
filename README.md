# Jarvis-Voice-Assistant
<b><u><i>A Python-based AI Voice Assistant that listens, speaks, and automates tasks.</b></u></i>

🎯<b>Objective</b>

To build an intelligent AI-powered voice assistant that performs daily tasks like opening websites, fetching news, and answering general queries using natural voice commands, integrated with multiple APIs and Python libraries.

🧠<b>Problem Addressed</b>

Many users rely on multiple apps to perform daily tasks such as searching online, playing music, or checking news. This project simplifies that process through a single voice interface — Jarvis, which understands and executes commands instantly.

⚙️<b>Algorithm / Workflow</b>
<ol type ="number">
<li>Speech Recognition: Captures and converts voice commands into text using speech_recognition.</li>

<li>Command Processing: Detects keywords (like “open Google” or “play song”) to execute functions.</li>

<li>AI Query Handling: Uses OpenAI API to process general questions and generate intelligent responses.</li>

<li>Text-to-Speech: Converts text responses to speech using gTTS or pyttsx3.</li>
<li><ul>API Integrations:

<li>NewsAPI → fetches live news headlines</li>

<li>YouTube links → plays songs from musicLibrary</li>

<li>OpenAI → generates AI responses</li>
</ul>
</li>
</ol>

<b>🪜Steps Followed</b>
<ol type ="number">
<li>Imported all required libraries (speech_recognition, webbrowser, pyttsx3, requests, openai, pygame, gtts).</li>

<li>Created musicLibrary.py for song link storage.</li>

<li>Wrote main program (main.py) to continuously listen for “Jarvis” keyword.</li>

<li>Integrated OpenAI for conversational replies.</li>

<li>Implemented error handling and reusable speak() functions.</li>

<li>Tested commands like open google, play kesariya, latest news, etc.</li>
</ol>

📚<b>Important Libraries</b>
<table border="1" cellspacing="0" cellpadding="8">
  <tr>
    <th>Library</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><code>speech_recognition</code></td>
    <td>Recognize and convert voice to text</td>
  </tr>
  <tr>
    <td><code>pyttsx3</code></td>
    <td>Text-to-speech engine</td>
  </tr>
  <tr>
    <td><code>gtts</code></td>
    <td>Google Text-to-Speech (for realistic voice)</td>
  </tr>
  <tr>
    <td><code>pygame</code></td>
    <td>Audio playback for TTS output</td>
  </tr>
  <tr>
    <td><code>webbrowser</code></td>
    <td>Open websites</td>
  </tr>
  <tr>
    <td><code>requests</code></td>
    <td>API integration for fetching news</td>
  </tr>
  <tr>
    <td><code>openai</code></td>
    <td>AI-powered conversational intelligence</td>
  </tr>
</table>

🧩<b>Features</b>
<ul>
<li> ✅ Wake-word activation (“Jarvis”)</li>
<li>✅ Open common websites</li>
<li>✅ Play YouTube songs</li>
<li>✅ Fetch latest news headlines</li>
<li>✅ Answer questions using OpenAI</li>
<li>✅ Text-to-Speech and Speech Recognition</li>
<li>✅ Extendable and modular Python structure</li>
</ul>

📁<b>Project Structure</b>
<ul>
<li>Jarvis_AI_Assistant/</li>
<li>│</li>
<li>├── main.py</li>
<li>├── client.py</li>
<li>├── musicLibrary.py</li>
<li>├── requirements.txt</li>
<li>├── README.md</li>
<li>└── assets/
<li>  └── jarvis_prototype.png  (prototype image you’ll upload)</li>
</li>
</ul>
📊 <b> Testing Instructions</b>
<ol type ="number">
<li>Clone the repository:
  git clone https://github.com/ASHISH8652/Jarvis_AI_Assistant.git
</li>
<li>Install dependencies:
pip install -r requirements.txt
</li>
<li>Run the program:
python main.py
</li>
<li>Say “Jarvis” followed by a command:
<ul>
<li>"Open Google”</li>
<li>“Play Kesariya”</li>
<li>“Tell me today’s news”</li>
<li>“What is artificial intelligence?”</li>
</ul>
</li>
</ol>
💡 <b> Built With</b>
<ul>
<li>Language: Python</li>
<li>Frameworks: OpenAI API, NewsAPI, gTTS</li>
<li>Platforms: Local machine</li>
<li>APIs: OpenAI, NewsAPI</li>
<li>Libraries: speech_recognition, pyttsx3, pygame, webbrowser, requests</li>
</ul>
🚀 <b> Elevator Pitch (Tagline)</b>

“Jarvis – An AI Voice Assistant that understands you and simplifies your digital life.”
🧾 <b>License</b>

This project is licensed under the MIT License – see the LICENSE file for details.

<b>💬 Author</b>

Ashish Kumar Prusty
🧾 License

This project is licensed under the MIT License – see the LICENSE file for details.
🌐 GitHub Profile :https://github.com/ASHISH8652/Jarvis_AI_Assistant.git


