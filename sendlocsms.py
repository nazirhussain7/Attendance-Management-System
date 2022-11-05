import requests
import json
    # mention url
url = "https://www.fast2sms.com/dev/bulk"

smssent="9448650440"
my_data = {
        # Your default Sender ID
        'sender_id': 'FSTSMS',

        # Put your message here!

        'message': "Send Your Location With ClassID, StudCount and Date",

        'language': 'english',
        'route': 'p',

        # You can send sms to multiple numbers
        # separated by comma.
        'numbers': smssent
    }

    # create a dictionary
headers = {
        'authorization': 'v54Wb3jqnrKBiJUdL2S7PwE9NpQxmHyCGA8YgsfTkROXuaZ6MVAqNMnyJGOT2o7VzWIdCHt8h4ZbEl6D',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }

    # make a post request
response = requests.request("POST", url, data=my_data, headers=headers)

returned_msg = json.loads(response.text)

    # print the send message
print(returned_msg['message'])
