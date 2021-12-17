from line_bot.models import TrainInfo

def create_single_text_message(message):
    for objects in TrainInfo.objects.all():
        if message==objects.operator:
            message=''
            for operator in TrainInfo.objects.filter(operator = objects.operator):
                message+= operator.railway + ' : '+ objects.information + '\n'
        
            test_message=[
                {
                    'type' : 'text',
                    'text' : message
                }
            ]
            return test_message
        
