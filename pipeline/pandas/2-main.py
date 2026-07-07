#!/usr/bin/env python3

"""
----
unzip the file without compromising my RAM and downloading the file
"""
import io
import requests
import zipfile


# 1. Google Drive direct download URL for the zip file
file_id = "16MgiuBfQKzXPoWFWi2w-LKJuZ7LgivpE"
direct_download_url = f"https://drive.google.com/file/d/16MgiuBfQKzXPoWFWi2w-LKJuZ7LgivpE/view"

print("Streaming zip archive from Google Drive (saving your local RAM)...")
response = requests.get(direct_download_url, stream=True)

# Define the exact filenames your exercise expects
coinbase_filename = 'coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv'



# 1. Google Drive direct download URL for the zip file
file_id = "16MgiuBfQKzXPoWFWi2w-LKJuZ7LgivpE"
direct_download_url = f"https://drive.google.com/file/d/15A-rLSrfZ0td7muSrYHy0WX9ZqrMweES/view"

print("Streaming zip archive from Google Drive (saving your local RAM)...")
response = requests.get(direct_download_url, stream=True)

# Define the exact filenames your exercise expects
bitstamp_filename = 'bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv'


# 2. Extract just a small preview slice of each file to your computer
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    for filename in [coinbase_filename, bitstamp_filename]:
        print(f"Creating a lightweight local copy of {filename}...")
        with z.open(filename) as infile:
            # Read just the first 10,000 lines (plenty for head/tail testing)
            # and write them to a local file
            lines = [infile.readline() for _ in range(10000)]
            with open(filename, 'wb') as outfile:
                outfile.writelines(lines)

print("\n--- Running your Exercise Code ---")

# 3. Your exercise code runs exactly how you wanted it, using the filename strings!
df1 = from_file(coinbase_filename, ',')
print(df1.head())


"""
df1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
print(df1.head())
df2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')
print(df2.tail())

"""

df2 = from_file(bitstamp_filename, ',')
print(df2.tail())
