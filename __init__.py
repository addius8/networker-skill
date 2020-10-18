from mycroft import MycroftSkill, intent_file_handler


class Networker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('networker.intent')
    def handle_networker(self, message):
        self.speak_dialog('networker')


def create_skill():
    return Networker()

