from flask import Flask, request, render_template_string
from flask_cors import CORS
import requests
import PyPDF2

app = Flask(__name__)
CORS(app)

# 🔑 Put your OpenRouter API key here
API_KEY = "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"

# ---------------- FORMAT FUNCTION ----------------
def format_output(text):
    text = text.replace("**", "")

    lines = text.split("\n")
    html = ""

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if "Match Score" in line:
            html += f"<div class='card score'>📊 {line}</div>"
        elif "Skill Match" in line:
            html += f"<div class='card score'>📈 {line}</div>"
        elif "Missing Skills" in line:
            html += "<div class='section'><h3>❌ Missing Skills</h3><ul>"
        elif "Strengths" in line:
            html += "</ul></div><div class='section'><h3>💪 Strengths</h3><ul>"
        elif "Weaknesses" in line:
            html += "</ul></div><div class='section'><h3>⚠️ Weaknesses</h3><ul>"
        elif "Final Recommendation" in line:
            html += "</ul></div><div class='section'><h3>✅ Recommendation</h3>"
        elif line.startswith("*"):
            html += f"<li>{line[1:].strip()}</li>"
        else:
            html += f"<p>{line}</p>"

    html += "</div>"
    return html

# ---------------- PDF TEXT EXTRACTION ----------------
def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# ---------------- AI CALL ----------------
def get_ai_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        return response.json()['choices'][0]['message']['content']
    except:
        return str(response.json())

# ---------------- HTML ----------------
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Resume Analyzer</title>
    <style>
        body {
            background: #0f172a;
            color: white;
            font-family: Arial;
            text-align: center;
            padding: 40px;
        }

        input {
            width: 320px;
            padding: 10px;
            margin: 10px;
            border-radius: 8px;
            border: none;
        }

        button {
            padding: 10px 20px;
            background: #22c55e;
            border: none;
            border-radius: 8px;
            color: white;
            cursor: pointer;
        }

        .result {
            margin-top: 20px;
            padding: 20px;
            background: #1e293b;
            border-radius: 10px;
            max-width: 650px;
            margin-left: auto;
            margin-right: auto;
            text-align: left;
        }

        .section {
            margin-top: 20px;
        }

        .section h3 {
            color: #22c55e;
        }

        ul {
            padding-left: 20px;
        }

        li {
            margin-bottom: 6px;
        }

        .card {
            background: #111827;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 10px;
            font-weight: bold;
        }

        .score {
            color: #22c55e;
        }
    </style>
</head>
<body>

<h1>🤖 AI Resume Analyzer</h1>

<form method="POST" enctype="multipart/form-data">
    <input type="text" name="job_role" placeholder="Enter Job Role" required><br>
    <input type="file" name="resume" accept=".pdf" required><br><br>
    <button type="submit">Analyze Resume</button>
</form>

{% if result %}
<div class="result">
    {{ result | safe }}
</div>
{% endif %}

{% if error %}
<div class="result" style="color:red;">
    {{ error }}
</div>
{% endif %}

</body>
</html>
"""

# ---------------- MAIN ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            job_role = request.form["job_role"]
            file = request.files["resume"]

            text = extract_text(file)

            prompt = f"""
You are an AI recruiter.

Job Role: {job_role}

Candidate Resume:
{text}

Give output in this format:

Match Score: <number>/10
Skill Match Percentage: <percentage>

Missing Skills:
* skill 1
* skill 2

Strengths:
* point 1
* point 2

Weaknesses:
* point 1
* point 2

Final Recommendation:
<short paragraph>
"""

            raw = get_ai_response(prompt)
            result = format_output(raw)

        except Exception as e:
            error = str(e)

    return render_template_string(HTML, result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)