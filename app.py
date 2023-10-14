from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/input', methods=['GET', 'POST'])
def user_input():
    if request.method == 'POST':
        user_data = request.form.get('user_input')
        return f'You entered: {user_data}'
    return render_template('input_form.html')

if __name__ == '__main__':
    app.run(debug=True)

