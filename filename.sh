#!/bin/bash

# Create an array to map search strings to corresponding spreadsheet names
search_strings=("Economics" "Contract" "English" "Legal" "Political" "Sociology")
spreadsheet_names=("spreadsheet2.xlsx" "spreadsheet1.xlsx" "spreadsheet3.xlsx" "spreadsheet4.xlsx" "spreadsheet5.xlsx" "spreadsheet6.xlsx")

# Get a list of files in the directory
files=(*.xlsx)

# Loop through each file and perform the renaming
for ((i=0; i<${#search_strings[@]}; i++)); do
    search="${search_strings[i]}"
    spreadsheet="${spreadsheet_names[i]}"
    
    for file in "${files[@]}"; do
        if [[ "$file" == *"$search"* ]]; then
            mv "$file" "$spreadsheet"
            echo "Renamed $file to $spreadsheet"
        fi
    done
done

