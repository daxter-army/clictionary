import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

def meaner(word, limit = 3):
    # to store meaning and use if any
    DICT = {}
    # URL for scrapping
    URL = 'https://www.dictionary.com/browse/'+ word +'?s=t'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('span', class_ = 'e1q3nk1v4')
    
    if len(results) == 0:
        print(Fore.RED + 'No result(s) found! please check your search word' + Style.RESET_ALL)
    else:
        # for populating dictionary
        print('fetching ' + str(limit) + ' result(s)...')
        for item in range(0, limit):
            if item < len(results):
                raw = results[item].text
                # if no meaning or use is there
                if not(raw):
                    DICT[Fore.RED + 'n/a ' + item] = Fore.RED + 'n/a' + Style.RESET_ALL
                # if sentence/use is not available
                if ':' not in raw :
                    DICT[raw.split(':')[0]] = Fore.RED + 'n/a' + Style.RESET_ALL
                    continue

                meaningAndUse = raw.split(':')
                DICT[meaningAndUse[0]] = meaningAndUse[-1].strip()

            else:
                break

    # printing results
    for key in DICT:
        print(Fore.GREEN + 'Meaning : ' + Fore.WHITE + key)
        print(Fore.YELLOW + '\tUse : ' + Fore.WHITE + DICT[key])

# Engine
if len(sys.argv) == 1:
    print(Fore.RED + 'No Search Keyword found !!!')
    print(Fore.WHITE + 'Input sample : <script_name> <search_word> <results_limit>\ndefault limit is 3')

elif len(sys.argv) == 2:
    searchWord = sys.argv[1]
    meaner(searchWord)

elif len(sys.argv) == 3:
    searchWord = sys.argv[1]
    resultLimit = int(sys.argv[2])
    meaner(searchWord, resultLimit)

elif len(sys.argv) > 3:
    print(Fore.YELLOW + 'Not more than 2 arguments!' + Style.RESET_ALL)