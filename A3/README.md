CAESAR CIPHER ALGORITHM:
For this program I decided to take a different approach on my Caesar Cipher algorithm in order to practice more options. For this one, I decided to have two alphabets, one uppercase and one lowercase, and then create shifted alphabets depending on the key, in this case is 3. I would get each sentence of the file input, I would find the index of each letter in the regular alphabet, and then get the letter from that index but shifted alphabet and add it to the encrypted or decrypted word. ONLY WORKS WITH KEY BETWEEN 0 AND 26. In order to make it work for key > 26 I would need to do %26 and add 26 to it or something like that.

ERROR HANDLING:
I used try-except to get name of the file input until the user enters a correct name. I took this approach from the book to do error handling.
If the user enters anything except D or E, lets the user know it was a wrong choice.

MORE COMMENTS:
The program outputs the decrypted or encrypted message into an output file, with the name of the input file but added \_enc or \_dec depending on what is done. I did this by getting the name before the .txt of the original input, and then adding \_enc.txt or \_dec.txt to the modified name.

I added more functions in order to make it a little better looking. The code might need some improvements, maybe other more functions in order to look cleaner.
