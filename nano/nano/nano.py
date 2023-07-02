import random, os, sys, json, time

def clear_screen():

    kern = sys.platform
    if kern == 'linux':
        os.system('clear')
    else:
        os.system('cls')

def firstLaunch():
    try:

        clear_screen()
        query = input(f'{front} Is this your first time using Nano (will install all needed libraries)? (default=n/no): ')
        if query.lower() == 'y':
            print('Installing requests...')
            os.system('pip install requests pyperclip customtkinter')
            clear_screen()
    except KeyboardInterrupt:
        clear_screen()
        print(f'{front} Exiting Nano')
        sys.exit()

import requests, pyperclip, customtkinter

dashboard = r"""                       
  ____ _____    ____   ____  
 /    \\__  \  /    \ /  _ \ 
|   |  \/ __ \|   |  (  <_> )
|___|  (____  /___|  /\____/ 
     \/     \/     \/        
"""
dashboard_ap = r"""
_____  ______                                    
\__  \ \____ \                                   
 / __ \|  |_> >                                  
(____  /   __/                                   
     \/|__| 
"""
dashboard_aa = r"""                                                 
_____  _____                                     
\__  \ \__  \                                    
 / __ \_/ __ \_                                  
(____  (____  /                                  
     \/     \/
"""
dashboard_aac = r"""
_____  _____    ____                             
\__  \ \__  \ _/ ___\                            
 / __ \_/ __ \\  \___                            
(____  (____  /\___  >                           
     \/     \/     \/ 
"""
dashboard_packgen = r"""
                     __                          
___________    ____ |  | __  ____   ____   ____  
\____ \__  \ _/ ___\|  |/ / / ___\_/ __ \ /    \ 
|  |_> > __ \\  \___|    < / /_/  >  ___/|   |  \
|   __(____  /\___  >__|_ \\___  / \___  >___|  /
|__|       \/     \/     \/_____/      \/     \/
"""
dashboard_topicgen = r"""
  __                .__
_/  |_  ____ ______ |__| ____   ____   ____   ____
\   __\/  _ \\____ \|  |/ ___\ / ___\_/ __ \ /    \ 
 |  | (  <_> )  |_> >  \  \___/ /_/  >  ___/|   |  \
 |__|  \____/|   __/|__|\___  >___  / \___  >___|  /
             |__|           \/_____/      \/     \/ 
"""


options = r"""
******************************************
**                                      **
**  Working:                            **
**                                      **
**  [1] Auto Pressure                   **
**  [2] AFK Alert                       **
**  [3] Auto AFK Check (custom unicode) **
**  [4] Packgen/Perpetual               **
**    └─ [4.1] Topicgen                 **
**    └─ [4.2] Packgen GUI              **
**                                      **
******************************************
**                                      **
**  In development/coming soon:         **
**                                      **
**  [5]Anydesk Hider (in production)    **
**  [6]Misc scripts (in production)     **
**                                      **
******************************************
"""

with open('ascii.txt', 'r') as ascii_file:
    custom_ascii_art = ascii_file.read()


with open('settings.json', 'r') as config:
    settings = json.load(config)

# -------String Values------- #
token = settings.get('token')
front = settings.get('front')
send_front = settings.get('send_front')

# -------Integer Values------- #

channel = settings.get('channel')
server = settings.get('server')
delay = settings.get('delay')
user_id = settings.get('user_id')
rate_limit = settings.get('rate_limit')
target = settings.get('target')

# -------Boolean Values------- #

dms = settings.get('dms')
server_check = settings.get('server_check')
single_server = settings.get('single_server')
rate_limiting = settings.get('rate_limiting')
fake_ping = settings.get('fake_ping')
logs = settings.get('logs')
discord = settings.get('discord')
custom_ascii = settings.get('custom_ascii')

fake_ping_text = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'
global_headers = {'authorization': f'{token}'}

packgen_output = 'packs.txt'
topicgen_output = 'topicgen.txt'

