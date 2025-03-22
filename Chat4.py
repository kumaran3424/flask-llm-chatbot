from flask import Flask, request, jsonify, render_template
import ollama
# Set your OpenAI API key here

app = Flask(__name__)



def chat_with_llama(prompt):
    try:
        response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('prompt')
    response = chat_with_llama(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
    