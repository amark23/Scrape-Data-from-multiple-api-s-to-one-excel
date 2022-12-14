# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GHHywg-Rpol-ZPjklVs4AQ1GJAD4soLt
"""

import json
import pandas as pd
from urllib.request import urlopen

url = ["https://cea.nic.in/api/instcap_allindia_res.php","https://cea.nic.in/api/installed_capacity_allindia.php",
       "https://cea.nic.in/api/installed_capacity.php","https://cea.nic.in/api/installed_capacity_statewise.php",
       "https://cea.nic.in/api/installed_capacity_progressive.php","https://cea.nic.in/api/planwise_growth.php",
       "https://cea.nic.in/api/psp_energy.php","https://cea.nic.in/api/psp_peak.php","https://cea.nic.in/api/transformation_substations.php",
       "https://cea.nic.in/api/transmission_lines.php"]

for i in url:
  urlres = urlopen(i)
  dictdata = json.loads(urlres.read())   # Reads JSON file & returns JSON object as a dictionary
  df = pd.DataFrame(dictdata)
  m = str(i[23:-4]) #for name as per api name
  with pd.ExcelWriter('DataFile.xlsx',if_sheet_exists='replace', mode='a') as writer:
    df.to_excel(writer, sheet_name=m, index = False)
  urlres.close() #Closing file