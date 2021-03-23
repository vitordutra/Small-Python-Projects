import os
import requests

def download_file(url, address):
    # Make a Request from Server
    response = requests.get(url)
    print(response)
    if response.status_code == requests.codes.OK:
        with open(address, "wb") as new_file:
            new_file.write(response.content)
        print(f"Download Finished. Saved in: {address}")
    else:
        response.raise_for_status


if __name__ == "__main__":
    BASE_URL = "https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf"
    OUTPUT_DIR = "output"

    for i in range(1, 26):
        file_name = os.path.join(OUTPUT_DIR, f"nota_de_aula_{i}")
        download_file(BASE_URL.format(i), file_name)
