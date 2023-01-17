#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Jeolpaul

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 22236765))
    API_HASH = os.environ.get("API_HASH", "a2d9fcdaff9f62efa5ec7aadb81efccd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5833640279:AAG3XFLEN5y1L7ueRp_BkY46J7aZgdsPFJY") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = os.environ.get("OWNER_ID", 1187675214)
    SESSION = os.environ.get("SESSION", "1BJWap1wBuwKGlSLBE-05uX3KG599Tg9HzNL9wGNlFe8noh5Mp8Vn0h7NbhfIp5lBX9yyzi46jf7izp36kR7shRSqnoaKu8d3u52p-edMSKw92NFrmMSaS7UsPsDbzTdu_aRURfhGbw4i5gtcbfCvkIIFlUfEDpvHhc0IMamfe39WCeBmyRmlxe5n-oRIbFm3gY8b2JBr4tQF62w921NwCno1390SkzrB-B5TIeFVN9fVxScgrHSaYmQUdIECGOqNX3YJGaWmRY1bJUlTjtzjs3Ktye1lMMEAJSAmkvWmgimd0oY4Lu7Kg1t-0najm24-bTRM6IRwXg67pL_pmMMmY-4bSj7CvSw=")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
