from twitter_bot.dm_manager import TWITTER_BOT_ID

class TwitterEvent:
    def __init__(self, event_data):
        """@event_data: dict object from JSON in POST request"""
        self.event_data = event_data

    def is_dm_event(self):
        """Return True if is the direct message event, False otherwise"""
        if "direct_message_events" in self.event_data:
            return True
        return False

    def get_event_data(self):
        """Return the data of event"""
        return self.event_data

class DMEvent(TwitterEvent):
    def __init__(self, event_data):
        super().__init__(event_data)

    def get_msg_sender_id(self):
        """Return the id of message sender"""
        return self.event_data['direct_message_events'][0]['message_create']['sender_id']

    def get_recipient_id(self):
        """Return the id of recipient of the message"""
        return self.event_data['direct_message_events'][0]['message_create']['sender_id']

    def get_quickrep_metadata(self) -> str:
        """Return metadata of quickrep. Each quickrep will have a separate metadata. Use that to decide what bot do next"""
        return self.event_data['direct_message_events'][0]['message_create']['message_data']['quick_reply_response']['metadata']

    def is_quickreply(self):
        """Return True if DM event is quick reply, False if is user command"""
        return 'quick_reply_response' in self.event_data['direct_message_events'][0]['message_create']['message_data']

    def is_self_created_event(self):
        """Return True if that event is bot created like auto-rep,... The webhook will send POST event for everything, include self tweet, self rep so we need to differentiate what user send, what we send"""
        dm_sender_id = self.get_msg_sender_id()
        return dm_sender_id == TWITTER_BOT_ID