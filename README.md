# WebScraping

Objective: Extract product information (name and price) from an HTML document using Python and Beautiful Soup.

Tools/Libraries Used:
- Python
- Beautiful Soup (a Python library for parsing HTML and XML documents)

Project Steps:

1. HTML Document Acquisition: Obtain an HTML document containing product information. This can be acquired from a website or a local file.

2. Parsing HTML with Beautiful Soup:
    - Import the Beautiful Soup library (`from bs4 import BeautifulSoup`).
    - Create a Beautiful Soup object by parsing the HTML content (`BeautifulSoup(html_content, 'html.parser')`).

3. Locating Desired Elements:
    - Identify and find the specific HTML elements that contain the product name and price using their classes or other attributes (`soup.find()`).
    - Use the `find()` method to search for elements by their classes or tags.

4. Extracting Information:
    - Once the elements are found, extract the text content using `.text` and remove any leading or trailing whitespace using `.strip()`.
    - Store the extracted information in variables (`Product_Name`, `Product_Price`).

5. Output or Further Processing:
    - Utilize the extracted data as needed, such as storing it in variables, writing it to a file (like an Excel file), or processing it further based on your project requirements.

Code Explanation:

The provided  code demonstrates how to extract the product name, price, reviews from an HTML snippet using Beautiful Soup:

- It creates a Beautiful Soup object by parsing the provided HTML snippet.
- Then, it uses the `find()` method to locate specific elements (in this case, the elements containing the product name and price) based on their classes.
- The text content of these elements is extracted using the `.text` method and stored in variables (`Product_Name` and `Product_Price`).
- The extracted information can be printed, saved to variables, or used for further processing.