def lols_send():
    sent_messages = set()
    for _ in range(5):
        lols = random.choice(open('wordlists_2/lols.txt', 'r').readlines()).strip()

        while lols in sent_messages:
            lols = random.choice(open('wordlists_2/lols.txt', 'r').readlines()).strip()
        sent_messages.add(lols)

        lols_send_request = requests.post(
            f'https://discord.com/api/v9/channels/{channel}/messages',
            headers={'authorization': f'{token}'},
            data={'content': f'{send_front} {lols}'},
        )
        ap_typing_url = f'https://discord.com/api/v9/channels/{channel}/typing'
        ap_typing_post = requests.post(ap_typing_url, headers=global_headers)

        if lols_send_request.status_code == 200:
            print(f'{front} Sent | {send_front} {lols} | successfully')

        if lols_send_request.status_code == 429:
            if rate_limiting == True:
                print(f'{front} Ratelimiting | {send_front} {lols} | retrying in {rate_limit} seconds')
                time.sleep(rate_limit)

            else:
                print(f'{front} Ratelimiting | {send_front} {lols} | retrying')
        if lols_send_request.status_code == 401:
            print(f'{front} Invalid token')

def pack_names_send():
    sent_messages = set()
    for _ in range(5):
        pack_names = random.choice(open('wordlists_2/pack_names.txt', 'r').readlines()).strip()
        
        while pack_names in sent_messages:
            pack_names = random.choice(open('wordlists_2/pack_names.txt', 'r').readlines()).strip()
        
        sent_messages.add(pack_names)
        
        pack_names_send_request = requests.post(
            f'https://discord.com/api/v9/channels/{channel}/messages',
            headers=global_headers,
            data={'content': f'{send_front} {pack_names}'}
        )
        ap_typing_url = f'https://discord.com/api/v9/channels/{channel}/typing'
        ap_typing_post = requests.post(ap_typing_url, headers=global_headers)

        if pack_names_send_request.status_code == 200:
            print(f'{front} Sent | {send_front} {pack_names} | successfully')
        
        if pack_names_send_request.status_code == 429:
            if rate_limiting == True:
                print(f'{front} Ratelimiting | {send_front} {pack_names} | retrying in {rate_limit} seconds')
                time.sleep(rate_limit)
            else:
                print(f'{front} Ratelimiting | {send_front} {pack_names} | retrying')
        if pack_names_send_request.status_code == 401:
            print(f'{front} Invalid token')

def insults_send():
    sent_messages = set()
    for _ in range(5):

        insults = random.choice(open('wordlists_2/insults.txt', 'r').readlines()).strip()
        
        while insults in sent_messages:
            insults = random.choice(open('wordlists_2/insults.txt', 'r').readlines()).strip()

        insults_send_request = requests.post(
            f'https://discord.com/api/v9/channels/{channel}/messages',
            headers=global_headers,
            data={'content': f'{send_front} {insults}'},
        )
        ap_typing_url = f'https://discord.com/api/v9/channels/{channel}/typing'
        ap_typing_post = requests.post(ap_typing_url, headers=global_headers)

        if insults_send_request.status_code == 200:
            print(f'{front} Sent | {send_front} {insults} | successfully')
        
        if insults_send_request.status_code == 429:
            if rate_limiting == True:
                print(f'{front} Ratelimiting | {send_front} {insults} | retrying in {rate_limit} seconds')
                time.sleep(rate_limit)
            else:
                print(f'{front} Ratelimiting | {send_front} {insults} | retrying')
        if insults_send_request.status_code == 401:
            print(f'{front} Invalid token')

def ap():
    try:
        while True:
            
            if custom_ascii == True:
                print(custom_ascii_art)
            
            else:
                print(dashboard_ap)
            funkies = [lols_send, pack_names_send, insults_send]
            random.choice(funkies)()
            time.sleep(delay)
            clear_screen()

    except KeyboardInterrupt:
        clear_screen()
        nano()
