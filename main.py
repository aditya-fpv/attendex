import openpyxl
from flask import Flask, render_template, request

app = Flask(__name)

def column_number_to_letter(column_number):
    # Your existing function
    # Make sure this function is properly indented

@app.route('/')
def home():
    return render_template('input_form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    user_input_number = request.form.get('user_number')
    matching_key, percentages = get_matching_key_and_percentages(user_input_number)
    course_names = {
        1: "Contracts",
        2: "Economics",
        3: "English",
        4: "LegalM",
        5: "Polsci",
        6: "Sociology"
    }
    
    if matching_key is not None:
        course_percentages = []
        for spreadsheet_index, percentage in enumerate(percentages):
            course_name = course_names.get(spreadsheet_index + 1, "Unknown Course")
            course_percentages.append((course_name, percentage))
        return render_template('result.html', matching_key=matching_key, course_percentages=course_percentages)
    else:
        return "No matching key found for the entered number."

def get_matching_key_and_percentages(user_input_number):
    data_structure = {}  # Your existing data_structure initialization

    for spreadsheet_index in range(1, 7):
        # Your existing code for loading and processing Excel sheets

    for key in data_structure.keys

