def reverse_file_content(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    
    reversed_content = content[::-1]
    
    with open(output_file, 'w') as file:
        file.write(reversed_content)

input_file = 'input.txt'
output_file = 'output.txt'

reverse_file_content(input_file, output_file)
print(f"Content from {input_file} has been reversed and written to {output_file}.")