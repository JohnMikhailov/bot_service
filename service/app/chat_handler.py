import json

from service.app.commands import execute_command
from service.app.exceptions import CommandError, ExternalServiceCallError, BaseError
from service.app.vk.users import get_user_by_id
from service.app.vk.utils import get_random_id


def create_button(**kwargs):
    color = {'color': kwargs.pop('color')} if 'color' in kwargs else {}

    action = {
        attr: value
        for attr, value in kwargs.items()
    }

    return {
        'action': action,
        **color
    }


def keyboard():
    return {
        "one_time": False,
        'inline': False,
        "buttons": [
            [
                create_button(
                    type='text',
                    payload="{\"command\": \"!commands\"}",
                    label='Commands list',
                    color='positive'
                )
            ]
        ]
    }


def get_answer(request_data: dict):
    peer_id = request_data['object']['message']['from_id']
    response_data = {
        'message': 'mocked message',
        'keyboard': json.dumps(keyboard()),
        'peer_id': peer_id,
        'random_id': get_random_id()
    }

    message_text = request_data['object']['message']['text']

    if 'payload' in request_data['object']['message']:
        payload = request_data['object']['message']['payload']

        if payload['command'].lower() == 'start':
            user = get_user_by_id(peer_id)

            user_name = user.get('first_name')
            message_text = f'Hey, {user_name}, stay cool, thanks for joining (>_<)'

            response_data.update({
                'message': message_text,
                'keyboard': json.dumps(keyboard())
            })

            return response_data

        message_text = payload['command']

    try:
        message = execute_command(message_text)
    except CommandError as ce:
        message = f'Error during command execution - {ce.context}'
    except ExternalServiceCallError as esce:
        message = f'Service {esce.context} not available'
    except BaseError as be:
        print(be)
        message = f'Something strange happen'
    except Exception as e:
        print(e)
        message = f'WOW, something really goes bad'

    response_data.update({'message': message})

    return response_data
