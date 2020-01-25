from mycroft import MycroftSkill, intent_file_handler

class TomatoSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_intent_file('what.is.a.prasad.intent', self.handle_what_is) #register the intentes
        self.register_intent_file('prasad.you.like.intent', self.handle_do_you_like) #register the intentes

    
    def handle_what_is(self, message): 
        self.speak('your friend is going to some place') #not given place

    def handle_do_you_like(self, message):
        first_type = message.data.get('from')  #get the first keword
        second_type = message.data.get('to') #get the second keword
                     
        if first_type is not None:
            self.speak("your friend is going " + first_type  + " " + "to" + " "+  second_type ) #print specific keword
            self.speak(first_type + " "+second_type)
        else:
            self.speak('you are not given any specific word!') #print if specific keword is not given
            
            
    def stop(self):
        pass

def create_skill():
    return TomatoSkill()
