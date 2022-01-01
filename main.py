#!/usr/bin/python2.7 -tt
import string
from socket import *
import sys
import math

#!/usr/bin/python2.7 -tt
import string
from socket import *
import sys
import math

request_end = '\r\n\r\n'
counter = 0
address_dict = {}
recv_length = 1024
port = int(sys.argv[1])


s = socket()
s.connect(('localhost', port))
while 1:
    address = ''
    ret_format_str = \
    'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\nContent-Length: '
    i = 0
    str_recieved = s.recv(recv_length)
    while i < len(str_recieved):
        if request_end not in str_recieved:
            str_recieved += s.recv(recv_length)

        if str_recieved[i:i + 3] == 'GET':
            j = i+4
            while str_recieved[j] != ' ':
                address += str_recieved[j]
                j += 1

        i += 1

    if address not in address_dict:
        address_dict[address] = 1
    else:
        address_dict[address] += 1

    address_len_return_value = int(math.log10(address_dict[address]))+1
    return_str = ret_format_str + str(address_len_return_value) + '\r\n\r\n' + str(address_dict[address]) + '\r\n\r\n'

    s.send(return_str)



