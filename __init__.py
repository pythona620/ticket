from mycroft import MycroftSkill, intent_file_handler

class multipleentitiesSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_intent_file('prasad.you.like.intent', self.handle_prasad_you_like) #register the intentes

#     def handle_prasad_you_like(self, message):
#         source = message.data.get('source')  #get the first keword
#         destination = message.data.get('destination') #get the second keword.
              
    def handle_enter_source_destination(self, stops):
        while True:
            source = self.getsourcebyuser('source')
            if source in stops:
                while True:
                    destination = self.getdestinationbyuser('destination')
                    if destination in stops:
                        return source, destination
                    else:
                        self.speak('Could you please enter a valid destination stop')
                        continue
            else:
                self.speak('Could you please enter a valid boarding point')
                continue

    stops = ['vizag', 'hyderabad', 'vijayawada']
    source, destination = enter_source_destination(stops)
    self.speak("The sourceing point is " + source + "and the destination is" +destination)


    def stop(self):
        pass

def create_skill():
    return multipleentitiesSkill()
