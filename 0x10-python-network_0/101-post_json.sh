#!/bin/bash
#Sends Json to the server
curl -s -X POST -H 'Content-Type: application/json' -d "@$2" "$1"