def aa():

    if custom_ascii == True:
        print(custom_ascii_art)
            
    else:
        print(dashboard_aa)
    
    print(f'{front} messages appear ontop, may take some time to load.\n')

    grab_channels = f'https://discord.com/api/v8/guilds/{server}/channels'
    dm_channels_url = 'https://discord.com/api/v8/users/@me/channels'

    aa_triggers = ['afk']
    aa_ping = [f'<@!{user_id}>']
    sent_messages = [] 
    try:
            
        while True:
            global_headers = {'authorization': f'{token}'}
            get_channels = requests.get(grab_channels, headers=global_headers)

            if get_channels.status_code == 401:
                input(f'{front} Invalid token, press enter to go back to Nano\'s Dashboard: ')
                nano()

            get_channels_json = get_channels.json()

            for channels in get_channels_json:
                channelids = channels.get('id')
                channelnames = channels.get('name')
                checkchannels = channelids

                aa_url = f'https://discord.com/api/v9/channels/{checkchannels}/messages?limit=25'
                if server_check == True:

                    aa_msgs = requests.get(aa_url, headers=global_headers)

                    if aa_output := aa_msgs.json():
                        for msg in aa_output:
                            if content := msg.get('content'):
                                if author := msg.get('author'):
                                    message_id = msg.get('id')
                                    if message_id in sent_messages: 
                                        continue
                                    else:
                                        sent_messages.append(message_id)
                                    username = author.get('username')
                                    discriminator = author.get('discriminator')

                                    # server term
                                    for aa_trigger in aa_triggers:
                                        if aa_trigger in content:
                                            print(f'{front} #{channelnames} | {username}#{discriminator}: {content}')
                                    for aa_ping_check in aa_ping:
                                        if aa_ping_check in content:
                                            print(f'{front} #{channelnames} | {username}#{discriminator} pinged you')
                                            
                if server_check == False and single_server == True:
                    for channels in get_channels_json:
                        channelids = channels.get('id')
                        channelnames = channels.get('name')
                        checkchannels = channelids
                        aa_url = f'https://discord.com/api/v9/channels/{checkchannels}/messages?limit=100'
                        global_headers = {'authorization': f'{token}'}
                        aa_msgs = requests.get(aa_url, headers=global_headers)
                        
                        if aa_output := aa_msgs.json():
                            for msg in aa_output:
                                if content := msg.get('content'):
                                    if author := msg.get('author'):
                                        message_id = msg.get('id')
                                        if message_id in sent_messages:
                                            continue
                                        else:
                                            sent_messages.append(message_id)
                                        username = author.get('username')
                                        discriminator = author.get('discriminator')
                                        for aa_trigger in aa_triggers:
                                            if aa_trigger in content:
                                                print(f'{front} #{channelnames} | {username}#{discriminator}: {content}')
                                        for aa_ping_check in aa_ping:
                                            if aa_ping_check in content:
                                                print(f'{front} #{channelnames} | {username}#{discriminator} pinged you')


                if dms == True:
                    dm_channels = requests.get(dm_channels_url, headers=global_headers)
                    
                    dm_channels_json = dm_channels.json()
                    for channel in dm_channels_json:
                        dm_channel_id = channel['id']
                        dm_channel_url = f'https://discord.com/api/v8/channels/{dm_channel_id}/messages?limit=15'
                        dm_messages = requests.get(dm_channel_url, headers=global_headers)
                        dm_messages_json = dm_messages.json()
                        for dm_msg in dm_messages_json:
                            dm_msg_content = dm_msg.get('content')
                            dm_message_id = dm_msg.get('id')
                            if dm_message_id in sent_messages:
                                continue
                            else:
                                sent_messages.append(dm_message_id) 
                            if dm_msg_author := dm_msg.get('author'):
                                dm_msg_username = dm_msg_author.get('username')
                                dm_msg_discriminator = dm_msg_author.get('discriminator')
                                for aa_trigger in aa_triggers: # dm term
                                    if aa_trigger in dm_msg_content:
                                        print(f'{front} {dm_msg_username}#{dm_msg_discriminator}: {dm_msg_content} in DMs')
                        

            time.sleep(delay)
    except KeyboardInterrupt:
        clear_screen()
        nano()

