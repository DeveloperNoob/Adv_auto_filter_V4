#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Jackbro007
import os

class Translation(object):
    EXPELLED = os.environ.get("EXPELL").split()
    IN_EXPELLED = os.environ.get("IN_EXPELL").split()
    KITTO = os.environ.get("KITTUMO")
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    GROUP_ID = int(os.environ.get("GROUP_ID"))
    FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL"))
    SIZE_BUTTON = bool(os.environ.get("SIZE_BUTTON"))
    START_TEXT = """<b>Hey {}!!</b>
<i>I am an awesome Bot that works for the <a href="https://t.me/onlymovie76">onlymovie76</a>

   Join my group and send a movie name to see my pevers 😁💥
</i>"""    
    
    HELP_TEXT = START_TEXT
    
    ABOUT_TEXT = """<b>➥ Name</b> : <code> Auto Filter Bot</code>
    
<b>➥ Creator</b> : <b><i><a href="https://t.me/AlbertEinstein_TG">AlbertEinstein_TG</a></i></b>

<b>➥ ReCreator</b> : <b><i><a href="https:t.me0/Jackbro007">Jackbro007</a></i></b>

<b>➥ Language</b> : <code>Python3</code>

<b>➥ Library</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>

<b> Source Code</b> : <i><a href="https://youtu.be/n_5jIQzji6w">AutoFilterBot</a></i>

<b> Server</b> : <i><a href="https://railway.app">Railway</a></i>
