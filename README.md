# Dhiraagu Dynamic DNS
A script to fetch Dhiraagu Fiber or ADSL connection IP and send to no-ip to assign ip to a domain name.

## Requirements
`linux`
`python3`
`requests`

## Installing

```bash
git clone https://github.com/shihaamabr/dhiraaguddns.git
cd dhiraaguddns
```
Edit the creds in ipupdate.py\
Give executable permissions for manual.sh and auto.sh 
```bash
chmod +x manual.sh
chmod +x auto.sh
```
set a chronjob for auto.sh for automatic update
`./manual.sh` if you needed to trigger update manually

---
