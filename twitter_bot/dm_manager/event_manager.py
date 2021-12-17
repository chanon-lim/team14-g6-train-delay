# This script provide EventManager object to handle DM events

class EventManager:
    def __init__(self, dm_event):
        """Analyze the dm_event is quickrep or user command and send message back. The dm_event is dictionary from JSON"""
        self.dm_event = dm_event

    def handle_event(self):
        try:
            recipient_id = ''
            is_quickreply = 'quick_reply_response' in self.dm_event['direct_message_events'][0]['message_create']['message_data']
            print('quickrep?', is_quickreply)
            print('user command?', not(is_quickreply))
        except Exception:
            print('Typing event')


