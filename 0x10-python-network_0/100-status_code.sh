#!/bin/bash
#Script to return status code
curl -s -o /dev/null -w "%{http_code}" "$1"
