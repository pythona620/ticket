from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
from mycroft.skills.context import adds_context, removes_context
import requests
import random
import re

__author__ = 'pythona'

LOGGER = getLogger(__name__)


airports= {
    "hyderabad"
    "visakhapatnum"
    "vijayawada"
    "tirupathi"
    "rajhamundri"
}

def getstops(self,stops):

    nameList = []
    airports = airports.get(stops)
    if airports != None:

    args = '&airports={}'.formats(airports)
    boarding = self.getdata('board',args)

    if boarding != None:

        boarding = self.trimboarding(boarding)
        
        nameList = [self.cleanString(board['fullname']) for board in boarding]
    return nameList if len(nameList) > 0 else None    
def create_skill():
    return NationalParksSkill()
