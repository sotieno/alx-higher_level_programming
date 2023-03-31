#!/bin/bash
# catch as catch can
curl -sL -X PUT "0.0.0.0:5000/catch_me" -H "Origin: ALX" -d "user_id=98"
