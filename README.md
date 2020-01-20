# Dhiraagu Dynamic DNS
A script to fetch Dhiraagu Fiber or ADSL connection IP and send to no-ip to assign ip to a domain name.

## Requirements
`linux`\
`python3`\
`requests` 

## Installing
```bash
git clone https://github.com/shihaamabr/dhiraaguddns.git
cd dhiraaguddns
```
Edit the creds in ipupdate.py\
Give executable permissions for `manual.sh` `and auto.sh`
```bash
chmod +x manual.sh
chmod +x auto.sh
```
set a chronjob for auto.sh for automatic update
`./manual.sh` if you needed to trigger update manually

The bash scripts have timezone set to Maldives, change it if you needed to log another timezone
[List of tz database time zones - WiKi](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)


---
