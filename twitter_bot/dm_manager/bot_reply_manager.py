from tweepy.models import User
from twitter_bot.dm_manager.twitter_api_manager import APIManager
from .quick_reply_manager import QuickrepOptionManager
from train_delay.models import TrainInfo
from twitter_bot.models import UserRegistration
from twitter_bot.worker.post_delay_tweet import current_operation_state

class TrainFollowerManager:
    def __init__(self):
        """Check if user already follow a trainline, register new follow, delete current follow"""
        pass

    def get_follow_status_of(self, user_twitter_id, operator_name, trainline_name):
        """Return 'already' if already follow, 'none' otherwise"""
        all_user_follow_data = UserRegistration.objects.all()
        query_result = all_user_follow_data.filter(user_twitter_id=user_twitter_id).filter(followed_operator_name=operator_name).filter(followed_trainline_name=trainline_name)
        if len(query_result) == 0:
            return 'none'
        else:
            return 'already'

    def get_all_trainline_follow_of_user(self, user_twitter_id):
        """Return dict contain all followed trainline of user with given id. The dict form is {train_operator_A: [trainline1, trainline2,...], ...}"""
        all_followed_trainline_data = UserRegistration.objects.all().filter(user_twitter_id=user_twitter_id)
        if len(all_followed_trainline_data) == 0:
            return {}
        else:
            return_data = {}
            for trainline_data in all_followed_trainline_data:
                operator = trainline_data.followed_operator_name
                trainline = trainline_data.followed_trainline_name
                if operator not in return_data:
                    return_data[operator] = [trainline]
                if (operator in return_data) and (trainline not in return_data[operator]):
                    return_data[operator].append(trainline)
            return return_data 

    def register_new_follow(self, user_twitter_id, operator_name, trainline_name):
        new_record = UserRegistration(user_twitter_id=user_twitter_id, followed_operator_name=operator_name, followed_trainline_name=trainline_name)
        new_record.save()  

class BotReplyManager:
    api_manager = APIManager() 
    quickreply_manager = QuickrepOptionManager()
    train_follower_manager = TrainFollowerManager()
    def __init__(self):
        """Handle DM activities of bot"""
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

    # Note: access train database often has error -> should add try-catch to handle
    def CHECK_DELAY_show_trainline_delay_status(self, recipient_id, operator_name, trainline_name, page):
        """Display the information of selected trainline, green circle if operate normally, orange circle if delay occur"""
        quickrep_options = self.quickreply_manager.CHECK_DELAY_show_trainline_delay_status_options(operator_name, trainline_name, page)
        try:
            trainline_status_object = TrainInfo.objects.filter(operator_ja=operator_name).filter(railway_ja=trainline_name)[0]
            trainline_status = current_operation_state(trainline_status_object.information_ja)
            if trainline_status == "normal":
                response = f"🟢 {trainline_status_object.railway_ja}: {trainline_status_object.information_ja}"
            else:
                response = f"🟠 {trainline_status_object.railway_ja}: {trainline_status_object.information_ja}"
            self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)
        except Exception:
            response = f"There is a problem with the service. Please try again later 🙇‍♂️"
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

    def FOLLOW_DELAY_show_all_operators_list(self, recipient_id):
        """Show list of all operators to FOLLOW delay"""
        quickrep_options = self.quickreply_manager.FOLLOW_DELAY_all_operator_options()
        response = "Please choose 1 operator to see all trainlines belong to"
        self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)
    
    def FOLLOW_DELAY_show_all_trainline_of_specific_operator(self, recipient_id, operator_name, page=0):
        """Show list of all trainline in a specific operator name, eg all trainline of JREast"""
        user_followed_trainline = self.train_follower_manager.get_all_trainline_follow_of_user(recipient_id)
        quickrep_options = self.quickreply_manager.FOLLOW_DELAY_all_trainline_of_specific_operator_options(user_followed_trainline, operator_name, page)
        response = "Choose a trainline to follow its delay status"
        self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)

    def FOLLOW_DELAY_show_trainline_follow_status(self, recipient_id, operator_name, trainline_name, page):
        """If the user already follow a trainline -> send already followed, if not, notify follow successfully"""
        print(f"FOLLOW_DELAY_show_trainline_follow_status run!!")
        print(f"\nFollowed trainline: {self.train_follower_manager.get_all_trainline_follow_of_user(recipient_id)}")
        already_followed = self.train_follower_manager.get_follow_status_of(recipient_id, operator_name, trainline_name) == 'already'

        if already_followed:
            response = "You already followed this trainline! Let's follow other trainline!"
        else:
            self.train_follower_manager.register_new_follow(recipient_id, operator_name, trainline_name)
            response = "You followed this trainline!"

        user_followed_trainline = self.train_follower_manager.get_all_trainline_follow_of_user(recipient_id)
        quickrep_options = self.quickreply_manager.FOLLOW_DELAY_show_trainline_follow_status_options(user_followed_trainline, operator_name, trainline_name, page)
        self.api_manager.send_direct_message(recipient_id, response, quick_reply_options=quickrep_options)
