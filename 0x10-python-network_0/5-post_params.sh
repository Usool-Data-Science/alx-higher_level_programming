#!/bin/bash
#Send a dataset to the server
curl -s -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
