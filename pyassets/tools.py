#Dont run this file directly
import re
import csv
import os
from datetime import datetime
def Ask(question, type = ["num","str","num_and_str", "pass", "num_and_str_special", "dec", "str_allowed"], error_msg = "Input wrong", allowed_strings = []):
    temp_var = input(question)
    if(type == "num"):
        #Ask for answer containing number
        if(is_num(temp_var)):
            return temp_var
        else:
            print(error_msg)
            Ask(question, type, error_msg)

    elif(type == "str"):
        #ask for answer containing string
        if(is_str(temp_var)):
            return temp_var
        else:
            print(error_msg)
            Ask(question, type, error_msg)

    elif(type == "num_and_str"):
        #ask for number and string in one thing
        if(is_str_and_num(temp_var)):
            return temp_var
        else:
            print(error_msg)
            Ask(question, type, error_msg)
    
    elif(type == "num_and_str_special"):
        #ask for number and string in one thing including :,;
        if(is_str_and_num_special(temp_var)):
            return temp_var
        else:
            print(error_msg)
            Ask(question, type, error_msg)

    elif(type == "dec"):
        #ask for answer containing number with decimal
        if(is_dec(temp_var)):
            return temp_var
        else:
            print(error_msg)
            Ask(question, type, error_msg)

    elif(type == "str_allowed"):
        #ask for answer containing allowed strings
        if(contains_specific_strings(temp_var, allowed_strings)):
            return temp_var
        else:
            print(error_msg)
            Ask(question, type, error_msg)

    elif(type == "pass"):
        #pass trough question
        return temp_var



def is_num(input_str):
    #checks for intigers
    return bool(re.match(r'^\d+$', input_str))

def is_dec(input_str):
    #checks for decimals in string
    return bool(re.match(r'^\d+(\.\d+)?$', input_str))

def is_str(input_str):
    #checks for JUST strings (a-z)
    return input_str.isalpha()

def is_str_and_num(input_str):
    #Checks if there are strings and numbers
    return bool(re.search(r'[a-zA-Z]\d', input_str)) or bool(re.search(r'\d[a-zA-Z]', input_str))

def contains_specific_strings(input_str, specific_strings):
    return any(specific_string in input_str for specific_string in specific_strings)

def is_str_and_num_special(input_str):
    # Checks if there are strings and numbers, including : and,
    return bool(re.search(r'[a-zA-Z\d:,;]', input_str)) or bool(re.search(r'[:;,]\d[a-zA-Z]', input_str))


def read_csv_raw(file_path, delimiter = ";"):
    """
    Reads a CSV file and returns its contents as a list of dictionaries.
    
    :param file_path: Path to the CSV file.
    :return: A list of dictionaries representing the rows of the CSV file.
             Returns None if the file does not exist.
    """
    if not os.path.exists(file_path):
        return None
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter = delimiter)
            return list(reader)
    except FileNotFoundError:
        return None

def write_csv(file_path, data, delimiter=";", write_header=True, mode='append'):
    """
    Writes a dictionary to a CSV file, creating the file if it does not exist.
    Writes empty arrays as empty rows in the CSV file.
    
    :param file_path: Path to the CSV file.
    :param data: Dictionary where keys are column headers and values are lists of data.
    :param delimiter: The delimiter to use in the CSV file.
    :param write_header: Whether to write the header row or not.
    :param mode: Mode to handle the file ('overwrite' or 'append').
    """
    # Check if the directory exists, if not, create it
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    try:
        # Open the file in the specified mode
        if mode == 'overwrite':
            with open(file_path, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file, delimiter=delimiter)
                # Always write the header row if write_header is True
                if write_header:
                    writer.writerow(data.keys())
                # Write the data rows
                for values in zip(*data.values()):
                    writer.writerow(values)
        elif mode == 'append':
            with open(file_path, mode='a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file, delimiter=delimiter)
                # Write the header row if write_header is True
                if write_header:
                    writer.writerow(data.keys())
                # Check if any list in data is empty
                if any(not values for values in data.values()):
                    # Write an empty row if any list is empty
                    writer.writerow([])
                else:
                    # Write the data rows
                    for values in zip(*data.values()):
                        writer.writerow(values)
    except FileNotFoundError:
        return None

def read_csv(file_path, delimiter=";"):
    """
    Reads a CSV file and returns its contents as a dictionary where keys are column names and values are lists of column values.
    
    :param file_path: Path to the CSV file.
    :return: A dictionary representing the columns of the CSV file.
             Returns None if the file does not exist.
    """
    if not os.path.exists(file_path):
        return None
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=delimiter)
            
            # Read the header row
            headers = next(reader)
            
            # Initialize an empty dictionary to hold the column data
            column_data = {header: [] for header in headers}
            
            # Iterate through the rows to populate the column data
            for row in reader:
                for i, value in enumerate(row):
                    column_data[headers[i]].append(value)
            
            return column_data
    except FileNotFoundError:
        return None
    
def str_arr_to_int(array):
    #this function converts an all string array with numbers inside to an array containing numbers
    return [int(numeric_string) for numeric_string in array]


def find_indexes(array, search_term):
    #this function searches and returns the keys that the search term resides in the array
    indices = []    
    for i, item in enumerate(array):
        if item == search_term:
            indices.append(i)
    
    return indices

def pad_string(desired_length, original_string):
    # Calculate the difference between the desired length and the original string length
    diff = desired_length - len(original_string)
    
    # If the original string is longer than the desired length, return the original string
    if diff <= 0:
        return original_string
    
    # Calculate the number of spaces needed for padding
    spaces_needed = abs(diff) // 2
    
    # Add spaces to the start and end of the string
    padded_string = " " * spaces_needed + original_string + " " * spaces_needed
    
    return padded_string

def Clear_Term():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')    

def extract_str_date(date_string, delimiter = "."):
    # Convert the string to a datetime object
    #04.05.2024 to separate numbers
    try:
        dt = datetime.strptime(date_string, f"%d{delimiter}%m{delimiter}%Y")
        return dt.day, dt.month, dt.year
    except:
        return None, None, None
    

def sort_dict(object_input, ascending=True):
    #sorts a dict form either ascending sizes to decending
    sorted_items = sorted(object_input.items(), key=lambda x: x[1], reverse=not ascending)    
    sorted_dict = {k: v for k, v in sorted_items}    
    return sorted_dict

