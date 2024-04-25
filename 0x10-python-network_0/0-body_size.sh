#!/bin/bash
#script to curl an iddress
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
