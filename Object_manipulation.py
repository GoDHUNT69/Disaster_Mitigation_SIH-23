import os

# Define the directory path where you want to edit the files
directory_path = r"C:\Users\prashantVIT\PycharmProjects\SIH'23(Draft)\datasets\3fallen trees\valid\labels"

# Ensure the specified path is a directory
if os.path.isdir(directory_path):
    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        # Construct the full path to the file
        file_path = os.path.join(directory_path, filename)

        # Check if the path is a file (not a subdirectory)
        if os.path.isfile(file_path):
            # Open the file for reading and writing
            with open(file_path, 'r+') as file:
                # Read the content of the file
                content = file.read()

                # Check if the file is not empty
                if content:
                    # Replace the first character with '#'
                    modified_content = '2' + content[1:]

                    # Move the file pointer to the beginning of the file
                    file.seek(0)

                    # Write the modified content back to the file
                    file.write(modified_content)

                    # Truncate any remaining content (if the new content is shorter)
                    file.truncate()

                    print(f'Edited content of {filename}')
                else:
                    print(f'Skipping empty file: {filename}')
else:
    print(f"'{directory_path}' is not a valid directory path.")
