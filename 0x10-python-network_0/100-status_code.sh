#!/bin/bash
# curls HTTP response code
curl -so /dev/null -w "%{http_code}" "$1"
