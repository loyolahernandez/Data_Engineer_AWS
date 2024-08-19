"""
************************************************************************
* Author = @ignacioloyola                                              *
* Date = '19/08/2024'                                                  *
* Description = Envio de surf forecast con Twilio                      *
************************************************************************
"""


from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER
import pysurfline
import pandas as pd
import os
from twilio.rest import Client
from twilio_config import *
import time
from utils import get_forecast, compare_conditions,create_sms,send_sms

# Condiciones buchu
spotId = "640a4d90e92030fa8aa15c69"
wind = 'Offshore'
max_height = 2.5
min_height = 2
sunrise = 8
sunset = 18
datos = []

df = get_forecast(spotId)
df_sesh = compare_conditions(df, wind, max_height, min_height, sunrise, sunset)
sms = create_sms(df_sesh)

send_sms(df_sesh, sms)
