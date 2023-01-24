#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Jeolpaul

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "video")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    SESSION = os.environ.get("SESSION", "BACbgAGVQTEY6FSQoIt8770LZfmHcKvCmujgQzAQyza0w4eZ_4pSVoN-kMM6PbFeoa_5PDidzCTOrbEkxWAZ4n8izkqSTe1iMqbJ3aElwiz6SjiC00CtKd1gjr_RiKT9XKbuu2zF6NE9DpEAa5ftoGPQm4gJ6ghF_Ie_5wqeF6bFUt3tG9XBZv5bKoYvqvRLS27hUnrzIpLx7Hujwe1Lu6yuK65Irfp6xpW3ACaopUT6WAAiwnBBKDx5-q_lSt9f4MXyzFrlcoAfuuwiWQdW94vyX2fN3dLSmpReixiK2u5ICB04pbwcZzcGfLTMWUqWLn1Ar8TGVoPed8yeZAD3K_I5QKuL4AA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
