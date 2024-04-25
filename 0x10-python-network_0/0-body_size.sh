#!/bin/bash
#script to curl an iddress
curl -s "$1" | wc -l
