from line_bot.models import TrainInfo

def create_single_text_message(message):
    if message=='1':
        message=''
        for op in TrainInfo.objects.filter(operator_en='JR East'):
            message+=op.railway_en + '( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message

    if message=='2':
        message='' #Tobu
        for op in TrainInfo.objects.filter(operator_en='Tobu Railway'):
            message+=op.railway_en + '( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='3':
        message='' #Toei
        for op in TrainInfo.objects.filter(operator_en='Tokyo Metropolitan Bureau of Transportation'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='4':
        message='' #SendaiMunicipal
        for op in TrainInfo.objects.filter(operator_en='Transportation Bureau City of Sendai'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='5':
        message='' #YokohamaMunicipal
        for op in TrainInfo.objects.filter(operator_en='Transportation Bureau, City of Yokohama'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='6':
        message='' #TokyoMetro
        for op in TrainInfo.objects.filter(operator_en='Tokyo Metro'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='7':
        message='' #MIR
        for op in TrainInfo.objects.filter(operator_en='Metropolitan Intercity Railway'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='8':
        message='' #TamaMonorail
        for op in TrainInfo.objects.filter(operator_en='Tokyo Tama Intercity Monorail'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='9':
        message='' #Keio
        for op in TrainInfo.objects.filter(operator_en='Keio Corporation'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='10':
        message='' #TWR
        for op in TrainInfo.objects.filter(operator_en='Tokyo Waterfront Area Rapid Transit'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='11':
        message='' #Tokyu
        for op in TrainInfo.objects.filter(operator_en='Tokyu Corporation'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='12':
        message='' #Seibu
        for op in TrainInfo.objects.filter(operator_en='Seibu Railway'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='13':
        message='' #Keikyu
        for op in TrainInfo.objects.filter(operator_en='Keikyu Corporation'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message
    
    if message=='14':
        message='' #Keisei
        for op in TrainInfo.objects.filter(operator_en='Keisei Electric Railway'):
            message+=op.railway_en +'( '+ op.railway_ja+ ' )' + ' : ' + op.information_en+ '( '+ op.information_ja +' )'+'\n'
        test_message=[
            {
                'type' : 'text',
                'text' : message
            }
            ]
        return test_message 
        
