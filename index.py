from flask import Flask, request, render_template_string
import openai
import base64

# Set OpenAI API Key (Pastikan kunci API benar)
encoded_key = "c2stcHJvai1BVjVtU0FKQVg0U041VTBvWk9pb255ZjVEUTUycWVTRXFrMG5HYzFWYVVMSi15U0xlR0JoU3FWeWhHaDdQT1lKWGdzRTV0cnZnc1QzQmxia0ZKaGx5VnVtUUlEZlVocmlCY0VHSDBkSnNSellXbW0ycHVtT3VnQXJrRVp2aG55N3BMRHBaWENMRGthNFR0NGt4M2lrbnpLclV6SUE="
try:
    openai.api_key = base64.b64decode(encoded_key).decode("utf-8")
except Exception as e:
    print(f"Error decoding API key: {str(e)}")

# Fungsi interaksi dengan GPT
def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.AuthenticationError:
        return "Authentication error: Please check your API key."
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return f"An error occurred: {str(e)}"

# Buat aplikasi Flask
app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal AI Rizqi</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(to bottom right, #6a11cb, #2575fc);
            color: #fff;
            font-family: 'Arial', sans-serif;
        }
        .card {
            border: none;
            border-radius: 15px;
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
        }
        .btn-primary {
            background: linear-gradient(to right, #6a11cb, #2575fc);
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .btn-primary:hover {
            background: #4a00e0;
            transform: scale(1.05);
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="header">
                    <h1>ROBBERT</h1>
                    <p>ikan sepat makan genteng, selamat datang Asan ganteng!</p>
                </div>
                <div class="card text-dark">
                    <div class="card-body">
                        <form method="post">
                            <div class="mb-3">
                                <label for="prompt" class="form-label">Pertanyaan:</label>
                                <input type="text" id="prompt" name="prompt" class="form-control" placeholder="Ketik pertamyaan disini ya..." required>
                            </div>
                            <div class="d-grid">
                                <button type="submit" class="btn btn-primary btn-lg">Send</button>
                            </div>
                        </form>
                        {% if response %}
                            <div class="response-box">
                                <strong>Response:</strong>
                                <p>{{ response }}</p>
                            </div>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Route utama
@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        user_prompt = request.form.get("prompt")
        response = chat_with_gpt(user_prompt)
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
