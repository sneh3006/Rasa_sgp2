# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"
# import mysql.connector as mysql

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_core_sdk.events import SlotSet
# from rasa_core_sdk import Tracker
# import requests
# import random

# conn= mysql.connect(user='root',password ='root',host='localhost',database='bot_data')
# cursor = conn.cursor()

class utter_python_syllabus(Action):

    def name(self) -> Text:
        return "utter_python_syllabus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Python Syllabus :",image="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png")
        

        return []

class utter_dbms_syllabus(Action):

    def name(self) -> Text:
        return "utter_dbms_syllabus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="DBMS Syllabus :",image="https://lh5.googleusercontent.com/pJ0UnW7ApU5V3gbY_QdjIpiE4CObtQP62cmJi6OHiutHxsx_m0rZ2Y-rBzb4AhHz39GDIJMiLXZdUB6ynqA-OD2Kd6977moRVm189oJXDZB442LTUPT_ZxkXMUFTSi73KQ=w1280")

        return []

class utter_data_structure_syllabus(Action):

    def name(self) -> Text:
        return "utter_data_structure_syllabus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Data Structure Syllabus :",image="https://lh6.googleusercontent.com/tmQmlC4nQeawk_XgyebOV2zuvNH5CiW7ZQc03xQqSDxemk0aTpHcMXVk6Q0RBiYT9G2tsWWVdy3OcLqGx9M-zTsy_N9-TLGjQq3KGW6aHTqXMvGHNyNgKWlaoUi3p-IxiQ=w1280")

        return []