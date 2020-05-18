# /CHANGE
@send_typing_action
def CHANGE(update, context):
    # for easier access to user data
    user_data = context.user_data
    # user must access backend first
    if not user_data['status']['backend']:
        update.effective_message.reply_text(text=backend_init_fail)
        return
    # dont run command if the user is currently doing an action
    elif user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)
        return
    # if theres no other issue
    else:
        TO_CHANGE = context.bot_data['TO_CHANGE']
        update.message.reply_text(text= str(TO_CHANGE))

dispatcher.add_handler(CommandHandler('CHANGE', CHANGE), group=1)


# /CHANGE
@send_typing_action
def CHANGE(update, context):
    # makes sure user has started the conversation
    if not context.user_data['status']['started']:
        update.message.reply_text(text=not_started_error)
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)

    # if no other issue
    else:
        

dispatcher.add_handler(CommandHandler('CHANGE', CHANGE), group=1)