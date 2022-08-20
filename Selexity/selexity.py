# // Lets start by importing stuff - god i hate the look of importing libs in py \\ # 
import os, json, logging, random, time, asyncio, discord, pymongo, aiohttp, tasksio, threading
from tracemalloc import start
from discord.ext import commands 
from tasksio import TaskPool
from colored import fg
from os import system, get_terminal_size as _terminal_size

_os = os.system # // Creating a small shortcut 

white                = fg('#FFFFFF')
pink                 = fg('#cc00dd')
cyan                 = fg('#47ffff')
lime                 = fg('#10f447')
light_purple         = fg('#cd07ff') #// Defining Colours? Colors? .
darker_light_purple  = fg('#7e2286') 
yellow               = fg('#fff900')
darker_yellow        = fg('#9e9b33')
red                  = fg('#ff0000')

OK_    = logging.basicConfig(level=logging.INFO,format=f"{white}[{pink}%(asctime)s.%(msecs)03d{white}]      {lime}%(message)s {white}      [ {cyan} OK {white} ]",datefmt="%H:%M:%S")
ERROR_ = logging.basicConfig(level=logging.INFO,format=f"{white}[{pink}%(asctime)s.%(msecs)03d{white}]      {lime}%(message)s {white}      [ {red} ERROR {white} ]",datefmt="%H:%M:%S")
INFO_  = logging.basicConfig(level=logging.INFO,format=f"{white}[{pink}%(asctime)s.%(msecs)03d{white}]      {lime}%(message)s {white}      [ {cyan} INFO {white} ]",datefmt="%H:%M:%S")
## ^^ Setting-up  Status' For Logging

def _xspaces(text: str):
        try:
            col = _terminal_size().columns
        except OSError:
            return 0
        textl = text.splitlines()
        ntextl = max((len(v) for v in textl if v.strip()), default = 0)
        return int((col - ntextl) / 2) # get terminal size so we can centre text.

def Center(text: str, spaces: int = None, icon: str = " "):
        if spaces is None:
            spaces = _xspaces(text=text)
        return "\n".join((icon * spaces) + text for text in text.splitlines()) #// Centre function just incase we use it later ;)



clear = _os("cls||clear")

with open("ClientConfiguration.json") as ClientConfig:
    try:
        config = json.load(ClientConfig)

        BotAuth              = config["Client Settings"]["Bot Authorization"]
        Guild                = config["Client Settings"]["Target Guild"]
        ChannelNames         = config["Guild Settings"]["Channel Names"]
        RoleNames            = config["Guild Settings"]["Role Names"]
        WebhookNames         = config["Guild Settings"]["Webhook Names"]
        WebhookContent       = config["Guild Settings"]["Webhook Content"]
        WebhookMessageAmount = config["Guild Settings"]["Webhook Message Amount"]
    except (Exception) as fault:
        ERROR_
        print(fault)

