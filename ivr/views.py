from django_twilio.decorators import twilio_view
from twilio.twimi import Respose

@twilio_view
def gather_digits(request):
    twilio_response=Response()
    
    with twilio_response.gather(action='https://www.twilio.com/blog/respond/', numDigits=1) as g:
        g.say('Press one for a song, two to recieve an sms')
        g.pause(lenght=1)
        g.say('Press one for a song, two to recieve an sms')
return twilio_response