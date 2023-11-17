from collections import deque
import re
import requests
import urllib.parse
from bs4 import BeautifulSoup

user_url = input('[+] Enter the URL: ')
urls = deque([user_url])
scrapped_urls = set()
emails = set()
count = 0
limit = int(input('[+] Enter the depth limit: '))

# Set a custom user-agent to mimic a web browser
headers = {'User-Agent': 'YourUserAgent'}

try:
    while urls and count < limit:  # Allow processing while there are URLs and within a depth limit
        count += 1
        url = urls.popleft()
        scrapped_urls.add(url)

        print(f'[{count}] Processing: {url}')
        

        try:
            response = requests.get(url, headers=headers, verify=True) # Set verify to False to ignore SSL errors
            response.raise_for_status()  # Check for HTTP request errors
        except (requests.exceptions.RequestException, requests.exceptions.ConnectionError) as e:
            print(f"Request error for {url}: {e}")
            continue

        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and collect email addresses from pattern matches
        new_emails = set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', response.text))
        emails.update(new_emails)

        for anchor in soup.find_all('a'):
            link = anchor.get('href', '')

            # Use urljoin for reliable URL resolution
            absolute_link = urllib.parse.urljoin(url, link)

            if absolute_link not in urls and absolute_link not in scrapped_urls:
                urls.append(absolute_link)

except KeyboardInterrupt:
    print('\n[+] Closing the program...')

print('\n[+] Email(s) found:')
print(f'\n{len(emails)} email(s) found: \n =======================================')

for mail in emails:
    print('  ' + mail)

print('\n[+] Program finished.')