#!/bin/bash

echo cdate,cp > ~/reg4us/public/csv/gspc2.csv
/usr/bin/curl http://tkrprice.herokuapp.com/static/gspc.csv|\
    grep 0      |\
    grep -v null|\
    awk -F, '{print $1","$5}' >> ~/reg4us/public/csv/gspc2.csv
exit
