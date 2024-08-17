#!/bin/bash
source /home/ubuntu/venv/bin/activate
/home/ubuntu/venv/bin/python /home/ubuntu/Data_Engineer_AWS/Proyecto1/Twilio_Scripts/twilio_script.py >> /home/ubuntu/Data_Engineer_AWS/Proyecto1/Twilio_Scripts/script.log 2>&1
