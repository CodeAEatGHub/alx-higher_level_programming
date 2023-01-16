#!/bin/bash
# Requests HTTP and echos body
curl -so /dev/null -w '%{size_download}\n' "$1"
