from bs4 import BeautifulSoup

# Read the content of the HTML file
with open("index.html", "r") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the elements on the page
heading = soup.find('h1')
paragraph = soup.find('p')
center_div = soup.find(class_='center_div')

# Verify the text content of the elements
if heading and heading.text == "Hello World! DevOps" \
    and paragraph and paragraph.text == "This example contains some advanced CSS methods you may not have learned yet. But, we will explain these methods in a later chapter in the tutorial." \
    and center_div:
    print("Test passed!")
else:
    print("Test failed!")
