import requests, bs4, argparse

#Basic config/information giver
parser = argparse.ArgumentParser(
    prog="pathcurse",
    description="Path segment finder"
)
#For a better usage
parser.add_argument(
    "-u", "--url",
    required=True,
    help="URL for scraping path segments"
)
args = parser.parse_args()

response = requests.get(args.url) #args.url can be defined to a variable
if response.status_code == 200:
    """
    200, OK status code. "Standard response for successful HTTP requests."
    Check https://en.wikipedia.org/wiki/List_of_HTTP_status_codes for detailed information
    """
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    for link in links:
        href = link["href"]
        if href.startswith("/"):
            href = args.url + href
        print(href)

else:
    print(f"Unable to connect, code of status: {response.status_code}")
