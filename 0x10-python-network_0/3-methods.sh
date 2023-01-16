#!/bin/bash
# Displays HTTP methods the service accepts
curl -sI "$1" | grep "Allow:" | cut -d" " -f2-
