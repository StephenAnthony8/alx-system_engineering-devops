#!/usr/bin/bash

curl -s -i "$1" | grep "Content-Length" | sed s/'Content-Length: '//
