def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            file1_contents = file1.read()
            file2_contents = file2.read()
            
            if file1_contents == file2_contents:
                return "The files are the same."
            else:
                return "The files are different."
    except FileNotFoundError as e:
        return f"Error: {e}"

# Example usage
file1_path = input("Enter the path of the first file: ")
file2_path = input("Enter the path of the second file: ")

result = compare_files(file1_path, file2_path)
print(result)