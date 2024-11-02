import requests
from bs4 import BeautifulSoup
import urllib.parse
import os

def banner():
    os.system("cls" if os.name == "nt" else "clear")  
    print("\033[1;31m" + "+" + "-" * 40 + "+")
    print("|           Dork - AUTO DORKING TOOL     |")
    print("|              by NetCore BD             |")
    print("+" + "-" * 40 + "+\033[0m")
    print()

def google_dork_search(query, num_results=20):
    results = []
    pages = num_results // 10 

    for page in range(pages):
        encoded_query = urllib.parse.quote(query)
        start = page * 10  
        url = f"https://www.google.com/search?q={encoded_query}&num=10&start={start}"

        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)

       
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            
            results_on_page = soup.find_all('h3')
            links = [result.find_parent('a')['href'] for result in results_on_page if result.find_parent('a')]
            results.extend(links)
        else:
            print(f"\033[1;31mError: {response.status_code}\033[0m")
            break

    return results[:num_results]

if __name__ == "__main__":
    banner()
    dork_query = input("\033[1;37mEnter Google Dork:\033[0m ")
    print("\033[1;34mSearching...\033[0m")
    results = google_dork_search(dork_query)

    print("\n\033[1;32mSearch Results:")
    print("+" + "-" * 40 + "+")
    for link in results:
        print("\033[1;36m" + link + "\033[0m")
    print("+" + "-" * 40 + "+")