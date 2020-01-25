from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

__author__ = 'pythona620/prasad'
LOGGER = getLogger(__name__)

class TicketSkill(MycroftSkill):
	def get_names(self, dialog):  #get input from mic
		yip = self.get_response(dialog) 
		return yip
	
	@intent_handler(IntentBuilder("").require("journy").optionally("travel"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.journy")

		# get myname
		source = self.get_names("get.source")
		# get myfriendname
		destination = self.get_names("get.destination")
		answer = source + destination #adding names

		self.speak_dialog("friends",{"answer":answer}) #output
	def stop(self):		
		pass
def create_skill():
	return TicketSkill()
