def count_words_in_alphabet_rearrangements(words_file, alphabets_file, output_file):
    # Read words from words.txt into a list for sequential checking
    with open(words_file, 'r') as f:
        words_list = [line.strip() for line in f]
        
    # Prepare to store results
    results = []

    # Read each rearrangement from alphabets.txt
    with open(alphabets_file, 'r') as f:
        for line in f:
            alphabet_rearrangement = line.strip()
            count = 0
            #print(alphabet_rearrangement)
            
            # Check each word in the words_list
            for word in words_list:
                #print(word)
                pos = 0  # default position in the alphabet rearrangement
                found = True
                
                # Check if each letter in the word can be found in the rearrangement
                for char in word:
                    
                    pos = alphabet_rearrangement.find(char, pos)  # Find char starting from the current pos
                    
                    if pos == -1:  # If character is not found, break
                        found = False
                        break
                    #pos += 1  # Move to the next position for the next character
                        

                if found:
                    count += 1  # Increment count if the word was found
                #if word in alphabet_rearrangement:
                    #count += 1
                    

            # Append the result for this rearrangement
            results.append(f"{alphabet_rearrangement} {count}")

    # Write the results to alphacounts.txt
    with open(output_file, 'a') as f:
        for result in results:
            f.write(result + '\n')

# Specify file names
words_file = 'words.txt'
alphabets_file = 'alphabets.txt'
output_file = 'alphacounts.txt'

# Execute the function
count_words_in_alphabet_rearrangements(words_file, alphabets_file, output_file)
