import os
import time
import datetime
from boto import dynamodb2
from boto.dynamodb2.table import Table
from boto.dynamodb2.items import Item
#from boto.dynamodb2.conditions import Key, Attr

TABLE_NAME = "ParkingPass"
REGION = "us-east-2"

conn= dynamodb2.connect_to_region(
        REGION,
        aws_access_key_id='AKIAINKNLJLNPOG7BJAQ',
        aws_secret_access_key='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'
        )
table = Table(
        TABLE_NAME,
        connection=conn
       )

users = Table('ParkingPass')
janedoe = Item(users, data={
     'Space': 'janedoe',
     'Type': 'Jane',
     'Available': 'Doe',
     })

janedoe.save()
#table=dynamodb2.get_table('ParkingPass')
#attrs = {'Space': 'A1', 'Type': 'A', 'Available': 'Yes'}
#my_item = table.new_item(attrs=attrs)
#results = table.query_2(
#            Space__eq=0
#            )

#response = table.scan(
#            FilterExpression=Attr('Available').eq('YES')

#print(items)

#tables= conn.list_tables()
#print(tables)
