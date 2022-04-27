# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from userge import Message, userge


@userge.on_cmd("del", about={"header": "delete replied message"})
async def del_msg(message: Message):
    msg_ids = [message.id]
    if message.reply_to_message:
        msg_ids.append(message.reply_to_message.id)
    await message.client.delete_messages(message.chat.id, msg_ids)
