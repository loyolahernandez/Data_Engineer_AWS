
import pandas as pd
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def compare_conditions(df, spotId, wind, max_height, min_height, sunrise, sunset):
    df_sesh = df[
        (df['surf_max'] <= max_height) & (df['surf_max'] >= min_height) &
        (df['timestamp_dt'].dt.hour <= sunset) & (df['timestamp_dt'].dt.hour >= sunrise) &
        (df['directionType'] == wind)
    ].copy()

    return df_sesh

def create_sms(df_sesh):
    df_sesh['date'] = df_sesh['timestamp_dt'].dt.date
    df_sesh['hour'] = df_sesh['timestamp_dt'].dt.hour

    # Data para el sms
    df_sms = df_sesh[['hour', 'surf_max', 'directionType']]

    # SMS a string
    sms = df_sms.to_string(index=False)

    return sms

def send_sms(sms):
    account_sid = TWILIO_ACCOUNT_SID 
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body='\nHola! \n\n\n Hoy puede salir ola en Buchu. \n\n\nCondiciones esperadas: ' + sms,
                        from_=PHONE_NUMBER,
                        to='+56982091549'
                    )
    
    return message.sid
