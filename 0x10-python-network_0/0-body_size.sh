#!/bin/bash
# Requests and displays size
curl -so /dev/null -w '%{size_download}\n' "$1"
