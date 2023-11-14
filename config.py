import os
# import yaml

# with open('application.yaml', 'r') as config:
#     conf = yaml.safe_load(config)

# port = conf['server']['port']
# session_id = conf['config']['session-uuid']
# bot_url = conf['config']['bot-url']
# bot_id = conf['config']['bot-id']
# mediator_address = conf['config']['mediator-address']
# bot_password = conf['config']['bot-password']

session_id = os.environ['SESSION_ID']
bot_url = os.environ['BOT_URL']
mediator_address = os.environ['MEDIATOR_URL']
bot_id = os.environ['BOT_ID']
port = os.environ['SERVER_PORT']
bot_password = os.environ['BOT_PASSWORD']
