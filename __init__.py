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
# 		self.speak_dialog("start.journy")
		# get source
# 		source = self.get_names("get.source")
		# get destination
# 		destination = self.get_names("get.destination")
# 		answer = source +" " + "to" + " " + destination #adding names
# 		self.speak_dialog("trvout",{"answer":answer}) #output
		def  enter_source_destination(stops):
		while True:
			source = input('Enter your boarding bus stop: ')
			if source in stops:
				while True:
					destination = input('Enter your destination: ')
					if destination in stops:
						return source, destination
					else:
					     print('Could you please enter a valid destination stop')
					     continue
 
	stops = ['vizag', 'hyderabad', 'vijayawada']
	source, destination = enter_source_destination(stops)
	print('The sourceing point is ', source, 'and the destination is ', destination)
	def stop(self):		
		pass
def create_skill():
	return TicketSkill()
