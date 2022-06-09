import re
from bs4 import BeautifulSoup
from urllib import parse, request
import requests
from requests.exceptions import HTTPError
import codecs
import time

class latinToFrench:
    def __init__(self):
        self.dictionary = dict()
    def scrapeTranslations(self, latin):
        definition_location = "=".join(["https://www.grand-dictionnaire-latin.com/dictionnaire-latin-francais.php?lemma", latin])
        r = requests.get(definition_location)
        r.raise_for_status()
        try:
            print(definition_location)
            definition_page= request.urlopen(definition_location)
        except urllib.error.URLError:
            time.sleep(6)
            try:
                definition_page = request.urlopen(definition_location)
            except urllib.error.URLError:
                return()
        sleepy_time = random.randint(3, 10)
        time.sleep(sleepy_time)
        soup = BeautifulSoup(definition_page, 'html.parser')
        definition_box = soup.find_all('span', attrs={'class': 'francais'})
        try:
            definition_box[0].text.strip()
            for definition in definition_box:
                each_definition = definition.text.split(",")
                if len(each_definition) < 1:
                    pass
                for definition in each_definition:
                    if len(definition.split()) == 1:
                        if not latin in self.dictionary.keys():
                            self.dictionary[latin] = []
                        definition = definition.strip()
                        if len(definition.split("'")) > 1:
                            definition = definition.split("'")[1]
                        print(definition)
                        self.dictionary[latin].append(definition)
        except IndexError:
            pass


######## test

# Strip the whitespace, then take all single words between commas.

outfile = codecs.open("/Users/jamesgawley/tesserae/scraped_translations.txt", "w", encoding='utf-8')
with codecs.open("/Users/jamesgawley/tesserae/data/common/grc.stem.txt", encoding='utf-8') as freqfile:
    count = 0
    for file_line in freqfile:
        count = count + 1
        all_definitions = []
        greek_stem = re.findall("^(.+)\t", file_line, re.UNICODE)[0]
        encoded_greek = parse.quote(greek_stem)
        definition_location = "/".join(("https://glosbe.com/grc/la", encoded_greek))
        try:
            r = requests.get(definition_location)
            r.raise_for_status()            
        except HTTPError:
            # all_definitions.insert(0, greek_stem)
            # all_definitions.append("\n")
            # outfile.write(out_line)
            continue
        definition_page= request.urlopen(definition_location)
        soup = BeautifulSoup(definition_page, 'html.parser')
        definition_box = soup.find_all('span', attrs={'class': 'francais'})
        for latin in definition_box:
            latin = latin.text.strip()
            definition = ''
            try:
                definition = re.findall("^(.+)\W", latin)[0]
            except IndexError:
                continue
            all_definitions.append(definition)
        if len(all_definitions) == 0:
            all_definitions = [latin.text.strip() for latin in definition_box]
        all_definitions.insert(0, greek_stem)
        all_definitions.append("\n")
        out_line = ",".join(all_definitions)
        outfile.write(out_line)
        print(out_line)
        if count > 270:
            time.sleep(260)
            count = 0
