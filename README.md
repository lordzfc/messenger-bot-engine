# Simple Messenger's Bot engine

A simple lib for mapping action to exact response.

To use that, You have to define your action_to_message dict and write your own sending msg function for processing message dict / object.

Example Actions Dict:

```python
{
  #desired object can be dict, database entry - depends on your sending funtion (or vice versa)
  "HI": {
    "message": "Hey!"
  },
  "BUY": {
    "message":"Bye!"
  }
}
```

Example send_func(required!):

```python
def send_response(sender, message):
  msg_bot.send_message(BotMessage(sender, message).payload)
```

Example usage:

```python
conversations = ConversationList(get_actions_dict(), send_response)
conversations.dispatch(sender_msg.sender, action)
```


## Todo:
[ ] `__repr__` and `__str__`