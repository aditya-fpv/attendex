import openpyxl

def column_number_to_letter(column_number):
    dividend = column_number
    column_letter = ''
    while dividend > 0:
        modulo = (dividend - 1) % 26
        column_letter = chr(65 + modulo) + column_letter
        dividend = (dividend - modulo) // 26
    return column_letter

# Create a dictionary to store the data structure
data_structure = {}

# Loop through 6 different spreadsheets
for spreadsheet_index in range(1, 7):
    # Load the workbook for the current spreadsheet
    workbook = openpyxl.load_workbook(f'spreadsheet{spreadsheet_index}.xlsx')

    # Select a specific sheet (e.g., the first sheet)
    sheet = workbook.active

    # Define the range of columns from F to BR
    columns = [column_number_to_letter(i) for i in range(6, 192)]  # F to BR

    for column in columns:
        first_cell_value = str(sheet[f'{column}1'].value)
        
        if first_cell_value not in data_structure:
            data_structure[first_cell_value] = [0] * 6

        # Extract data from the column
        data = []
        for row in range(2, sheet.max_row + 1):
            cell = sheet[f'{column}{row}']
            data.append(cell.value)

        # Calculate the percentage of 1s
        total_cells = len(data)
        count_ones = data.count(1)
        percentage = (count_ones / total_cells) * 100

        # Store the percentage in the data structure for the current spreadsheet
        data_structure[first_cell_value][spreadsheet_index - 1] = percentage

    # Close the current workbook
    workbook.close()

# Now, data_structure is a dictionary where each number has a list of percentages for 6 spreadsheets


course_names = {
    1: "Contracts",
    2: "Economics",
    3: "English",
    4: "LegalM",
    5: "Polsci",
    6: "Sociology"
}

# Get the number from the user
user_input_number = input("Enter a number (1 to 192): ")

# Initialize a variable to store the matching key
matching_key = None

# Iterate through the keys in the dictionary and check for a match
for key in data_structure.keys():
    # Extract the number from the key (assuming the number is at the beginning inside square brackets)
    key_parts = key.split()
    if key_parts and key_parts[0].startswith('[') and key_parts[0][1:].isdigit():
        extracted_number = int(key_parts[0][1:])
        if extracted_number == int(user_input_number):
            matching_key = key
            break

# Check if a matching key was found
if matching_key is not None:
    percentages = data_structure[matching_key]
    print(f"Matching Key: {matching_key}")
    for spreadsheet_index, percentage in enumerate(percentages):
        course_name = course_names.get(spreadsheet_index + 1, "Unknown Course")
        print(f"{course_name}: {percentage:.2f}%")
else:
    print(f"No matching key found for number {user_input_number}.")
