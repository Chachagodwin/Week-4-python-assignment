#f = open('Countries.txt', 'r')

#print(f.read())

#f.close()


# Context Manager Method
#with open('Question.txt', 'r') as f:
 #   for line in f:
  #    print(line, end='')

#with open('State.txt', 'a') as f:
   # To add more content to the file without overwriting the old content, instead of 'w', write 'a'
#f.write('\nAbia')

#with open('Question.txt', 'r') as readFile:
 #  for line in readFile:
  #     if line.startswith('Answer'):
   #       with open('Answers.txt', 'w') as appendFIle:
    #           appendFIle.write(line)


try:
    with open('input.txt', 'r') as readFile:
        with open('output.txt', 'w') as writeFile:
            for line in readFile:
                # Modify the line (e.g., convert to uppercase)
                modified_line = line.upper()
                writeFile.write(modified_line)
    print('File has been read and modified content written to ' output.txt '.')
except FileNotFoundError:
    print('Error: 'input.txt' does not exist.')
except IOError:
    print('Error: Unable to read/write the file.')

