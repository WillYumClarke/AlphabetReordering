def has_unique_letters(word):
    """Check if a word contains all unique letters."""
    return len(word) == len(set(word))

def filter_unique_letter_words(input_file, output_file):
    """Read words from input_file and write words with unique letters to output_file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for word in infile:
            word = word.strip()  # Remove newline characters and extra whitespace
            if has_unique_letters(word):  # Check if word has all unique letters
                outfile.write(word + '\n')

# Run the function
filter_unique_letter_words('words_alpha.txt', 'new_words_alpha.txt')
