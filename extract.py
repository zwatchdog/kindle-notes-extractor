import re
import pandas as pd

data = []
quote = ""

# open the file and read the lines 
with open(r"clippings.txt", encoding="utf-8") as file:
    lines = file.readlines()

# iterate over the file and remove white spaces 
for line in lines:
    line = line.strip()

    if line.startswith("- Your Highlight"):
        # skip lines that startswith your highlight
        continue
    elif line.startswith("- Your Bookmark") or line.startswith("=========="):
        # remove this part if you want to see your bookmarks 
        continue
    elif line != "":
        if quote == "":
            quote = line
        else:
            # match one or more characters (.+) , any whitespace character (\s) 
            # \((.+)\) , this means \( starts with "(", \) ends with ")", so captures the author's name which is one or more character in the parenthesis 
            # $ means end of the line
            match = re.match(r"^(.+)\s\((.+)\)$", line)
            if match:
                book_title = match.group(1)
                author = match.group(2)
                data.append([quote, book_title, author])
                quote = ""  # Reset the 'quote' variable

df = pd.DataFrame(data, columns=["quote", "book title", "author"])

df.to_csv('my_kindle_clippings.csv', index = False)
