


# look up the references for a pubMed article
# AFTER it has been found using pymed.
# the articleDictionary is the product of a pymed search.
# https://pypi.org/project/pymed/


# requires:
from bs4 import BeautifulSoup
from urllib import parse, request
import requests
from requests.exceptions import HTTPError


article_address = "https://pubmed.ncbi.nlm.nih.gov/" + articleDictionary['pubmed_id']


try:
    r = requests.get(article_address)
    r.raise_for_status()            
# if there's an http error, move on.
except HTTPError:
    # all_definitions.insert(0, greek_stem)
    # all_definitions.append("\n")
    # outfile.write(out_line)
    pass
article_page = request.urlopen(article_address)
# turn the code of the webpage into a navigable python object
soup = BeautifulSoup(article_page, 'html.parser')

pattern = re.compile("^citation")
all_meta_tags = soup.find_all('meta', attrs={'content': pattern})
all_meta_tags= all_meta_tags[0].prettify().split("\n")