FILENAME = "subject_data.txt"

def main():
    data = load_data()
    print_subjects(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []

    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)

    input_file.close()
    return data

def print_subjects(data):
    """Print the subject details in a formatted way."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students.")

main()