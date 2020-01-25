from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler

class TicketSkill(MycroftSkill):
    def __init__(self):
        
        super().__init__()
        self.learning = True
        
    def initialize(self):
        
         @intent_handler(IntentBuilder('prasad.you.like.intent').require('prasad'))
            
            
    def handle_thank_you_intent(self, message):
      
        self.speak_dialog("welcome")
    
    
    def stop(self):
        pass
        
def TicketSkill():
    return TestingSkill()
