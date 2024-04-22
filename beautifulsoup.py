from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
<html>
<head>
    <title>Sample HTML Page</title>
</head>
<body>
    <h1>Welcome to my website!</h1>
    <p>This is a sample HTML page.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
</body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Extract title
title = soup.title
print("Title:", title.text)

# Extract text from the body
body_text = soup.body.get_text()
print("Body Text:", body_text)

# Extract list items
list_items = soup.find_all('li')
print("List Items:")
for item in list_items:
    print("-", item.text)
