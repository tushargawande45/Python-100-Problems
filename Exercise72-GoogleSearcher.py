# create a script that let the user type in a search term and opens and search on the browser for that term on Google

import webbrowser

query = input("Input your query: ")

webbrowser.open("https://google.com/search?q=%s" % query)