from contextlib import closing
import datetime 
import requests
import json
import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime

engine = create_engine("mysql://root:777@localhost/aeolianeye", echo=True)
conn = engine.connect()
metadata = MetaData()
users = Table(
	'AeolianSensor1', metadata,
	Column('time', DateTime, primary_key=True, nullable=False),
	Column('data', Integer, nullable=False),
	Column('id', String(24))
)
metadata.create_all(engine)

format = '%Y-%m-%dT%H:%M:%S.%fZ'
new_format = '%Y-%m-%d %H:%M:%S' 

url = "https://api.particle.io/v1/devices/events?access_token=ac6cafcc843d7911615b1d92061bc15f0ec1d598"
with closing(requests.get(url, stream=True)) as r:
	for line in r.iter_lines():
		line = line.decode('utf-8')
		if line.startswith('data'):
			obj = json.loads(line[line.find('{'):])
			print(obj)
			dataA = obj.get('data')
			print(dataA, "dataA")
			timeA = obj.get('published_at')
			print(timeA, "timeA")
			datetimeA = datetime.datetime.strptime(timeA, format)
			dataA = obj.get('data')
			coreid = obj.get('coreid')
			ins = users.insert().values(time=datetimeA, data=dataA, id=coreid)
			result = conn.execute(ins)
			print(result)
