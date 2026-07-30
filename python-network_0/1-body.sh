#!/bin/bash
# Sends a GET request to a URL and displays the body only if status is 200
response=$(curl -s -w "\n%{http_code}" "$1")
status_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$ d')

if [ "$status_code" -eq 200 ]; then
    echo "$body"
fi
