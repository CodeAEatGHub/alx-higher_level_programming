#!/usr/bin/bash
curl -sI "$1" | awk '$1 == "Content-Length:" {print $2}'
