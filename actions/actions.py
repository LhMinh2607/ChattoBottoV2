# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet

class ActionWeather(Action): 
    #bot forecast weather (no it can't)
    def name(self) -> Text:
        return "action_weather" 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'weather':
                name = e['value']
            if name == "today":
                message = "nice"
            if name == "yesterday":
                message = "was nice"
            if name == "tomorrow":
                message = "gonna be nice"
        dispatcher.utter_message(text=message)
        #self._deactivate()
        return []

class ActionAskForName(Action):
    #bot tells user its name
    def name(self) -> Text:
        return "action_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        print(entities)

        for e in entities:
            if e['entity'] == 'you':
                name = e['value']
            if name == "your name":
                message = "My name is ChattoBotto (aka Chad Bot). Atleast that was my creator's decision"
            # if name == "identity" or "identify":
            #     message = "I identify as an attack helicopter"
            if name == "age": #how old
                message = "I'm older than you"
            if name == "author": #created you
                message = "LhMinh2607"
        dispatcher.utter_message(text=message)
        return []




class AskForSlotAction(Action):
    #bot asks for user's age
    def name(self) -> Text:
        return "action_ask_user_age"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        username = tracker.get_slot("username")
        dispatcher.utter_message(text=f"So {username}, How old are you?")
        return []

class ActionAskUsername(Action):
    #bot asks for username
    def name(self) -> Text:
        return "action_ask_username"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(response="utter_ask_username")
        username = next(tracker.get_latest_entity_values("username"), None)
        # if(username):
        #     dispatcher.utter_message(response="utter_ask_username")
        # else:
        #     dispatcher.utter_message(response="utter_greet_with_name")
        return []

class ActionGreetUser(Action):
    #bot greets user with conditions
    def name(self) -> Text:
        return "action_greet_user"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        username = tracker.get_slot("username")
        if(username):
            dispatcher.utter_message(response="utter_greet_with_name")
        else:
            dispatcher.utter_message(response="utter_greet")
        return []
    
class ShowFeedbackAction(Action):
    #bot asks for user's age
    def name(self) -> Text:
        return "action_show_feedback"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        rude_bot = tracker.get_slot("rude_bot")
        rude_bot2 = tracker.get_slot("rude_bot2")
        opinion_about_bot = tracker.get_slot("opinion_about_bot")
        star_rating = tracker.get_slot("star_rating")
        dispatcher.utter_message(response="utter_ask_rude_bot")
        dispatcher.utter_message(text=f"You said: {rude_bot}")
        dispatcher.utter_message(response="utter_ask_rude_bot2")
        dispatcher.utter_message(text=f"You said: {rude_bot2}")
        dispatcher.utter_message(response="utter_ask_opinion_about_bot")
        dispatcher.utter_message(text=f"You said: {opinion_about_bot}")
        dispatcher.utter_message(response="utter_ask_star_rating")
        dispatcher.utter_message(text=f"You rated {star_rating}")
        return []

class SubmitFeedbackAction(Action):
    #bot asks for user's age
    def name(self) -> Text:
        return "action_submit_feedback"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        username = tracker.get_slot("username")
        if(username):
            dispatcher.utter_message(response="utter_submit_feedback")
        else:
            dispatcher.utter_message(response="utter_submit_feedback_nameless")

        return []
# class NameForm(Action):
#     def name(self) -> Text:
#         return "utter_ask_username"

#     def run(self, dispatcher, tracker, domain):  
#         return[SlotSet("username", "None")]

# for e in entities:
        #     if e['entity'] == 'temp' or 'temperature':
        #         name = e['value']
        #     if name == "today" or "":
        #         message = "cool"
        #     if name == "yesterday":
        #         message = "was cool"
        #     if name == "tomorrow":
        #         message = "gonna be cool"   