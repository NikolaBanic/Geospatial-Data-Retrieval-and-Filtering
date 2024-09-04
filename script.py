# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:02:34 2024

@author: nikol
"""

import requests
import geopandas as gpd
import json
import sys


# API url
api_url = "https://plovput.li-st.net/getObjekti/"
response = requests.get(api_url)

# Check for invalid status code
if response.status_code != 200:
    print(f"Error, status code: {str(response.status_code)} \n")
    sys.exit()
else:
    print(f"Success, status code: {str(response.status_code)} \n")
    
# Loading data
data = response.json()

# Create GeoDataFrame
if 'features' in data:
    geo_df = gpd.GeoDataFrame.from_features(data['features'])
else:
    print("Invalid data format")
    sys.exit()
    
# Print the total number of records
total_records = len(geo_df)
print(f"Total number of records: {total_records} \n")


# Filter records where 'tip_objekta' equals 16
type_16_df = geo_df[geo_df['tip_objekta'] == 16]
print(f"Total number of records where 'tip_objekta' is equal to 16 is: {len(type_16_df)} \n")


# Save the filtered data to a new GeoJSON file
type_16_df.to_file('type_16_objects.geojson', driver='GeoJSON')
print("Data with 'tip_objekta' equal to 16 has been saved to 'type_16_objects.geojson' \n")