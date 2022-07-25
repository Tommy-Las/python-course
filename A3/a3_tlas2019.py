import string


def display_menu():
    print('''
    The purpose of this program is to decrypt or encrypt a sentence using Caesar Cipher.
    The program reads each line from an input file,
    Each letter of the sentence is going to be replaced by a letter moved a fixed number of positions.
    which is called a 'key' and is set to the value of 3.
    Each decrypted or encrypted sentence will be written into an output file, with the same name of the input file
    but added _enc or _dec depending on the user choice.
    Lets Start!''')


def get_file():

    file_name = input("\nPlease enter the name of the file: ")

    # loop that runs until user picks the correct input file name

    while True:
        try:
            input_file = open(file_name, 'r')
            break
        except FileNotFoundError:
            print("Name of the file not found. Try Again.\n")
            file_name = input("Please enter the name of the file: ")

    # returns file object and file name
    return input_file, file_name


def shifted_alphabet_e(alphabet, key):
    return alphabet[key:] + alphabet[:key]


def shifted_alphabet_d(alphabet, key):
    return alphabet[-key:] + alphabet[:-key]


def encrypt(word, key):

    modified_word = ''

    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    shifted_lower = shifted_alphabet_e(alphabet_lower, key)
    shifted_upper = shifted_alphabet_e(alphabet_upper, key)

    for char in word:
        if char in shifted_lower:
            letter_index = alphabet_lower.find(char)
            modified_word += shifted_lower[letter_index]
        elif char in shifted_upper:
            letter_index = alphabet_upper.find(char)
            modified_word += shifted_upper[letter_index]
        else:
            modified_word += char

    return modified_word


def decrypt(word, key):

    modified_word = ''

    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    shifted_lower = shifted_alphabet_d(alphabet_lower, key)
    shifted_upper = shifted_alphabet_d(alphabet_upper, key)

    for char in word:
        if char in shifted_lower:
            letter_index = alphabet_lower.find(char)
            modified_word += shifted_lower[letter_index]
        elif char in shifted_upper:
            letter_index = alphabet_upper.find(char)
            modified_word += shifted_upper[letter_index]
        else:
            modified_word += char

    return modified_word


def driver():
    continue_loop = 'y'

    display_menu()

    while continue_loop == 'y':
        file_input, file_name = get_file()
        key = 3

        choice = input(
            "\nWould you like to Encrypt (E) or Decrypt (D): ").lower()

        if choice == 'e':
            output_name = file_name[:-4]+'_enc.txt'
            output_file = open(output_name, 'w')
            phrase = ''
            for line_str in file_input:
                word_list = line_str.split()
                length = len(word_list)
                for i in range(length):
                    word_list[i] = encrypt(word_list[i], key)
                phrase = " ".join(word_list)
                print(phrase, file=output_file)

        elif choice == 'd':
            output_name = file_name[:-4]+'_dec.txt'
            output_file = open(output_name, "w")
            phrase = ''
            for line_str in file_input:
                word_list = line_str.split()
                length = len(word_list)
                for i in range(length):
                    word_list[i] = decrypt(word_list[i], key)
                phrase = " ".join(word_list)
                print(phrase, file=output_file)
        else:
            print("\nERROR: Choose (E) or (D)")
            continue

        print(
            f"\nSUCCESFUL: Values were written to file named '{output_name}'")

        output_file.close()

        continue_loop = input(
            "\nWould you like to try another file? (Y) , or Quit (Q): ")

    print("\nThank you for using my program!")


driver()
