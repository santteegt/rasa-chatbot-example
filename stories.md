## happy path
* greet
  - action_custom_greet
  - slot{"user_name": "Santiago"}
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - action_custom_greet
  - slot{"user_name": "Santiago"}
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy

## sad path 2
* greet
  - action_custom_greet
  - slot{"user_name": "Santiago"}
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  
## todo path
* greet
  - action_custom_greet
  - slot{"user_name": "Santiago"}
  - utter_greet
* get_todo_list
  - action_todo_api_call
  
## posts path
* greet
  - action_custom_greet
  - slot{"user_name": "Santiago"}
  - utter_greet
* get_posts_list
  - action_posts_api_call