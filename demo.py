from bs4 import BeautifulSoup

html_content = """
<div class="a-section a-spacing-none a-spacing-top-micro">
    <div data-cy="title-recipe" class="a-section a-spacing-none puis-padding-right-small s-title-instructions-style">
        <div class="s-desktop-width-max s-desktop-content s-wide-grid-style-t1 s-opposite-dir s-wide-grid-style sg-row">
            <span class="a-price-whole">34,990</span>
            <span class="a-size-medium a-color-base a-text-normal">ZEBRONICS Newly Launched NBC 2S Core i5 11th Gen 1155G7 - (16 GB RAM/ 512 GB M.2 SSD SATA/Windows 11 Home) 15.6” 1080p, Type C Port, Fingerprint Sensor, 38.5Wh Battery (Silver)</span>
        </div>
    </div>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Find the necessary elements using their classes
price_span = soup.find('span', class_='a-price-whole')
name_span = soup.find('span', class_='a-size-medium a-color-base a-text-normal')

# Extract the text if the elements are found, or set default values
Product_Name = name_span.text.strip() if name_span else ''
Product_Price = price_span.text.strip() if price_span else ''

# Print the extracted data
print("Product Name:", Product_Name)
print("Product Price:", Product_Price)
