def is_vowel(char):
    vowels = "AEIOUaeiou"
    return char in vowels

def create_tf13_1(file_name):
    try:
        with open(file_name, "w") as file:
            file.write("This is a sample text file.\n")
            file.write("It contains words of different lengths.\n")
            file.write("Some words start with vowels, others with consonants.\n")
            file.write("The program will find and save words starting with vowels in TF13_2.\n")
            file.write("Let's test it out!")

        print(f"File {file_name} was created successfully!")
    except IOError as e:
        print(f"Error creating {file_name}: {e}")

def find_and_save_vowels(file1_name, file2_name):
    try:
        with open(file1_name, "r") as file1, open(file2_name, "w") as file2:
            for line in file1:
                words = line.split()
                for word in words:
                    if is_vowel(word[0]):
                        file2.write(word + '\n')

        print(f"Words starting with vowels saved in {file2_name}!")
    except IOError as e:
        print(f"Error processing files: {e}")

def print_file_contents(file_name):
    try:
        with open(file_name, "r") as file:
            print(f"Contents of {file_name}:")
            for line in file:
                print(line.strip())

    except IOError as e:
        print(f"Error reading {file_name}: {e}")

if __name__ == "__main__":
    file1_name = "TF13_1.txt"
    file2_name = "TF13_2.txt"

    create_tf13_1(file1_name)
    find_and_save_vowels(file1_name, file2_name)
    print_file_contents(file2_name)



