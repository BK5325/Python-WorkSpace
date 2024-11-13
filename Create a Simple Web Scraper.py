import requests
from bs4 import BeautifulSoup
import csv
import logging

# Set up logging
logging.basicConfig(filename='scrape.log', level=logging.INFO)

# URL of the website to scrape
url = "https://www.amazon.com/amz-books/discover?node=8975347011&navStore=books&bbn=283155&rh=n%3A283155%2Cn%3A8975347011&dc&qid=1731419975&rnid=2941120011&ref=is_r_n_10&ref_=is_r_n_10"

# Send a GET request to the website with headers
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# If the GET request is successful, the status code will be 200
if response.status_code == 200:
    logging.info("Successful GET request")
    
    # Get the content of the response
    page_content = response.content
    
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Find the relevant data on the page
    data = []
    items = soup.find_all('div', class_='s-result-item')
    
    for item in items:
        title = item.find('h2', class_='a-size-mini').text.strip()
        price = item.find('span', class_='a-price-whole').text.strip()
        data.append([title, price])
    
    # Write the data to a CSV file
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Price"])  # header row
        writer.writerows(data)
    
    logging.info("Data scraped and saved to data.csv")
    print("Data scraped and saved to data.csv")
else:
    logging.error(f"Failed to retrieve page. Status code: {response.status_code}")
    print(f"Failed to retrieve page. Status code: {response.status_code}")
