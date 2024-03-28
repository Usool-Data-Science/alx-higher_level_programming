#!/bin/bash
#Send a specialized header to the server
curl -s --header 'X-School-User-Id: 98' "$1"
