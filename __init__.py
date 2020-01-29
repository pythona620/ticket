from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler

class TicketSkill(MycroftSkill):

    def __init__(self):
        super(TicketSkill,self).__init__()

    def initialize(self):
        self.register_entity_file('source.entity')
        self.register_entity_file('destination.entity')

    


    @intent_handler(IntentBuilder("").require("journy").optionally("travel"))

    def plan_tour(self,sour,dest):
        while true:
            source = self.get_sourcebyuser("get.sour")
            if source in stops:
                while true:
                    destination = self.get_destinationbyuser("get.dest")
                    if destination in stops:
                        return sour, dest
                    else:
                        self.speak('Could you please enter a valid destination stop')
                        continue
            else:
                self.speak('Could you please enter a valid boarding point')
                continue

    self.speak("The source point is " + sour + "and the destination is" +dest)
    def stop(self):
        
        pass

def create_skill():
    return TicketSkill()
