from twitter_bot.worker import ALL_TRAIN_OPERATORS, ALL_TRAIN_LINES

class QuickrepOptionManager:
    def __init__(self):
        pass

    def default_options(self):
        """Return list of default options like 'Home', 'Help' button"""
        default_option = [
                {
                    "label": "ð  ããžã ",
                    "description": "ããžã ãļåļ°ã",
                    "metadata": "home"
                },
                # {
                #     "label": "â Help",
                #     "description": "Do you need help?",
                #     "metadata": "help"
                # }
        ]
        return default_option

    def CHECK_DELAY_all_operator_options(self):
        """Return list of all operator for checking current delay state. For choosing operator to follow train line, use follow_delay_all_operator_options()"""
        quickrep_options = []
        for number, operator in enumerate(ALL_TRAIN_OPERATORS, start=1):
            quickrep_option = {
                'label': f'ðð {number}. {operator}',
                'description': f'{operator}ãŪč·Ŋį·ãčĶãã',
                'metadata': f'check_delay#{operator}'
            }
            quickrep_options.append(quickrep_option)
        # add default options
        quickrep_options.extend(self.default_options())
        return quickrep_options 

    def CHECK_DELAY_all_trainline_of_specific_operator_one_page_options(self, operator_name):
        quickrep_options = []
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name]

        # if operator has <= 17 trainlines
        for number, trainline in enumerate(all_train_lines_in_operator, start=1):
            quickrep_option = {
                'label': f'ðð {number}. {trainline}',
                'description': f'{trainline}ãŪéčĄæå ąãčĶãã',
                'metadata': f'check_delay#get_status#{operator_name}#{trainline}#0'
                # the last number 0 is the page number, because one page -> 0
            }
            quickrep_options.append(quickrep_option)

        # add return button
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': 'return_to#check_delay_info'
        }
        quickrep_options.append(return_option)
        quickrep_options.extend(self.default_options())
        return quickrep_options
        
    def CHECK_DELAY_all_trainline_of_specific_operator_first_page_options(self, operator_name):
        """Quick reply when number of item > 20 and is the first page, have 'Next' option"""
        quickrep_options = []
        # because have 'Next', 'Back', 2 default buttons -> 16 options remaining
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][:16]
        for number, trainline in enumerate(all_train_lines_in_operator, start=1):
            quickrep_option = {
                'label': f'ðð {number}. {trainline}',
                'description': f'{trainline}ãŪéčĄæå ąãčĶãã',
                'metadata': f'check_delay#get_status#{operator_name}#{trainline}#0'
            }
            quickrep_options.append(quickrep_option)
        # add return button
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': 'return_to#check_delay_info'
        }
        # add continue button
        continue_option = {
            'label': 'âĄïļ æŽĄãŪããžãļ',
            'description': 'æŽĄãŪããžãļãļæĨã',
            'metadata': f'continue#check_delay#{operator_name}#1'
        }
        quickrep_options.extend([return_option, continue_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def CHECK_DELAY_all_trainline_of_specific_operator_middle_page_options(self, operator_name, page:int):
        quickrep_options = []
        # because have 'Next', 'Back', 2 default buttons -> 16 options remaining
        start_index = page*16
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][start_index:start_index+16]
        for number, trainline in enumerate(all_train_lines_in_operator, start=start_index+1):
            quickrep_option = {
                'label': f'ðð {number}. {trainline}',
                'description': f'{trainline}ãŪéčĄæå ąãčĶãã',
                'metadata': f'check_delay#get_status#{operator_name}#{trainline}#{page}'
            }
            quickrep_options.append(quickrep_option)
        # add return button
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': f'return_to#check_delay#{operator_name}#{page-1}'
        }
        # add continue button
        continue_option = {
            'label': 'âĄïļ æŽĄãŪããžãļ',
            'description': 'æŽĄãŪããžãļãļæĨã',
            'metadata': f'continue#check_delay#{operator_name}#{page+1}'
        }
        quickrep_options.extend([return_option, continue_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def CHECK_DELAY_all_trainline_of_specific_operator_last_page_options(self, operator_name, page:int):
        quickrep_options = []
        # because have 'Next', 'Back', 2 default buttons -> 16 options remaining
        start_index = page*16
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][start_index:]
        for number, trainline in enumerate(all_train_lines_in_operator, start=start_index+1):
            quickrep_option = {
                'label': f'ðð {number}. {trainline}',
                'description': f'{trainline}ãŪéčĄæå ąãčĶãã',
                'metadata': f'check_delay#get_status#{operator_name}#{trainline}#{page}'
            }
            quickrep_options.append(quickrep_option)
        # add return button
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': f'return_to#check_delay#{operator_name}#{page-1}'
        }
        quickrep_options.extend([return_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def CHECK_DELAY_all_trainline_of_specific_operator_options(self, operator_name, page=0):
        """Return list of all railway in a specific operator_name
        
        @page: Twitter only allow quick reply max 20 entries. If have more, must separate different pages -> eg JREast has 37 trainlines -> need parameter page"""
        start_index = page*17
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][start_index:]

        if (page == 0) and (len(all_train_lines_in_operator) <= 17):
            return self.CHECK_DELAY_all_trainline_of_specific_operator_one_page_options(operator_name)
        elif (page == 0) and (len(all_train_lines_in_operator) > 17):
            return self.CHECK_DELAY_all_trainline_of_specific_operator_first_page_options(operator_name)
        elif (page != 0) and (len(all_train_lines_in_operator) > 17):
            return self.CHECK_DELAY_all_trainline_of_specific_operator_middle_page_options(operator_name, page)
        else:
            return self.CHECK_DELAY_all_trainline_of_specific_operator_last_page_options(operator_name, page)

    def CHECK_DELAY_show_trainline_delay_status_options(self, operator_name, trainline_name, page):
        """After get the delay status, give the options of all current trainlines"""
        return self.CHECK_DELAY_all_trainline_of_specific_operator_options(operator_name, page)

    #############################
    # This is part of FOLLOW_DELAY
    #############################
    # Generate quick reply event when user follow a trainline to get DM notification

    def FOLLOW_DELAY_all_operator_options(self):
        """Return list of all operator for following current delay state. For choosing operator to check train line, use check_delay_all_operator_options()"""
        quickrep_options = []
        for number, operator in enumerate(ALL_TRAIN_OPERATORS, start=1):
            quickrep_option = {
                'label': f'ðð {number}. {operator}',
                'description': f'{operator}ãŪč·Ŋį·ãčĶã',
                'metadata': f'follow_delay#show_all_trainline_in#{operator}'
            }
            quickrep_options.append(quickrep_option)
        # add default options
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def FOLLOW_DELAY_all_trainline_of_specific_operator_options(self, user_followed_trainline, operator_name, page=0):
        """Return list of all railway in a specific operator_name
        
        @page: Twitter only allow quick reply max 20 entries. If have more, must separate different pages -> eg JREast has 37 trainlines -> need parameter page"""
        start_index = page*17
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][start_index:]

        if (page == 0) and (len(all_train_lines_in_operator) <= 17):
            return self.FOLLOW_DELAY_all_trainline_of_specific_operator_one_page_options( user_followed_trainline, operator_name)
        elif (page == 0) and (len(all_train_lines_in_operator) > 17):
            return self.FOLLOW_DELAY_all_trainline_of_specific_operator_first_page_options(user_followed_trainline, operator_name)
        elif (page != 0) and (len(all_train_lines_in_operator) > 17):
            return self.FOLLOW_DELAY_all_trainline_of_specific_operator_middle_page_options(user_followed_trainline, operator_name, page)
        else:
            return self.FOLLOW_DELAY_all_trainline_of_specific_operator_last_page_options(user_followed_trainline, operator_name, page)

    def FOLLOW_DELAY_all_trainline_of_specific_operator_one_page_options(self, user_followed_trainline, operator_name):
        quickrep_options = []
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name]

        # if operator has <= 17 trainlines
        for number, trainline in enumerate(all_train_lines_in_operator, start=1):
            # check if a trainline is followed or not, change label depend on that
            if operator_name in user_followed_trainline and trainline in user_followed_trainline[operator_name]:
                quickrep_label = f'ðâ {number}. {trainline} [ããĐã­ãžäļ­]'
            else:
                quickrep_label = f'ðð {number}. {trainline}'

            quickrep_option = {
                'label': quickrep_label,
                'description': f'éčĄæå ąãããĐã­ãžããã',
                'metadata': f'follow_delay#follow_status_of#{operator_name}#{trainline}#0'
                # the last number 0 is the page number, because one page -> 0
            }
            quickrep_options.append(quickrep_option)

        # add return button
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': 'return_to#follow_delay#show_all_operator'
        }
        quickrep_options.append(return_option)
        quickrep_options.extend(self.default_options())
        return quickrep_options    

    def FOLLOW_DELAY_all_trainline_of_specific_operator_first_page_options(self,user_followed_trainline, operator_name):
        """Quick reply when number of item > 20 and is the first page, have 'Next' option"""
        quickrep_options = []
        # because have 'Next', 'Back', 2 default buttons -> 16 options remaining
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][:16]
        for number, trainline in enumerate(all_train_lines_in_operator, start=1):
            # check if a trainline is followed or not, change label depend on that
            if operator_name in user_followed_trainline and trainline in user_followed_trainline[operator_name]:
                quickrep_label = f'ðâ {number}. {trainline} [ããĐã­ãžäļ­]'
            else:
                quickrep_label = f'ðð {number}. {trainline}'

            quickrep_option = {
                'label': quickrep_label,
                'description': f'éčĄæå ąãããĐã­ãžããã',
                'metadata': f'follow_delay#follow_status_of#{operator_name}#{trainline}#0'
            }
            quickrep_options.append(quickrep_option)
        # add return button
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': 'return_to#follow_delay#show_all_operator'
        }
        # add continue button
        continue_option = {
            'label': 'âĄïļ æŽĄãŪããžãļ',
            'description': 'æŽĄãŪããžãļãļæĨã',
            'metadata': f'continue#follow_delay#show_all_trainline_in#{operator_name}#1'
        }
        quickrep_options.extend([return_option, continue_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def FOLLOW_DELAY_all_trainline_of_specific_operator_middle_page_options(self, user_followed_trainline, operator_name, page:int):
        quickrep_options = []
        # because have 'Next', 'Back', 2 default buttons -> 16 options remaining
        start_index = page*16
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][start_index:start_index+16]
        for number, trainline in enumerate(all_train_lines_in_operator, start=start_index+1):
            # check if a trainline is followed or not, change label depend on that
            if operator_name in user_followed_trainline and trainline in user_followed_trainline[operator_name]:
                quickrep_label = f'ðâ {number}. {trainline} [ããĐã­ãžäļ­]'
            else:
                quickrep_label = f'ðð {number}. {trainline}'

            quickrep_option = {
                'label': quickrep_label,
                'description': f'éčĄæå ąãããĐã­ãžããã',
                'metadata': f'follow_delay#follow_status_of#{operator_name}#{trainline}#{page}'
            }
            quickrep_options.append(quickrep_option)
        # add return button
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': f'return_to#follow_delay#show_all_trainline_in#{operator_name}#{page-1}'
        }
        # add continue button
        continue_option = {
            'label': 'âĄïļ æŽĄãŪããžãļ',
            'description': 'æŽĄãŪããžãļãļæĨã',
            'metadata': f'continue#follow_delay#show_all_trainline_in#{operator_name}#{page+1}'
        }
        quickrep_options.extend([return_option, continue_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def FOLLOW_DELAY_all_trainline_of_specific_operator_last_page_options(self, user_followed_trainline, operator_name, page:int):
        quickrep_options = []
        # because have 'Next', 'Back', 2 default buttons -> 16 options remaining
        start_index = page*16
        all_train_lines_in_operator = ALL_TRAIN_LINES[operator_name][start_index:]
        for number, trainline in enumerate(all_train_lines_in_operator, start=start_index+1):
            # check if a trainline is followed or not, change label depend on that
            if operator_name in user_followed_trainline and trainline in user_followed_trainline[operator_name]:
                quickrep_label = f'ðâ {number}. {trainline} [ããĐã­ãžäļ­]'
            else:
                quickrep_label = f'ðð {number}. {trainline}'
        
            quickrep_option = {
                'label': quickrep_label,
                'description': f'éčĄæå ąãããĐã­ãžããã',
                'metadata': f'follow_delay#follow_status_of#{operator_name}#{trainline}#{page}'
            }
            quickrep_options.append(quickrep_option)
        # add return button
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': f'return_to#follow_delay#show_all_trainline_in#{operator_name}#{page-1}'
        }
        quickrep_options.extend([return_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def FOLLOW_DELAY_show_trainline_follow_status_options(self, user_followed_trainline, operator_name, trainline_name, page):
        """After showing follow status, give the options of all current trainlines"""
        return self.FOLLOW_DELAY_all_trainline_of_specific_operator_options(user_followed_trainline, operator_name, page)

    #########################################
    # Unfollow delay part
    #########################################
    def UNFOLLOW_DELAY_show_all_following_trainline(self, user_followed_trainline_dict, page:int):
        """@user_followed_trainline_dict in form {operator: [trainline1, trainline2,..]...}"""
        # change from the dict -> list [(operator1, trainline1), (operator2, trainline2)]
        user_followed_trainline = []
        for operator in user_followed_trainline_dict:
            operator_trainlines = user_followed_trainline_dict[operator]
            for trainline in operator_trainlines:
                user_followed_trainline.append((operator, trainline))
        if (page == 0) and (len(user_followed_trainline) <= 18):
            return self.UNFOLLOW_DELAY_show_all_following_trainline_onepage(user_followed_trainline, 0)
        elif (page == 0) and (len(user_followed_trainline) > 18):
            return self.UNFOLLOW_DELAY_show_all_following_trainline_first_page(user_followed_trainline, 0)
        elif (page != 0) and ( (len(user_followed_trainline)-1)%16==0 ):
            return self.UNFOLLOW_DELAY_show_all_following_trainline_last_page(user_followed_trainline, page)
        elif (page != 0) and ((page+1)*16+1 <= len(user_followed_trainline)):
            return self.UNFOLLOW_DELAY_show_all_following_trainline_middle_page(user_followed_trainline, page)
        else:
            return self.UNFOLLOW_DELAY_show_all_following_trainline_last_page(user_followed_trainline, page)

    def UNFOLLOW_DELAY_show_all_following_trainline_onepage(self, user_followed_trainline, page=0):
        """If the number of trainline not exceed max num of quickrep -> use this function
        
        @user_followed_trainline in form list of tuple [(operator1, trainline1),...]"""
        page = 0
        quickrep_options = []
        number = 1
        for data in user_followed_trainline:
            operator = data[0]
            trainline = data[1]
            quickrep_option = {
            'label': f"â {number}. {trainline} ({operator})",
            'description': f'č·Ŋį·ãããĐã­ãžč§ĢéĪããã',
            'metadata': f'unfollow_delay#unfollow_specific_trainline#{operator}#{trainline}#page#0'
            }
            # the page in above metadata show the page of this option if the number of option too large, need to split to multiple page
            quickrep_options.append(quickrep_option)
            number += 1
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def UNFOLLOW_DELAY_show_all_following_trainline_first_page(self, user_followed_trainline, page=0):
        """The number of following trainline a lot -> span multiple quickrep page, this page has continue button"""
        page = 0
        quickrep_options = []
        # max quickrep = 20, 2 default, 1 next button -> 
        for number, data in enumerate(user_followed_trainline[:17], start=1):
            operator = data[0]
            trainline = data[1]
            quickrep_option = {
            'label': f"â {number}. {trainline} ({operator})",
            'description': f'č·Ŋį·ãããĐã­ãžč§ĢéĪããã',
            'metadata': f'unfollow_delay#unfollow_specific_trainline#{operator}#{trainline}#page#0'
            }
            # the page in above metadata show the page of this option if the number of option too large, need to split to multiple page
            quickrep_options.append(quickrep_option)

        continue_option = {
            'label': 'âĄïļ æŽĄãŪããžãļ',
            'description': 'æŽĄãŪããžãļãļæĨã',
            'metadata': f'continue#unfollow_delay#show_all_following_trainlines#page#1'
        }   
        quickrep_options.append(continue_option)
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def UNFOLLOW_DELAY_show_all_following_trainline_middle_page(self, user_followed_trainline, page:int):
        """The middle page of following trainline, will have 'Back' and 'Continue' options"""
        quickrep_options = []
        # max quickrep = 20, 2 default, 1 next button
        start_index = page*16 + 1
        for number, data in enumerate(user_followed_trainline[start_index:start_index+16], start=start_index+1):
            operator = data[0]
            trainline = data[1]
            quickrep_option = {
            'label': f"â {number}. {trainline} ({operator})",
            'description': f'č·Ŋį·ãããĐã­ãžč§ĢéĪããã',
            'metadata': f'unfollow_delay#unfollow_specific_trainline#{operator}#{trainline}#page#{page}'
            }
            # the page in above metadata show the page of this option if the number of option too large, need to split to multiple page
            quickrep_options.append(quickrep_option)

        continue_option = {
            'label': 'âĄïļ æŽĄãŪããžãļ',
            'description': 'æŽĄãŪããžãļãļæĨã',
            'metadata': f'continue#unfollow_delay#show_all_following_trainlines#page#{page+1}'
        }   
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': f'return_to#unfollow_delay#show_all_following_trainline#page#{page-1}'
        }
        quickrep_options.extend([continue_option, return_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options

    def UNFOLLOW_DELAY_show_all_following_trainline_last_page(self, user_followed_trainline, page:int):
        """The last page of following trainline, will have back button"""
        quickrep_options = []
        # max quickrep = 20, 2 default, 1 next button
        start_index = page*16 + 1
        for number, data in enumerate(user_followed_trainline[start_index:], start=start_index+1):
            operator = data[0]
            trainline = data[1]
            quickrep_option = {
            'label': f"â {number}. {trainline} ({operator})",
            'description': f'č·Ŋį·ãããĐã­ãžč§ĢéĪããã',
            'metadata': f'unfollow_delay#unfollow_specific_trainline#{operator}#{trainline}#page#{page}'
            }
            # the page in above metadata show the page of this option if the number of option too large, need to split to multiple page
            quickrep_options.append(quickrep_option)
  
        return_option = {
            'label': 'âŽïļ åãŪããžãļ',
            'description': 'åãŪããžãļãļåļ°ã',
            'metadata': f'return_to#unfollow_delay#show_all_following_trainline#page#{page-1}'
        }
        quickrep_options.extend([return_option])
        quickrep_options.extend(self.default_options())
        return quickrep_options


    ########################################
    # Home option
    ########################################
    def home_options(self):
        quickrep_options = [
            {
                'label': 'ð WebãĩãĪããŦæĨã',
                'description': 'ããĢãĻæå ąãããĨãžãđ...',
                'metadata': 'visit_website'
            },
            {
                'label': 'ð č·Ŋį·ãŪéčĄæå ąãčĶã',
                'description': 'æąäšŽã§įūåĻãŪ86č·Ŋį·ãŪéčĄæå ą',
                'metadata': 'check_delay_info'
            },
            {
                'label': 'ð č·Ŋį·ãŪéčĄæå ąãããĐã­ãžãã',
                'description': 'ããĐã­ãžãããč·Ŋį·ãŪéåŧķãŪæãDMãåäŋĄãã',
                'metadata': f'follow_delay#show_all_operator'
            },
            {
                'label': 'â č·Ŋį·ãŪéčĄæå ąãããĐã­ãžč§ĢéĪãã',
                'description': 'č·Ŋį·ãŪéåŧķéįĨãŪåäŋĄãåæ­Ēãã',
                'metadata': 'unfollow_delay#show_all_following_trainline'
            }
        ]
        return quickrep_options