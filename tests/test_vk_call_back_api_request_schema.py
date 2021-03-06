from service.api.serializers.vk_call_back_event import VKChatSchema


call_back_api_event_data = {
    'type': 'message_new',
    'object': {
        'message': {
            'date': 1,
            'from_id': 1,
            'id': 10,
            'out': 0,
            'peer_id': 1,
            'text': 'hey',
            'conversation_message_id': 9,
            'fwd_messages': [],
            'important': False,
            'random_id': 0,
            'attachments': [],
            'is_hidden': False
        },
        'client_info': {
            'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
            'keyboard': True,
            'inline_keyboard': True, 'lang_id': 0
        }
    },
    'group_id': 1,
    'event_id': 'ei',
    'secret': 'secret'
}

call_back_api_event_data_with_payload = {
    'type': 'message_new',
    'object': {
        'message': {
            'date': 1,
            'from_id': 1,
            'id': 10,
            'out': 0,
            'peer_id': 1,
            'text': 'hey',
            'conversation_message_id': 9,
            'fwd_messages': [],
            'important': False,
            'random_id': 0,
            'attachments': [],
            'payload': '{"button":"1"}',
            'is_hidden': False
        },
        'client_info': {
            'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
            'keyboard': True,
            'inline_keyboard': True, 'lang_id': 0
        }
    },
    'group_id': 1,
    'event_id': 'ei',
    'secret': 'secret'
}


def test_vk_api_call_back_request():
    data = VKChatSchema().load(call_back_api_event_data)

    assert data == call_back_api_event_data


def test_vk_api_call_back_request_with_payload():
    data = VKChatSchema().load(call_back_api_event_data_with_payload)

    assert data == call_back_api_event_data_with_payload
    # assert isinstance(data['object']['message']['payload'], dict)
    # assert data['object']['message']['payload']['button'] == '1'
