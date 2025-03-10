# Question: Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:

# https:/www.google.com
# https:/www.yahoo.com
# https:/www.stackoverflow.com
# https:/www.pythonhow.com
# Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.

# Expected output: 

# http://www.google.com
# http://www.yahoo.com
# http://www.stackoverflow.com
# http://www.pythonhow.com


# Clean each line by removing 's' from https and adding a slash

with open("urls.txt", "r") as file:
    lines = file.readlines()

print(lines)

with open("urls_corrected.txt", "w") as file:
    for line in lines:
        line_remove_s = line.replace("s", "", 1)
        line_remove_s_add_slash = line_remove_s[:6] + "/" + line_remove_s[6:]
        file.write(line_remove_s_add_slash)
