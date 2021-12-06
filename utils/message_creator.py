def create_single_text_message(message):
    if message=='thank you':
        message='welcome!'
    test_message=[
        {
            'type' : 'text',
            'text' : message
        }
    ]
    return test_message