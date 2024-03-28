#!/bin/bash
# Returns the output code
curl -Ls -w "%{http_code}\n" "$1"
