import socket
import sys
import os


from boto import dynamodb2
from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex
from boto.dynamodb2.types import NUMBER
from time import gmtime, strftime

TABLE_NAME = "ParkingPass"
REGION = "us-east-2"

conn= dynamodb2.connect_to_region(
    REGION,
    aws_access_key_id='AKIAINKNLJLNPOG7BJAQ',
    aws_secret_access_key='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'
    )
table = Table(
    TABLE_NAME,
    connection=conn)



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ("100.80.242.56",10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
def write(counter,avail):
    attrib = {"Type": "S", "Available": avail,"Spot":21}
    with table.batch_write() as table_batch:
        #for example_counter in xrange(10):
        reqhashdata = {"Space": counter,"timestamp": time.time()}
        final_dynamo_data = dict(attrib.items() + reqhashdata.items())
        table_batch.put_item(data=final_dynamo_data)


while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        #print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(100)
            strftime("%Y-%m-%d %H:%M:%S", gmtime())
            print >>sys.stderr, 'received "%s"\n' % data
            if data:
                #print >> sys.stderr, 'sending data back to the client'
                connection.sendall(data)
                if ('S21' in data):
                    write('S21','YES')
                else:
                    write('S21','NO')
            else:
                print >> sys.stderr, 'no more data from', client_address
                break
    finally:
        #clean up connection
        connection.close()

def request(space):
        results = table.query(Space__eq=space)
        #results = table.query(timestamp__gte=0)
        print (results)
        print("debug only disregard")
        #if len(results)==0:
        # print("No parking available")
        for space in results:
            print("Results of your request:")
            print str(space['Type']) + str(space['Spot'])
            
