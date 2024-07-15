# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage to scrape
# url = 'https://www.india.gov.in/'

# # Send a GET request to the URL
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content of the webpage using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find and extract specific elements from the webpage
#     # For example, let's extract all <a> tags (hyperlinks) and print their text and href attributes
#     for link in soup.find_all('a'):
#         link_text = link.text.strip()  # Get the text of the hyperlink
#         link_href = link.get('href')   # Get the href attribute (URL) of the hyperlink
#         print(f"Link Text: {link_text}, Link Href: {link_href}")

#     # You can also find and extract other elements such as <p>, <h1>, <div>, etc., based on their HTML tags
#     # For example, to extract all paragraphs (<p> tags) from the webpage and print their text
#     for paragraph in soup.find_all('p'):
#         print(paragraph.text.strip())

# else:
#     print("Failed to retrieve the webpage. Status code:", response.status_code)

import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.youtube.com/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Create an HTML string with the scraped content and link to the CSS file
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scraped Content</title>
        <link rel="stylesheet" href="styles.css">  <!-- Link to the CSS file -->
    </head>
    <body>
        <div class="container">
            <h1>Scraped Content</h1>
    """

    # Find and extract specific elements from the webpage
    # For example, let's extract all <a> tags (hyperlinks) and append them to the HTML content
    html_content += "<h2>Hyperlinks</h2>"
    for link in soup.find_all('a'):
        link_text = link.text.strip()  # Get the text of the hyperlink
        link_href = link.get('href')   # Get the href attribute (URL) of the hyperlink
        html_content += f"<p><a class='link' href='{link_href}'>{link_text}</a></p>"

    # Extract all paragraphs (<p> tags) from the webpage and append them to the HTML content
    html_content += "<h2>Paragraphs</h2>"
    for paragraph in soup.find_all('p'):
        paragraph_text = paragraph.text.strip()  # Get the text of the paragraph
        html_content += f"<p class='paragraph'>{paragraph_text}</p>"

    # Close the HTML tags
    html_content += """
            </div>
        </body>
    </html>
    """

    # Save the HTML content to a file named 'scraped_content.html'
    with open('scraped_content.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("Scraped content saved to 'scraped_content.html'.")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
