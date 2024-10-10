"""Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build
a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes,
sort and print the resulting words in python sort() order as shown in the desired output."""

# Prompt for the file name
fname = input("Enter file name: ")

# Open the file for reading
try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
    exit()

# Initialize an empty list to hold unique words
unique_words = []

# Read each line in the file
for line in fh:
    # Split the line into words
    words = line.split()
    
    # Append each unique word to the list
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

# Sort the list of unique words
unique_words.sort()

# Print the sorted unique words
print(unique_words)

# Close the file
fh.close()
