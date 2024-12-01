def read_file():    while True:
        try:            filename = input("Enter the name of the text file to open: ").strip()
            if not filename.isalnum():                raise ValueError("Invalid file name. File name should not contain special characters.")
                        with open(filename, 'r') as file:
                content = file.read()                print("\nFile content:\n")
                print(content)            return filename  # Return the filename for further operations
                    except FileNotFoundError:
            print("Error: The file does not exist. Please enter a valid filename.")        except ValueError as e:
            print(f"Error: {e}. Please enter a valid filename.")
def write_to_file(filename):    while True:
        try:
            print("\nDo you want to write to the same file or a new file?")            choice = input("Enter 'same' for the same file or 'new' for a new file: ").strip().lower()
                        if choice == 'same':
                with open(filename, 'a') as file:  # Append content to the same file                    content = input("Enter the content to write to the file: ")
                    file.write('\n' + content)                print(f"Content successfully written to the file '{filename}'.")
                break            
            elif choice == 'new':                new_filename = input("Enter the name of the new file: ").strip()
                with open(new_filename, 'w') as file:                    content = input("Enter the content to write to the new file: ")
                    file.write(content)                print(f"Content successfully written to the new file '{new_filename}'.")
                break            
            else:                print("Invalid choice. Please enter 'same' or 'new'.")
                except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
        finally:
            print("The write operation has been completed.")
def main():
    filename = read_file()      write_to_file(filename)  

if name == "__main__":    main()
