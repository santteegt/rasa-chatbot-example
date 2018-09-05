from rasa_core_sdk import Action
# from rasa_core_sdk.forms import FormAction, EntityFormField, BooleanFormField
from rasa_core_sdk.events import SlotSet
import requests


class GreetApiCall(Action):

	def name(self):
		# type: () -> Text
		return "action_custom_greet"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

		return [SlotSet("user_name", "John Doe")]


class TodoApiCall(Action):

	def name(self):
		# type: () -> Text
		return "action_todo_api_call"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

		# cuisine = tracker.get_slot('cuisine')
		result = requests.get("https://jsonplaceholder.typicode.com/todos/1").json()

		text = "Your current TODO list:"
		dispatcher.utter_message("{} {}".format(text, result))

		# TODO: 'dict' object has no attribute 'timestamp' error ?
		# return [BotUttered(text=text, data=result, timestamp=time.time())]
		return []


class PostsApiCall(Action):

	def name(self):
		# type: () -> Text
		return "action_posts_api_call"

	def run(self, dispatcher, tracker, domain):
		# type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

		# cuisine = tracker.get_slot('cuisine')
		result = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1").json()

		dispatcher.utter_message("You have posted the following messages: {}".format(result))
		dispatcher.utter_template("utter_did_that_help", tracker)

		# TODO: 'dict' object has no attribute 'timestamp' error ?
		# return [SlotSet("posts", result if result is not None else {})]
		return []

#
# class ActionSearchPosts(FormAction):
# 	RANDOMIZE = False
#
# 	@staticmethod
# 	def required_fields():
# 		return [
# 			EntityFormField("user", "userid"),
# 			BooleanFormField("pagination", "yes", "no")
# 		]
#
# 	def name(self):
# 		return 'action_search_posts'
#
# 	def submit(self, dispatcher, tracker, domain):
# 		results = requests.get(
# 			"https://jsonplaceholder.typicode.com/posts?userId={}".format(tracker.get_slot("id"))).json()
#
# 		results = results[:5] if tracker.get_slot("vegetarian") is True else results
# 		# results = RestaurantAPI().search(
# 		# 	tracker.get_slot("cuisine"),
# 		# 	tracker.get_slot("people"),
# 		# 	tracker.get_slot("vegetarian"))
# 		return [SlotSet("search_results", results)]
