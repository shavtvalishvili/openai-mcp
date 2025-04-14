CONVERSATION_HISTORY_PROMPT = """
    ### **Conversation History**:
    {message_list_json_string}
"""

CONVERSATION_HISTORY_0 = [
    {'role': 'user', 'channel': 'email',
     'content': 'Hi! I am looking forward to purchasing a vehicle at Waterloo Honda. Do you have any Honda Civics at least from year 2023 with relatively low milage, preferably with leather interior?'}
]

CONVERSATION_HISTORY_1 = [
    {'role': 'user', 'channel': 'email',
     'content': 'Do you have any Honda Civics at least from year 2023 with relatively low milage, preferably with leather interior?'},
    {'role': 'assistant', 'channel': 'email', 'content': """Hi,
It's Olivia Reed from Waterloo Honda.
Thank you for expressing your interest.
I do show that such vehicle is available, but I'll have my team check to make sure it's ready for you at the dealership. In the meantime, I can assist you with any other questions you might have.
If you'd like to schedule an appointment, simply choose a day and time, and I'll arrange it for you. Alternatively, would you like us to call your number, +1-315-352-8168, before you schedule an appointment?
2024 Honda Civic
$20 000
VIN: 5N1DR3DF1RC220469
Stock #: AW1154
"""},
    {'role': 'assistant', 'channel': 'sms',
     'content': """Hi, It's Olivia Reed from Waterloo Honda. Thank you for expressing your interest. I do show that such vehicle is available, but I'll have my team check to make sure it's ready for you at the dealership. In the meantime, I can assist you with any other questions you might have. If you'd like to schedule an appointment, simply choose a day and time, and I'll arrange it for you. Alternatively, would you like us to call your number, +1-315-352-8168, before you schedule an appointment? https://vi.carleadsup.com/cars?r=jgjell"""}
]

CONVERSATION_HISTORY_2 = [
    {'role': 'user', 'channel': 'email',
     'content': 'Do you have any Honda Civics at least from year 2023 with relatively low milage, preferably with leather interior?'},
    {'role': 'assistant', 'channel': 'email', 'content': """Hi,
It's Olivia Reed from Waterloo Honda.
Thank you for expressing your interest.
I do show that such vehicle is available, but I'll have my team check to make sure it's ready for you at the dealership. In the meantime, I can assist you with any other questions you might have.
If you'd like to schedule an appointment, simply choose a day and time, and I'll arrange it for you. Alternatively, would you like us to call your number, +1-315-352-8168, before you schedule an appointment?
2024 Honda Civic
$20 000
VIN: 5N1DR3DF1RC220469
Stock #: AW1154
"""},
    {'role': 'assistant', 'channel': 'sms',
     'content': """Hi, It's Olivia Reed from Waterloo Honda. Thank you for expressing your interest. I do show that such vehicle is available, but I'll have my team check to make sure it's ready for you at the dealership. In the meantime, I can assist you with any other questions you might have. If you'd like to schedule an appointment, simply choose a day and time, and I'll arrange it for you. Alternatively, would you like us to call your number, +1-315-352-8168, before you schedule an appointment? https://vi.carleadsup.com/cars?r=jgjell"""},
    {'role': 'user', 'channel': 'email', 'content': 'Yes, I would like to schedule an appointment.'},
    {'role': 'assistant', 'channel': 'email', 'content': 'When would you like me to schedule an appointment for you?'},
    {'role': 'user', 'channel': 'email', 'content': """I'd like to schedule an appointment on Wednesday at 3PM."""}
]
