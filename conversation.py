
class Conversation(object):
  def __init__(self, actions, sender, send_func):
    self._actions = actions
    self._sender = sender
    self._send_func = send_func
    self._last_action = ''

  def dispatch(self, action):
    self._last_action = action
    self._send_func(self._sender, self._actions[action])