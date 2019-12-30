from bs4 import BeautifulSoup
from time import sleep
import urllib.request as urllib2
import re


OUTPUT_FILENAME = "poems.txt"


pattern = re.compile("<br\/?>")  # line breaks


urls = []
for i in range(1, 2000):
    urls.append(f"https://www.pensador.com/poemas/{i}/")


def main():
    with open(OUTPUT_FILENAME, "a") as output_file:
        for url in urls:
            print(f"Fetching {url}")
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page, features="html.parser")
            divs = soup.find_all("p", "frase fr0")
            contents = []
            for div in divs:
                contents.append(textfify(tag=div))
            for content in contents:
                output_file.write(f"{content.strip()}\n\n\n\n")
            sleep(1.5)


def textfify(tag):
    texts = [str(text) for text in tag]
    joined_text = ' '.join(texts)
    for match in re.findall(pattern, joined_text):
        joined_text = joined_text.replace(match, '')
    return joined_text.strip()


if __name__ == "__main__":
    main()