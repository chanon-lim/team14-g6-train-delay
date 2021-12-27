# This script provide EventManager object to handle DM events
from twitter_bot import dm_manager
from twitter_bot.dm_manager.twitter_api_manager import APIManager
from twitter_bot.dm_manager import TWITTER_BOT_ID
from twitter_bot.dm_manager.twitter_event import TwitterEvent, DMEvent
from twitter_bot.worker import ALL_TRAIN_OPERATORS, ALL_TRAIN_LINES
from .quick_reply_manager import QuickrepOptionManager
from train_delay.models import TrainInfo
from twitter_bot.worker.post_delay_tweet import current_operation_state

class BotReplyManager:
    api_manager = APIManager() 
    quickreply_manager = QuickrepOptionManager()
    def __init__(self):
        pass

    def visit_website(self, recipient_id):
        """Send message and link to Mike's website"""
        quickrep_options = self.quickreply_manager.home_options()
        response = "Please visit website at: https://train-delay-chien.herokuapp.com/"
        self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)

    def CHECK_DELAY_show_all_operators_list(self, recipient_id):
        """Show list of all operators to CHECK delay"""
        quickrep_options = self.quickreply_manager.CHECK_DELAY_all_operator_options()
        response = "Please choose 1 operator to see all trainlines belong to"
        self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)

    def CHECK_DELAY_show_all_trainline_of_specific_operator(self, recipient_id, operator_name, page=0):
        """Show list of all trainline in a specific operator name, eg all trainline of JREast"""
        quickrep_options = self.quickreply_manager.CHECK_DELAY_all_trainline_of_specific_operator_options(operator_name, page)
        response = "Choose a trainline to check its delay status"
        self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)

    def home(self, recipient_id):
        quickrep_options = self.quickreply_manager.home_options()
        response = "Welcome back..."
        self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)

    def user_cmd_apologize(self, recipient_id):
        """Sorry user for not supporting user cmd yet"""
        quickrep_options = self.quickreply_manager.home_options()
        response = "Sorry, we currently do not support user command yet. Please use quick reply instead 🙇‍♂️"
        self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)

    def CHECK_DELAY_show_trainline_delay_status(self, recipient_id, operator_name, trainline_name, page):
        quickrep_options = self.quickreply_manager.CHECK_DELAY_show_trainline_delay_status_options(operator_name, trainline_name, page)
        trainline_status_object = TrainInfo.objects.filter(operator_ja=operator_name).filter(railway_ja=trainline_name)[0]
        trainline_status = current_operation_state(trainline_status_object.information_ja)
        if trainline_status == "normal":
            response = f"🟢 {trainline_status_object.railway_ja}: {trainline_status_object.information_ja}"
        else:
            response = f"🟠 {trainline_status_object.railway_ja}: {trainline_status_object.information_ja}"
        self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)

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
        if quickrep_metadata[0] == "continue" and quickrep_metadata[1] == "check_delay":
            option_page = int(quickrep_metadata[3])
            operator_name = quickrep_metadata[2]
            self.bot_reply_manager.CHECK_DELAY_show_all_trainline_of_specific_operator(recipient_id, operator_name, option_page)
        if quickrep_metadata[0] == "return_to":
            if quickrep_metadata[1] == "check_delay_info":
                self.bot_reply_manager.CHECK_DELAY_show_all_operators_list(recipient_id)
            else:
                operator_name = quickrep_metadata[2]
                option_page = int(quickrep_metadata[3])
                self.bot_reply_manager.CHECK_DELAY_show_all_trainline_of_specific_operator(recipient_id, operator_name, option_page)

    # now when user send smt -> return to top menu, for testing only
    def handle_dm_user_cmd_event(self, dm_event: DMEvent):
        recipient_id = dm_event.get_recipient_id()
        self.bot_reply_manager.user_cmd_apologize(recipient_id)


