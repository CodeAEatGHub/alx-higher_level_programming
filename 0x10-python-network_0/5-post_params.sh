#!/bin/bash
# Sends a POST request to a URL
curl -sX POST -d "email=hr@codingschool.com&subject=I will always be here for PLD" "$1"
