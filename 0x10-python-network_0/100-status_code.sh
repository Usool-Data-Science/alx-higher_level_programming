#!/bin/bash
# Returns the output code
curl -s -o /dev/null -w "%{http_code}" "$1"
