import os
import time

from boto import dynamodb2
from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex
#from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER

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

def write(counter):
    attrib = {"Type": "A", "Available": "YES","Spot":21}
    with table.batch_write() as table_batch:
            #for example_counter in xrange(10):
             reqhashdata = {"Space": counter,"timestamp": time.time()}
             final_dynamo_data = dict(attrib.items() + reqhashdata.items())
             table_batch.put_item(data=final_dynamo_data)

def request(space):
    results = table.query(Space__eq=space)
    #results = table.query(timestamp__gte=0)
    print (results)
    print("debug only disregard")
    #if len(results)==0:
    #    print("No parking available")
    for space in results:
        print("Results of your request:")
        print str(space['Type']) + str(space['Spot'])



write("A1")
write("B3")
write("S21")

request("A1")
request("B3")
request("S21")
