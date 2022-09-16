# books = open("books.txt", "w")

# books.write("This is a book store\n")
# books.write("This is line 2\n")
# books.write("This is line 3\n")

# books.close()

f = open('books.txt', 'r')

for line in f.readlines():
    print(line.strip())

f.close()
