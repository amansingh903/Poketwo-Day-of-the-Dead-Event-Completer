import random, re, string
import requests as r

class Utils:
    @staticmethod
    def click_button(token, message_id, custom_id, channel_id, guild_id, application_id, session_id, type, values=None):
        url = 'https://discord.com/api/v9/interactions'
        headers = {'Authorization': token}
        payload = {
            "type": 3,
            "guild_id": guild_id,
            "channel_id": channel_id,
            "message_id": message_id,
            "application_id": application_id,
            "session_id": session_id,
            "data": {
                "component_type": type,
                "custom_id": custom_id,
                "type": 3
            }
        }
        if values is not None:
            payload['data']['values'] = [values]
        res = r.post(url, headers=headers, json=payload)
        return res.status_code

    @staticmethod
    def send(content, token, channel_id):
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        headers = {'Authorization': token}
        payload = {'content': content}
        r.post(url, headers=headers, json=payload)



    @staticmethod
    def generate_session_id():
        return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

