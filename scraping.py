import requests

url = "https://data.cdc.gov/api/views/hk9y-quqm/rows.csv?accessType=DOWNLOAD"

local_filename = "covid19_death_conditions.csv"

response = requests.get(url)
if response.status_code == 200:
    with open(local_filename, "wb") as file:
        file.write(response.content)
    print(f"Download successful! File saved as {local_filename}")
else:
    print(f"Failed to download. Status code: {response.status_code}")