def number_to_unicode(number):
    number_str = str(number)
    return "".join(
        {
            '0': "0",
            '1': "1",
            '2': "2",
            '3': "3",
            '4': "4",
            '5': "5",
            '6': "6",
            '7': "7",
            '8': "8",
            '9': "9",
            
        }[digit]
        for digit in number_str)

def aac():  # sourcery skip: merge-nested-ifs
    try:

        if custom_ascii == True:
            print(custom_ascii_art)
                
        else:
            print(dashboard_aac)

        print(f'{front} Copied a custom AFK Check unicode to your clipboard. (will not be picked up by anti afk stuff)')
        pyperclip.copy('ａｆｋ ｃｈｅｃｋ')

        up_to = int(input(f'{front} How far do you want to count to?: '))

        aac_url_post = f'https://discord.com/api/v9/channels/{channel}/messages'
        _ = 0

        while _ < up_to:
            custom_unicode = number_to_unicode(_+1)
            
            if fake_ping == True:
                aac_post = requests.post(aac_url_post, headers=global_headers, data={'content': f'{send_front} {custom_unicode}{fake_ping_text}<@{target}>'})
                if aac_post.status_code == 200:
                    print(f'{front} [✓] Sent: {custom_unicode} [ghostping]')
                    _ += 1
                elif aac_post.status_code == 429:
                    if rate_limiting == True:
                        print(f'{front} [X] Ratelimited, retrying in {rate_limit}s: {custom_unicode} [invisping]')
                        time.sleep(rate_limit)
                    else:
                        print(f'{front} [X] Ratelimited, retrying: {custom_unicode} [invisping]')
            
            elif fake_ping == False:
                aac_post = requests.post(aac_url_post, headers=global_headers, data={'content': f'{send_front} {custom_unicode}'})
                if aac_post.status_code == 200:
                    print(f'{front} Sent: {custom_unicode}')
                    _ += 1
                elif aac_post.status_code == 429:
                    if rate_limiting == True:
                        print(f'{front} [X] Ratelimited, retrying in {rate_limit}s: {custom_unicode}')
                        time.sleep(rate_limit)
                    else:
                        print(f'{front} [X] Ratelimited, retrying: {custom_unicode}')

        clear_screen()
        aac()
    
    except KeyboardInterrupt:
        clear_screen()
        nano()

