import sys
import datetime
import os

def main():

    # String time
    time_begin = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    print("Inizio elaborazione [" + time_begin + "]\n")

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    listdir = os.listdir(input_filename) # lista di cartelle

    with open(output_filename, 'w') as output_file:

        for dir in listdir:
            listfile = os.listdir(input_filename+"/"+dir)  # lista di file

            for file in listfile:
                size = os.path.getsize(input_filename+"/"+dir+"/"+file)
                if size > 4:
                    output_file.write(input_filename+"/"+dir+"/"+file+" [size: "+str(size)+"]"+"\n")

    output_file.close()

    time_end = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    print("\nDone [" + time_end + "]")

main()