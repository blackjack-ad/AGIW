import sys
import datetime
from bs4 import BeautifulSoup
import json

def main():

    # String time
    time_begin = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    print("Inizio elaborazione [" + time_begin + "]\n")

    input_filename = sys.argv[1] # index.txt della categoria da esaminare

    with open(input_filename, 'r') as input_file:

        urls = [x for x in input_file.readlines()]  # list
        input_file.close()

        i = 1
        for row in urls:
            path_site = row.split()[1]
            site = open(path_site) # legge sito
            soup = BeautifulSoup(site, 'lxml')

            try:

                # parte da modificare per ogni dominio (questo funziona su www.labx.com)
                title = soup.find('title').text
                price = soup.find('span', attrs = {'class':'price SalesPrice'}).text
                # altri campi ottenibili nello stesso modo

                t = title.replace('\n','').lstrip().rstrip() # formatta la stringa eliminando spazi bianchi, tab ecc.
                p = price.replace('\n','').lstrip().rstrip()

                data = {"name": t, "price": p}
                json_data = json.dumps(data)

                output = open(path_site.rstrip(".html") + ".json", 'w')

                print("[" + str(i) + "] " + json_data)

                output.write(json_data)

                i = i + 1

            except:
                pass

        time_end = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

        print("\nDone [" + time_end + "]")

main()