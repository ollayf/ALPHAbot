# /CHNAGEE
@send_typing_action
def CHNAGEE(update, context):
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
        TO_CHNAGEE = context.bot_data['TO_CHNAGEE']
        update.message.reply_text(text= str(TO_CHNAGEE))

dispatcher.add_handler(CommandHandler('CHNAGEE', CHNAGEE), group=1)


# /CHNAGEE
@send_typing_action
def CHNAGEE(update, context):
    # makes sure user has started the conversation
    if not context.user_data['status']['started']:
        update.message.reply_text(text=not_started_error)
    # dont run command if the user is currently doing an action
    elif context.user_data['status']['action']:
        update.effective_message.reply_text(text=middle_of_action_msg)

    # if no other issue
    else:
        

dispatcher.add_handler(CommandHandler('CHNAGEE', CHNAGEE), group=1)