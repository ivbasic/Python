from pychpp import CHPP

#### pychpp  - framagit.org/Pierre86/pychpp #######################################
    
# Set consumer_key and consumer_secret provided for your app by Hattrick
consumer_key = ''
consumer_secret = ''
    
# Initialize CHPP instance
chpp = CHPP(consumer_key, consumer_secret)
    
# Get url, request_token and request_token_secret to request API access
# You can set callback_url and scope
auth = chpp.get_auth() #callback_url="www.mycallbackurl.com", scope=""
  
# auth['url'] contains the url to which the user can grant the application
# access to the Hattrick API
# Once the user has entered their credentials,
# a code is returned by Hattrick (directly or to the given callback url)
auth['url']
code = ""

# Get access token from Hattrick
# access_token['key'] and access_token['secret'] have to be stored
# in order to be used later by the app
access_token = chpp.get_access_token(
                request_token=auth["request_token"],
                request_token_secret=auth["request_token_secret"],
                code=""
                )

# Once you have obtained access_token for a user
# You can use it to call Hattrick API
chpp = CHPP(consumer_key,
            consumer_secret,
            access_token['key'],
            access_token['secret'],
            )

###################################################################################

transfer = chpp.transfers_team(ht_id=156197, page_index="all")
transfer.transfer_list

my_ex_player_id_listed = []
for item in (transfer.transfer_list):
    item = str(item)
    if ")> S - " in item:
        my_ex_player_id = int(item.split('(')[-1].split(')')[0])
        print (f"Processing ID {my_ex_player_id}...")
        if my_ex_player_id != 0:
            try:
                player = chpp.player(ht_id=my_ex_player_id)
                if (player.is_transfer_listed) == True:
                    # add player ID to list
                    my_ex_player_id_listed.append(my_ex_player_id)
            except:
                continue
                # print (f"Player with ID is {my_ex_player_id} fired.")
        else:
            continue
            # print (f"Player with ID is {my_ex_player_id} fired.")
            
print(f"You have players on tranfer list! \nID: {my_ex_player_id_listed}")

