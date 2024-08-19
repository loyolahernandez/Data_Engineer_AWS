
import pandas as pd
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pysurfline

def get_forecast(spotId, wind, max_height, min_height, sunrise, sunset):

    spotforecasts = pysurfline.get_spot_forecasts(
        spotId,
        days=4,
        intervalHours=3,
    )

    df = spotforecasts.get_dataframe()

    return df

def compare_conditions(df, wind, max_height, min_height, sunrise, sunset):
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

    return df_sesh, sms

def send_sms(df_sesh, sms):
    if df_sesh.empty:
        return
    else:
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
