# This script provide EventManager object to handle DM events
from twitter_bot import dm_manager
from twitter_bot.dm_manager.twitter_api_manager import APIManager
from twitter_bot.dm_manager import TWITTER_BOT_ID
from twitter_bot.dm_manager.twitter_event import TwitterEvent, DMEvent
from twitter_bot.worker import ALL_TRAIN_OPERATORS, ALL_TRAIN_LINES
from .bot_reply_manager import BotReplyManager
from train_delay.models import TrainInfo
from twitter_bot.worker.post_delay_tweet import current_operation_state

class EventManager:
    bot_reply_manager = BotReplyManager()
    def __init__(self):
        """Analyze the dm_event is quickrep or user command and send message back. The dm_event is dictionary from JSON"""
        pass

    def handle_event(self, twitter_event: TwitterEvent):
        """Classify event to dm_event"""
        if twitter_event.is_dm_event():
            dm_event = DMEvent(twitter_event.get_event_data())
            self.handle_dm_event(dm_event)
        return 0

    def handle_dm_event(self, dm_event: DMEvent):
        """dm_event has 2 types: quickreply or user command"""
        # ignore self created events
        if dm_event.is_self_created_event():
            return 0
        else:
            if dm_event.is_quickreply():
                self.handle_dm_quickreply_event(dm_event)
            else:
                self.handle_dm_user_cmd_event(dm_event)

    def handle_dm_quickreply_event(self, dm_event: DMEvent):
        recipient_id = dm_event.get_recipient_id()
        quickrep_metadata = dm_event.get_quickrep_metadata().split("#")
        # quickrep_metadata is a list in form ["home"] | ["check_delay", "JREast"]
        if quickrep_metadata[0] == "visit_website":
            self.bot_reply_manager.visit_website(recipient_id)
        if quickrep_metadata[0] == "check_delay_info":
            self.bot_reply_manager.CHECK_DELAY_show_all_operators_list(recipient_id)
        if quickrep_metadata[0] == "home":
            self.bot_reply_manager.home(recipient_id)
        if quickrep_metadata[0] == "check_delay":
            if "get_status" in quickrep_metadata:
                print(f"get_status quickrep run!") #worked!
                operator_name = quickrep_metadata[2]
                trainline_name = quickrep_metadata[3]
                page = int(quickrep_metadata[4])
                self.bot_reply_manager.CHECK_DELAY_show_trainline_delay_status(recipient_id, operator_name, trainline_name, page)
            if len(quickrep_metadata) == 2: # return list of trainline in operator
                operator_name = quickrep_metadata[1]
                print("operator_name:", operator_name)
                self.bot_reply_manager.CHECK_DELAY_show_all_trainline_of_specific_operator(recipient_id, operator_name, 0)
        if quickrep_metadata[0] == "continue":
            if quickrep_metadata[1] == "check_delay":
                option_page = int(quickrep_metadata[3])
                operator_name = quickrep_metadata[2]
                self.bot_reply_manager.CHECK_DELAY_show_all_trainline_of_specific_operator(recipient_id, operator_name, option_page)
            if quickrep_metadata[1] == "follow_delay":
                option_page = int(quickrep_metadata[4])
                operator_name = quickrep_metadata[3]
                self.bot_reply_manager.FOLLOW_DELAY_show_all_trainline_of_specific_operator(recipient_id, operator_name, option_page)
            if quickrep_metadata[1] == "unfollow_delay":
                page = int(quickrep_metadata[4])
                self.bot_reply_manager.UNFOLLOW_DELAY_display_all_following_trainline(recipient_id, page)
        if quickrep_metadata[0] == "return_to":
            # there are 2 cases when hit 'BACK' button: return to all operator when only 1 page of trainline OR return to previous page of trainline
            if quickrep_metadata[1] == "unfollow_delay":
                page = int(quickrep_metadata[4])
                self.bot_reply_manager.UNFOLLOW_DELAY_display_all_following_trainline(recipient_id, page)
            elif quickrep_metadata[1] == "follow_delay":
                if "show_all_operator" in quickrep_metadata:
                    self.bot_reply_manager.FOLLOW_DELAY_show_all_operators_list(recipient_id)
                if "show_all_trainline_in" in quickrep_metadata:
                    operator_name = quickrep_metadata[3]
                    option_page = int(quickrep_metadata[4])
                    self.bot_reply_manager.FOLLOW_DELAY_show_all_trainline_of_specific_operator(recipient_id, operator_name, option_page)
            # ugly, need to refactor and change the name of button for consistency
            else:
                if quickrep_metadata[1] == "check_delay_info":
                    self.bot_reply_manager.CHECK_DELAY_show_all_operators_list(recipient_id)
                else:
                    operator_name = quickrep_metadata[2]
                    option_page = int(quickrep_metadata[3])
                    self.bot_reply_manager.CHECK_DELAY_show_all_trainline_of_specific_operator(recipient_id, operator_name, option_page)
        if quickrep_metadata[0] == "follow_delay":
            if "show_all_operator" in quickrep_metadata:
                self.bot_reply_manager.FOLLOW_DELAY_show_all_operators_list(recipient_id)
            if "show_all_trainline_in" in quickrep_metadata:
                operator_name = quickrep_metadata[2]
                self.bot_reply_manager.FOLLOW_DELAY_show_all_trainline_of_specific_operator(recipient_id, operator_name)
            if "follow_status_of" in quickrep_metadata:
                operator_name = quickrep_metadata[2]
                trainline_name = quickrep_metadata[3]
                page = int(quickrep_metadata[4])
                self.bot_reply_manager.FOLLOW_DELAY_show_trainline_follow_status(recipient_id, operator_name, trainline_name, page)
        if quickrep_metadata[0] == "unfollow_delay":
            if "unfollow_specific_trainline" in quickrep_metadata:
                operator_name = quickrep_metadata[2]
                trainline_name = quickrep_metadata[3]
                page = int(quickrep_metadata[5])
                self.bot_reply_manager.UNFOLLOW_DELAY_unfollow_specific_trainline(recipient_id, operator_name, trainline_name, page)
            if "show_all_following_trainline" in quickrep_metadata:
                self.bot_reply_manager.UNFOLLOW_DELAY_display_all_following_trainline(recipient_id, 0)
    
    # now when user send smt -> return to top menu, for testing only
    def handle_dm_user_cmd_event(self, dm_event: DMEvent):
        recipient_id = dm_event.get_recipient_id()
        self.bot_reply_manager.user_cmd_apologize(recipient_id)


