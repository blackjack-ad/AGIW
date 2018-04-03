import json
import urllib.request
import datetime

# String time
time_begin = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

# File JSON da cui prendere gli url
json_file = "siti_sample.json"
data = json.load(open(json_file))

# Lista dei titoli JSON
_keys = list(data.keys())

# Lista di array [url, nome file] per output
output = []

print("Inizio elaborazione [" + time_begin + "]\n")

i = 0

# Scansione per titoli (siti) e url
while i < len(_keys):
    title = _keys[i]
    site = data[title]
    print("Elaborazione di: " + title)

    j = 0
    while j < len(site):
        url = site[j]
        name = title + "_" + str(j) + ".html"
        try:
            print("Download HTML di: " + url)
            url_code = urllib.request.urlopen(url)

            # Lettura codice HTML
            s = url_code.read()

            # Creazione del documento
            documento = open("output/"+name, "wb")

            # Write del documento
            documento.write(s)

            # Append in output
            output.append((url,name))
        except urllib.error.URLError:
            print("[Download NON riuscito]: " + url)
            output.append((url, "ERROR"))

        j = j+1

    i = i+1

documento.close()

# Creazione e scrittura del file output.txt
print ("\nCreazione file output.txt")

output_file = open("output.txt", "w")
for item in output:
    output_file.write(item[0] + " --> " + item[1] + "\n")
output_file.close()

time_end = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

print("\nDone [" + time_end + "]")