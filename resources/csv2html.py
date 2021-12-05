import pandas as pd
a = pd.read_csv("FB.csv")
a.to_html("Table.html")
html_file = a.to_html()