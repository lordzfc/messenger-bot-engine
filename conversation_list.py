from .conversation import Conversation

class ConversationList(object):
  def __init__(self, actions, send_func):
    self._conversations = {}
    self._send_func = send_func
    self._actions = actions

  def add(self, sender, init_action=None): #init_action is optional do m.me links
    if sender not in self._conversations:
      c = Conversation(actions=self._actions, sender=sender, send_func=self._send_func)
      self._conversations[sender] = c
    # else: ELSE WHAT?
  
  def update_actions(self, actions):
    self._actions = actions

  def dispatch(self, sender, action):
    if sender not in self._conversations:
      self.add(sender)
    self._conversations[sender].dispatch(action)