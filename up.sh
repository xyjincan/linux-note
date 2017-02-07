#!/bin/bash


rm hosts.bak
rm hosts

wget "https://raw.githubusercontent.com/racaljk/hosts/master/hosts"

cp /etc/hosts hosts.bak
rm /etc/hosts
cat fedohosts  hosts >>  new
cp new /etc/hosts
rm new

echo "Success"
