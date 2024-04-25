#!/bin/bash
#script to send json in request
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
