#!/bin/bash
# Returns the output code
curl -s -w "%{response_code}\n" "$1"
