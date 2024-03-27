#!/bin/bash
#Shows the list of methods allowed on the server
curl -Is $1 | grep -i 'Allow:' | cut -d ' ' -f 2-
