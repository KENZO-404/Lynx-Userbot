# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.tl.types import MessageEntityMentionName
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot import CMD_HELP, bot
from telethon import events

from . import *


@ultroid_cmd(
    pattern="ungban ?(.*)",
)
async def _(e):
    xx = await eor(e, "`UnGbanning...`")
    if e.is_private:
        userid = (await e.get_chat()).id
    elif e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        if (e.pattern_match.group(1)).isdigit():
            try:
                userid = (await e.client.get_entity(int(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
        else:
            try:
                userid = (await e.client.get_entity(str(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if not is_gbanned(userid):
        return await eod(xx, "`User is not gbanned.`", time=3)
    async for ggban in e.client.iter_dialogs():
        if ggban.is_group or ggban.is_channel:
            try:
                await e.client.edit_permissions(ggban.id, userid, view_messages=True)
                chats += 1
            except BaseException:
                pass
    ungban(userid)
    await xx.edit(
        f"`Ungbanned` [{name}](tg://user?id={userid}) `in {chats} chats.\nRemoved from gbanwatch.`",
    )


@ultroid_cmd(
    pattern="gban ?(.*)",
)
async def _(e):
    xx = await eor(e, "`Gbanning...`")
    if e.is_private:
        userid = (await e.get_chat()).id
    elif e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        if (e.pattern_match.group(1)).isdigit():
            try:
                userid = (await e.client.get_entity(int(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
        else:
            try:
                userid = (await e.client.get_entity(str(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", tome=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if userid == ultroid_bot.uid:
        return await eod(xx, "`I can't gban myself.`", time=3)
    if user.id == 1448477501:
        return await eod(xx, "`I can't gban my Developers.`", time=3)
    if is_gbanned(userid):
        return await eod(
            xx,
            "`User is already gbanned and added to gbanwatch.`",
            time=4,
        )
    async for ggban in e.client.iter_dialogs():
        if ggban.is_group or ggban.is_channel:
            try:
                await e.client.edit_permissions(ggban.id, userid, view_messages=False)
                chats += 1
            except BaseException:
                pass
    gban(userid)
    await xx.edit(
        f"`Gbanned` [{name}](tg://user?id={userid}) `in {chats} chats.\nAdded to gbanwatch.`",
    )


@ultroid_cmd(
    pattern="gocast ?(.*)",
)
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return eor(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[6:]
    kk = await eor(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in ultroid_bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await ultroid_bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")


@ultroid_cmd(
    pattern="gucast ?(.*)",
)
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return eor(event, "`Give some text to Globally Broadcast`")
    tt = event.text
    msg = tt[7:]
    kk = await eor(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in ultroid_bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await ultroid_bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")


@ultroid_cmd(
    pattern="gkick ?(.*)",
)
async def gokick(e):
    xx = await eor(e, "`Gkicking...`")
    if e.is_private:
        userid = (await e.get_chat()).id
    elif e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        if (e.pattern_match.group(1)).isdigit():
            try:
                userid = (await e.client.get_entity(int(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
        else:
            try:
                userid = (await e.client.get_entity(str(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if userid == ultroid_bot.uid:
        return await eod(xx, "`I can't gkick myself.`", time=3)
    if user.id == 1448477501:
        return await eod(xx, "`I can't gkick my Developers.`", time=3)
    async for gkick in e.client.iter_dialogs():
        if gkick.is_group or gkick.is_channel:
            try:
                await ultroid_bot.kick_participant(gkick.id, userid)
                chats += 1
            except BaseException:
                pass
    await xx.edit(f"`Gkicked` [{name}](tg://user?id={userid}) `in {chats} chats.`")


@ultroid_cmd(
    pattern="gomute ?(.*)",
)
async def _(e):
    xx = await eor(e, "`Gmuting...`")
    if e.is_private:
        userid = (await e.get_chat()).id
    elif e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        if (e.pattern_match.group(1)).isdigit():
            try:
                userid = (await e.client.get_entity(int(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
        else:
            try:
                userid = (await e.client.get_entity(str(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", tome=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if userid == ultroid_bot.uid:
        return await eod(xx, "`I can't gmute myself.`", time=3)
    if user.id == 1448477501:
        return await eod(xx, "`I can't gmute my Developers.`", time=3)
    if is_gmuted(userid):
        return await eod(xx, "`User is already gmuted.`", time=4)
    async for onmute in e.client.iter_dialogs():
        if onmute.is_group:
            try:
                await e.client.edit_permissions(onmute.id, userid, send_messages=False)
                chats += 1
            except BaseException:
                pass
    gmute(userid)
    await xx.edit(f"`Gmuted` [{name}](tg://user?id={userid}) `in {chats} chats.`")


@ultroid_cmd(
    pattern="ungomute ?(.*)",
)
async def _(e):
    xx = await eor(e, "`UnGmuting...`")
    if e.is_private:
        userid = (await e.get_chat()).id
    elif e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        if (e.pattern_match.group(1)).isdigit():
            try:
                userid = (await e.client.get_entity(int(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
        else:
            try:
                userid = (await e.client.get_entity(str(e.pattern_match.group(1)))).id
            except ValueError as err:
                return await eod(xx, f"{str(err)}", time=5)
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    if not is_gmuted(userid):
        return await eod(xx, "`User is not gmuted.`", time=3)
    async for hurr in e.client.iter_dialogs():
        if hurr.is_group:
            try:
                await e.client.edit_permissions(hurr.id, userid, send_messages=True)
                chats += 1
            except BaseException:
                pass
    ungmute(userid)
    await xx.edit(f"`Ungmuted` [{name}](tg://user?id={userid}) `in {chats} chats.`")


@ultroid_bot.on(events.ChatAction)
async def _(e):
    if e.user_joined or e.added_by:
        user = await e.get_user()
        chat = await e.get_chat()
        if is_gbanned(str(user.id)):
            if chat.admin_rights:
                try:
                    await e.client.edit_permissions(
                        chat.id,
                        user.id,
                        view_messages=False,
                    )
                    gban_watch = f"`Gbanned User` [{user.first_name}](tg://user?id={user.id}) `Spotted\n"
                    gban_watch += f"Banned Successfully`"
                    await e.reply(gban_watch)
                except BaseException:
                    pass


CMD_HELP.update({
    "globalban": "\
⚡𝘾𝙈𝘿⚡: `.gban`\
\n↳ : Melakukan Banned Secara Global Ke Semua Grup Dimana Anda Sebagai Admin.\
\n\n⚡𝘾𝙈𝘿⚡: `.ungban`\
\n↳ : Membatalkan Banned Secara Global."})
