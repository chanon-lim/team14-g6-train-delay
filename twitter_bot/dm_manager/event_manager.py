# This script provide EventManager object to handle DM events
from twitter_bot.dm_manager.twitter_api_manager import APIManager

class EventManager:
    api_manager = APIManager()
    def __init__(self, dm_event):
        """Analyze the dm_event is quickrep or user command and send message back. The dm_event is dictionary from JSON"""
        self.dm_event = dm_event

    def handle_event(self):
        try:
            recipient_id = ''
            is_quickreply = 'quick_reply_response' in self.dm_event['direct_message_events'][0]['message_create']['message_data']
            print('quickrep?', is_quickreply)
            print('user command?', not(is_quickreply))
            if is_quickreply:
                response = "Thank you for using quickreply, you will receive quickrep with content 'Because you using quickrep' :)"
                quickrep_option = [
                            {
                                "label": "Because you using quickrep 1 😘",
                                "description": "Description 1",
                                "metadata": "external_id_1"
                            },
                            {
                                "label": "Because you using quickrep 2 🙏",
                                "description": "Description 2",
                                "metadata": "external_id_2"
                            }
                        ]
                self.api_manager.send_direct_message(1465928035333713926, response, quick_reply_options=quickrep_option)
            else:
                response = "Sorry we currently do not support user command, try using quickrep 🥺"
                quickrep_option = [
                            {
                                "label": "Hmm...user command...",
                                "description": "Description 1",
                                "metadata": "external_id_3"
                            },
                            {
                                "label": "Hmm...user command 2...🤔",
                                "description": "Description 2",
                                "metadata": "external_id_4"
                            }
                        ]
                self.api_manager.send_direct_message(1465928035333713926, response, quick_reply_options=quickrep_option)
        except Exception:
            print('Typing event')


