import sys
import os

def run_soplang(filename):
    """
    A simple interpreter for Soplang to execute .sop files.
    """
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    variables = {}

    for line in lines:
        line = line.strip()

        # Skip comments and empty lines
        if line.startswith("//") or not line:
            continue

        # Handle variable declaration (door)
        if line.startswith("door "):
            parts = line[5:].split("=")
            var_name = parts[0].strip()
            value = parts[1].strip()

            # Remove quotes if it's a string
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.isdigit():
                value = int(value)

            variables[var_name] = value

        # Handle print (qor)
        elif line.startswith("qor(") and line.endswith(")"):
            content = line[4:-1].strip()

            # If it's a variable
            if content in variables:
                print(variables[content])
            # If it's a string
            elif content.startswith('"') and content.endswith('"'):
                print(content[1:-1])
            # If it's a concatenation
            elif "+" in content:
                parts = content.split("+")
                result = ""
                for part in parts:
                    part = part.strip()
                    if part.startswith('"') and part.endswith('"'):
                        result += part[1:-1]
                    elif part in variables:
                        result += str(variables[part])
                print(result)
            else:
                print(f"Error: Unknown content '{content}' in qor.")

        else:
            print(f"Error: Unknown command '{line}'.")

if __name__ == "__main__":
    # Provide a default file if no argument is passed
    default_file = "Data Types.sop"
    if len(sys.argv) < 2:
        print(f"No file provided. Using default file: {default_file}")
        run_soplang(default_file)
    else:
        run_soplang(sys.argv[1])