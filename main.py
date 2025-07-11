import json
import pandas as pd


with open('data.json', 'r') as file:
    data = json.load(file)


t2m_data = data['properties']['parameter']['T2M']


df = pd.DataFrame(list(t2m_data.items()), columns=['Timestamp', 'Temperature'])


df.to_excel('t2m_data.xlsx', index=False)
