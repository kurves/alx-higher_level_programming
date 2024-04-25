#!/bin/bash
#script that shows supported methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
