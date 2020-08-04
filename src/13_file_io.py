"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

#THIS WAY YOU MUST CLOSE THE FILE

fooFile = open('foo.txt', 'r')
fileContent = fooFile.read()
fooFile.close()

print(fileContent)

# THIS WAY DOESN'T REQUIRE YOU TO CLOSE THE FILE
# PYTHON WILL CLOSE THE FILE FOR YOU
# THIS WILL SET CONTENT TO NONE IN THE CASE OF THE FILE NO EXISTING

try:
    with open("foo.txt") as fooFile1:
        content = fooFile1.read()
except FileNotFoundError:
    content = None

print('\n')
print(content)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
names = ["Eddie", "John", "Tommy", "Pete"]

with open('bar.txt', 'w') as barFile:
    for name in names:                      # loops through names
        barFile.write(name)                 # write each name to file
        barFile.write("\n")                 # add new line after each name

with open('bar.txt', 'r') as barFile:
    barContent = barFile.read()

print('\n')           # Separates with a new line.
print(barContent)     # Prints our file contents.
print(barFile.closed) # Shows if the file was closed or not.