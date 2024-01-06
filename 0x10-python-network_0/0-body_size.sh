#!/usr/bin/bash
# Script that displays size of a URL response body
curl -s -i "$1" | grep "Content-Length" | sed s/'Content-Length: '//
