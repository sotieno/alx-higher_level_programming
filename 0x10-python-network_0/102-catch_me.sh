#!/bin/bash
# catch as catch can
curl -s -X PUT "0.0.0.0:5000/catch_me" -L -H "Origin: ALX" -d "user_id=98"
