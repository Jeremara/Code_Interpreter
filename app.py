from file_reader import read_file
from code_writer import generate_code_with_retry
from code_executor import execute_code

def main(file_path, user_prompt):
    content = read_file(file_path)
    
    if isinstance(content, dict):  # Handle XLSX case
        content = "\n".join([df.to_string() for df in content.values()])  # Convert DataFrame to string
    
    prompt = f"Based on the following content and user's request, generate a Python script:\n\nContent:\n{content}\n\nUser's Request:\n{user_prompt}"
    code = generate_code_with_retry(prompt)
    print(f"Generated Code:\n{code}\n")  # Print the generated code for debugging
    result = execute_code(code)
    return result

def format_output(result):
    if isinstance(result, str):
        return f"Error: {result}"
    else:
        return f"Execution Result: {result}"

# Example Usage
if __name__ == "__main__":
    file_path = "demo.pdf"  # Replace with your file path
    user_prompt = input("Enter request:\n")  # Take user's request
    result = main(file_path, user_prompt)
    formatted_result = format_output(result)
    print(formatted_result)
