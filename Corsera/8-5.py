"""8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count."""

# Prompt for the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

# Open the file for reading
try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
    exit()

# Initialize a count variable
count = 0

# Read each line in the file
for line in fh:
    # Check if the line starts with 'From ' (note the space)
    if line.startswith('From '):
        # Split the line into words
        words = line.split()
        # Print the second word (the email address)
        print(words[1])
        # Increment the count
        count += 1

# Print the final count of lines that start with 'From '
print("There were", count, "lines in the file with From as the first word")

# Close the file
fh.close()