def packgen():
    clear_screen()
    if custom_ascii_art == True:
        print(custom_ascii_art)

    else:

        print(dashboard_packgen)
    while True:
        try:
                
            time.sleep(delay)

            actions_by_a = random.choice(open('wordlists/actions/actions_by_a.txt', 'r').readlines()).strip()
            actions_by = random.choice(open('wordlists/actions/actions_by.txt', 'r').readlines()).strip()
            actions_standalone = random.choice(open('wordlists/actions/actions_standalone.txt', 'r').readlines()).strip()
            additions = random.choice(open('wordlists/additions/additions.txt', 'r').readlines()).strip()
            additions2 = random.choice(open('wordlists/additions/additions2.txt', 'r').readlines()).strip()
            animals = random.choice(open('wordlists/objects_misc/animals.txt', 'r').readlines()).strip()
            bodyparts_external = random.choice(open('wordlists/objects_misc/bodyparts_external.txt', 'r').readlines()).strip()
            bodyparts_internal = random.choice(open('wordlists/objects_misc/bodyparts_internal.txt', 'r').readlines()).strip()
            characters = random.choice(open('wordlists/lists/characters.txt', 'r').readlines()).strip()
            family_members = random.choice(open('wordlists/lists/family_members.txt', 'r').readlines()).strip()
            foods = random.choice(open('wordlists/objects_misc/foods.txt', 'r').readlines()).strip()
            insects = random.choice(open('wordlists/objects_misc/insects.txt', 'r').readlines()).strip()
            materials = random.choice(open('wordlists/objects_misc/materials.txt', 'r').readlines()).strip()
            names = random.choice(open('wordlists/lists/names.txt', 'r').readlines()).strip()
            numbers = random.choice(open('wordlists/person/numbers.txt', 'r').readlines()).strip()
            objects = random.choice(open('wordlists/objects_misc/objects.txt', 'r').readlines()).strip()
            races = random.choice(open('wordlists/person/races.txt', 'r').readlines()).strip()
            time_type = random.choice(open('wordlists/person/time_type.txt', 'r').readlines()).strip()
            quotes = random.choice(open('wordlists/lists/quotes.txt', 'r').readlines()).strip()

            bp = (bodyparts_external, bodyparts_internal)
            bpchoose = random.choice(bp) # chooses internal or external bodyparts

            combos = [
                f'tell me why your {family_members} got {actions_by_a} {additions} {objects}', 
                f'you got caught tryna {additions2} with your {additions} {family_members}s {objects}', 
                f'yo ass got {actions_by_a} {additions} version of {characters}',
                f'your {family_members} got {actions_by_a} {objects}',
                f'i walked in the room and saw you get {actions_by_a} {additions} {animals}',
                f'your {family_members} got caught tryna {additions2} your {additions} pet {animals}',
                f'your {family_members} beat you with a {additions} {objects}',
                f'this why your pet {animals} started {actions_standalone} your {additions} {family_members}',
                f'your {family_members} caught you eating leftover {foods} and started {actions_standalone} you',
                f'you tried riding a {objects} and fell over and got {actions_by_a} {animals} dressed up as a {foods}',
                f'yo ass got {actions_by_a} {races} {insects}',
                f'you got {actions_by_a} {additions} version of {names}',
                f'you tried {actions_standalone} your {numbers} {time_type} old {family_members}',
                f'you look like a {additions} version of your {numbers} {time_type} old {family_members}',
                f'you sound like a {races} {animals} when you sing yo ass said {quotes}',
                f'yo {races} {family_members} walked in the room and caught you {actions_standalone} your {additions} pet {animals} and started {actions_standalone} you',
                f'and then you got {actions_by_a} {races} {animals} with a {materials} {bpchoose}',
                f'yo {family_members} is in the hospital cuz you tried {actions_standalone} on them'
                ]
            
            
            choose_combo = random.choice(combos)
            with open(packgen_output, 'a') as output:
                output.write(f'\n {front} {choose_combo}')

            match logs:
                case True:
                    match discord:
                        case True:
                            send = requests.post(f'https://discord.com/api/v9/channels/{channel}/messages', data={'content': f'{send_front} {choose_combo}'}, headers=global_headers)
                            match send.status_code:
                                case 200:
                                    print(f'[🗸] {front} {choose_combo}')
                                case 429:
                                    match rate_limiting:
                                        case True:
                                            print(f'[X] {front} Ratelimited, retrying in {rate_limit}s')
                                            time.sleep(rate_limit)
                                        case False:
                                            print(f'[X] {front} Ratelimited, retrying')
                                case 401:
                                    print(f'[X] {front} Invalid token or channel ID, check your settings to validate')
                        case False:
                            print(f'{front} {choose_combo}')

                case False:
                    match discord:
                        case True:
                            send = requests.post(f'https://discord.com/api/v9/channels/{channel}/messages', data={'content': f'{send_front} {choose_combo}'}, headers=global_headers)
                            match send.status_code:
                                case 429:
                                    match rate_limiting:
                                        case True:
                                            time.sleep(rate_limit)
                                        case False:
                                            pass
                        case False:
                            pass
        except KeyboardInterrupt:
            match logs:
                case True:
                    clear_screen()
                    print(f'{front} Exiting Packgen')
                    sys.exit()
                case False:
                    clear_screen()
                    sys.exit()

