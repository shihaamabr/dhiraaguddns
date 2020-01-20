#!/bin/bash
(
echo ============================= ;
echo Auto Update;
/usr/bin/python3.6 ipupdate.py ;
TZ=Indian/Maldives date; (unset TZ);
echo =============================
) | tee -a ip.log
