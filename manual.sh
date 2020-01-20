#!/bin/bash
(
echo ============================= ;
echo Auto Update;
python3 ipupdate.py ;
TZ=Indian/Maldives date; (unset TZ);
echo =============================
) | tee -a ip.log
