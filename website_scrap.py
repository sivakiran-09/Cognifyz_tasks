import requests
from bs4 import BeautifulSoup

# Wikipedia page
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
headers = {
    "User-Agent": "Mozilla/5.0"
}
try:
    # Fetch webpage
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title
    title = soup.find("h1")
    print("\n📖 Wikipedia Article")
    print("=" * 50)
    print("Title:", title.text)

    print("\n📄 First 5 Paragraphs:\n")

    # Extract paragraphs
    paragraphs = soup.find_all("p")

    count = 0
    for para in paragraphs:
        text = para.get_text(strip=True)

        if text:  # Skip empty paragraphs
            print(text)
            print()
            count += 1

        if count == 5:
            break

except requests.exceptions.RequestException as e:
    print("❌ Error:", e)