#!/bin/sh

cd "$(dirname "$0")"

/usr/sbin/eips -c
/usr/sbin/eips 15  4 'Starting Orbit Clock...'

# Delete old file
rm -f > ./time_latest.png 

# Refresh
python3 /mnt/base-us/extensions/orbitclock/bin/clock.py
eips -g ./time_latest.png
sleep 20
exit