def topicgen():
    try:
        if custom_ascii == True:
            print(custom_ascii_art)
        else:
            print(dashboard_topicgen)
        while True:
            time.sleep(delay)

            actions_by_a = random.choice(open('wordlists/actions/actions_by_a.txt', 'r').readlines()).strip()
            actions_by = random.choice(open('wordlists/actions/actions_by.txt', 'r').readlines()).strip()
            actions_standalone = random.choice(open('wordlists/actions/actions_standalone.txt', 'r').readlines()).strip()
            additions = random.choice(open('wordlists/additions/additions.txt', 'r').readlines()).strip()
            additions2 = random.choice(open('wordlists/additions/additions2.txt', 'r').readlines()).strip()
            animals = random.choice(open('wordlists/objects_misc/animals.txt', 'r').readlines()).strip()
            bodyparts_external = random.choice(open('wordlists/objects_misc/bodyparts_external.txt', 'r').readlines()).strip()
            bodyparts_internal = random.choice(open('wordlists/objects_misc/bodyparts_internal.txt', 'r').readlines()).strip()
            characters = random.choice(open('wordlists/lists/characters.txt', 'r').readlines()).strip()
            family_members = random.choice(open('wordlists/lists/family_members.txt', 'r').readlines()).strip()
            foods = random.choice(open('wordlists/objects_misc/foods.txt', 'r').readlines()).strip()
            insects = random.choice(open('wordlists/objects_misc/insects.txt', 'r').readlines()).strip()
            materials = random.choice(open('wordlists/objects_misc/materials.txt', 'r').readlines()).strip()
            names = random.choice(open('wordlists/lists/names.txt', 'r').readlines()).strip()
            numbers = random.choice(open('wordlists/person/numbers.txt', 'r').readlines()).strip()
            objects = random.choice(open('wordlists/objects_misc/objects.txt', 'r').readlines()).strip()
            races = random.choice(open('wordlists/person/races.txt', 'r').readlines()).strip()
            time_type = random.choice(open('wordlists/person/time_type.txt', 'r').readlines()).strip()
            quotes = random.choice(open('wordlists/lists/quotes.txt', 'r').readlines()).strip()

            bp = (bodyparts_external, bodyparts_internal)
            bpchoose = random.choice(bp) # chooses internal or external bodyparts

            topic = f'{actions_standalone} {bpchoose} {animals} {characters} {family_members} {insects} {materials} {names} {quotes} {objects} {additions}'
            
            with open(topicgen_output, 'a') as out:
                out.write(f'\n {front}  {topic}')

            if logs and discord == True:
                send = requests.post(f'https://discord.com/api/v9/channels/{channel}/messages', data={'content': f'{send_front} {topic}'}, headers=global_headers)
                match send.status_code:
                    case 200:
                        print(f'{front} {send_front} {topic}')
                    
                    case 429:
                        match rate_limiting:
                            case True:
                                print(f'[X] {front} Ratelimited, retrying in {rate_limit}s')
                                time.sleep(rate_limit)

                            case False:
                                print(f'[X] {front} Ratelimited, retrying')
                    
                    case 401:
                        print(f'{front} Invalid token')
            if logs == True and discord == False:
                print(f'{front} {send_front} {topic}')



    except KeyboardInterrupt:
        clear_screen()
        nano()

