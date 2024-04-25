#!/bin/bash
#script that makes a request to url
curl -s http://0.0.0.0:5000/catch_me | grep "You got me!"
