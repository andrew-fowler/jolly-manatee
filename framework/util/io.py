from framework.util.time import current_time


def output(mesg):
    print("{0}: {1}".format(current_time(), mesg))

#
# def slack_message(message, channel="bas-chat"):
#     from slacker import Slacker
#     slack = Slacker(os.environ['SLACK_TOKEN'])
#     slack.chat.post_message(channel, message)