class packgenui(customtkinter.CTk):
    def exit_button(self):
        clear_screen()
        nano()
    def gen(self):

        actions_by_a = random.choice(open('wordlists/actions/actions_by_a.txt', 'r').readlines()).strip()
        actions_by = random.choice(open('wordlists/actions/actions_by.txt', 'r').readlines()).strip()
        actions_standalone = random.choice(open('wordlists/actions/actions_standalone.txt', 'r').readlines()).strip()
        additions = random.choice(open('wordlists/additions/additions.txt', 'r').readlines()).strip()
        additions2 = random.choice(open('wordlists/additions/additions2.txt', 'r').readlines()).strip()
        animals = random.choice(open('wordlists/objects_misc/animals.txt', 'r').readlines()).strip()
        bodyparts_external = random.choice(open('wordlists/objects_misc/bodyparts_external.txt', 'r').readlines()).strip()
        bodyparts_internal = random.choice(open('wordlists/objects_misc/bodyparts_internal.txt', 'r').readlines()).strip()
        characters = random.choice(open('wordlists/lists/characters.txt', 'r').readlines()).strip()
        family_members = random.choice(open('wordlists/lists/family_members.txt', 'r').readlines()).strip()
        foods = random.choice(open('wordlists/objects_misc/foods.txt', 'r').readlines()).strip()
        insects = random.choice(open('wordlists/objects_misc/insects.txt', 'r').readlines()).strip()
        materials = random.choice(open('wordlists/objects_misc/materials.txt', 'r').readlines()).strip()
        names = random.choice(open('wordlists/lists/names.txt', 'r').readlines()).strip()
        numbers = random.choice(open('wordlists/person/numbers.txt', 'r').readlines()).strip()
        objects = random.choice(open('wordlists/objects_misc/objects.txt', 'r').readlines()).strip()
        races = random.choice(open('wordlists/person/races.txt', 'r').readlines()).strip()
        time_type = random.choice(open('wordlists/person/time_type.txt', 'r').readlines()).strip()
        quotes = random.choice(open('wordlists/lists/quotes.txt', 'r').readlines()).strip()

        self.bp = (bodyparts_external, bodyparts_internal)
        bpchoose = random.choice(self.bp) # chooses internal or external bodyparts

        self.combos = [
            f'tell me why your {family_members} got {actions_by_a} {additions} {objects}', 
            f'you got caught tryna {additions2} with your {additions} {family_members}s {objects}', 
            f'yo ass got {actions_by_a} {additions} version of {characters}',
            f'your {family_members} got {actions_by_a} {objects}',
            f'i walked in the room and saw you get {actions_by_a} {additions} {animals}',
            f'your {family_members} got caught tryna {additions2} your {additions} pet {animals}',
            f'your {family_members} beat you with a {additions} {objects}',
            f'this why your pet {animals} started {actions_standalone} your {additions} {family_members}',
            f'your {family_members} caught you eating leftover {foods} and started {actions_standalone} you',
            f'you tried riding a {objects} and fell over and got {actions_by_a} {animals} dressed up as a {foods}',
            f'yo ass got {actions_by_a} {races} {insects}',
            f'you got {actions_by_a} {additions} version of {names}',
            f'you tried {actions_standalone} your {numbers} {time_type} old {family_members}',
            f'you look like a {additions} version of your {numbers} {time_type} old {family_members}',
            f'you sound like a {races} {animals} when you sing yo ass said {quotes}',
            f'yo {races} {family_members} walked in the room and caught you {actions_standalone} your {additions} pet {animals} and started {actions_standalone} you',
            f'and then you got {actions_by_a} {races} {animals} with a {materials} {bpchoose}',
            f'yo {family_members} is in the hospital cuz you tried {actions_standalone} on them'
            ]
        
        
        self.choose_combo = random.choice(self.combos)
        self.content_button.configure(text=self.choose_combo)
    def __init__(self):
        super().__init__()

        self.geometry('780x780')
        self.title('packgen')

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.content_button = customtkinter.CTkLabel(master=self.frame, width=64, height=64, text='packgen :3')
        self.content_button.pack()

        self.generate_button = customtkinter.CTkButton(master=self.frame, text="press me for sex", width=32, height=32 ,command=self.gen)
        self.generate_button.pack()

        self.cancel_button = customtkinter.CTkButton(master=self.frame, text="exit", width=32, height=32 ,command=self.exit_button)
        self.cancel_button.place(x=111, y=15)

        self.cancel_button.pack()

def nano():
    try:

        clear_screen()
        if custom_ascii == True:
            print(custom_ascii_art)
        
        else:

            print(dashboard)
        print(options)
        choice = input('What script would you like to execute? 1/2/3/4: ')

        match choice:
            case '1':
                clear_screen()
                ap()
            case '2':
                clear_screen()
                aa()
            case '3':
                clear_screen()
                aac()
            case '4':
                clear_screen()
                packgen()
            case '4.1':
                clear_screen()
                topicgen()

            case '4.2':
                clear_screen()
                start = packgenui()
                start.mainloop()
            case _:
                clear_screen()
                nano()
    except KeyboardInterrupt:
        clear_screen()
        if custom_ascii == True:
            print(custom_ascii_art)

        else:

            print(dashboard)
        print(f'{front} Exiting Nano')
        sys.exit()

if __name__ == '__main__':
    firstLaunch()
    nano()