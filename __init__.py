from mycroft import MycroftSkill, intent_file_handler

class TicketSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_intent_file('prasad.you.like.intent', self.handle_prasad_you_like) #register the intentes

    def handle_prasad_you_like(self):
        source = message.data.get('source')  
        destination = message.data.get('destination')
        self.speak (source,destination)          
    def handle_enter_source_destination(self, stops):
        while True:
            source = self.get_sourcebyuser("get.source")
            if source in stops:
                while True:
                    destination = self.get_destinationbyuser("get.destination")
                    if destination in stops:
                        return source, destination
                    else:
                        self.speak('Could you please enter a valid destination stop')
                        continue
            else:
                self.speak('Could you please enter a valid boarding point')
                continue

    self.speak("The source point is " + source + "and the destination is" +destination)
    source, destination = enter_source_destination(stops)

    def stop(self):
        stops = ['vizag', 'hyderabad', 'vijayawada']
        pass

def create_skill():
    return TicketSkill()
