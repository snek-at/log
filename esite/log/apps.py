# -*- coding: utf-8 -*-
import os
import io
import logging

from django.conf import settings
from django.apps import AppConfig

from telethon import TelegramClient, events
from telethon.tl.custom import Button
#from .file_handler import progress
#import os
import time
import datetime
import asyncio
import threading
import json
import re

#from esite.waveater.models import Log

#log = Log.objects.create(uid=45350407,workpaket=[workpackage,])
# BOX object
class BOX:
    # meths
    @classmethod
    def os(cls, os):
        return{
            'posix': lambda: '/opt/ts3soundboard/',
            'nt': lambda: 'C:\\SinusBot\\',
            'mac': lambda: os.sys.exit()
        }.get(os, lambda: cls.help)()

    @classmethod
    def commands(cls, cmd):
        # input: lowercase string splitted by ":"
        # output: [0] - the text message,[1] - buttons
        cmd = cmd.split(": ")[0]
        return {
            'start': lambda: cls.start,
            'back': lambda: cls.start,
            'workpackages': lambda: cls.workpackages,
            'wp': lambda: cls.workpackage,
        }.get(cmd, lambda: cls.help)()

    @classmethod
    def start(cls, **kwargs):
        return ("Back",[
            [Button.inline('Workpackages'), Button.inline('Start')],
        ])

    @classmethod
    def workpackages(cls, **kwargs):
        from .models import Workpackage

        user_id = kwargs["event"].query.user_id
        workpackages = Workpackage.objects.all()
        # user_id = kwargs["event"].query.user_id
        # print('Hello')
        # log = Log.objects.get(uid=user_id)
        # print("USERIDDD", log.workpackages)
        # workpackages_object = json.loads(log.workpackages)
        # print(workpackages_object[0]['name'])
        # print([[Button.inline(workpackage['name'])] for workpackage in workpackages_object])
        button_list = [[Button.inline(f"wp: {workpackage.pid} {workpackage.name}")] for workpackage in workpackages]
        print(button_list)
        button_list.append([Button.inline('Back')])
        return (f'Afoch irgendwos',
            button_list
        )
    
    @classmethod
    def workpackage(cls, **kwargs):
        from .models import Workpackage
        print(kwargs['event'])
        user_id = kwargs['event'].query.user_id

        # workpackage = Workpackage.objects.get(uid=user_id)
        data = kwargs['event'].query.data.decode("utf-8").lower()
        print(data)
        pid = re.search('\d{3}\-\d{3}-\d{3}', data).group(0)
        workpackage = Workpackage.objects.get(pid=pid)
        print("WP", workpackage)

        wp_out = f"`{workpackage.name}\nstatus: {workpackage.status}\ndurration: {workpackage.durration}\nrealtime: {workpackage.realtime}\nsid: {workpackage.sid}\ndid: {workpackage.did}\npid: {workpackage.pid}`"
        return (wp_out, [[Button.inline('Back')]])

    @classmethod
    def help(cls, **kwargs):
        return ("useable commands and arguments are",[
            [Button.inline('Workpackages'), Button.inline('Start')],
        ])
        #return ('useable commands and arguments are:\n\thelp\t--help -h\n\tadd\t--add -a\n\texit\t--exit -e', [])


class LogConfig(AppConfig):
    name = 'esite.log'

    def ready(self):
        #from esite.waveater.models import Log
        """Start the client."""
        workpackage = {
            "name": "init",
            "status": "fertig",
            "durration": "9h",
            "realtime": "10h35m3s",
            "sid": "1",
            "did": "1.1",
            "pid": "1.1.1",
        }
        workpackage2 = {
            "name": "init2",
            "status": "fertig",
            "durration": "9h",
            "realtime": "10h35m3s",
            "sid": "1",
            "did": "1.1",
            "pid": "1.1.1",
        }

        # log = Log(uid=45350407, workpackages=json.dumps([workpackage,workpackage2 ]))
        # log.save()
        # log = Log(uid=903222659, workpackages=json.dumps([workpackage,workpackage2 ]))
        # log.save()
        threading.Thread(name="log-main-thread", target=Log.main).start()

class Log():
    def main():
        loop = asyncio.new_event_loop()
        client = TelegramClient('anon', settings.TELEGRAM_API_ID, settings.TELEGRAM_API_HASH, loop=loop).start(bot_token=settings.TELEGRAM_BOT_TOKEN)

        @client.on(events.CallbackQuery)
        async def callback(event):
            data = event.query.data.decode("utf-8").lower()
            cmd_out= BOX.commands(data)(event=event)
            # print(workpackages)
            # if(workpackages):
            #     print("true1")
            #     cmd_out= BOX.commands(data)(event,workpackages)
            #     print("true")
            # else:
            #     print("false")
            #     cmd_out= BOX.commands(data)(event)
            #     print("false")

            #workpackages = cmd_out[3]           
            #print(event.query.user_id)
            #print(event.query.__dict__.keys())
            #print(event.query.data.decode("utf-8"))
            #print(BOX.commands(event.query.data.decode("utf-8").lower())()[0])
            #print(cmd_out)
            await client.edit_message(event.chat_id, event.query.msg_id, cmd_out[0], buttons=cmd_out[1])

        def funcname(parameter_list):
            pass

        @client.on(events.NewMessage(pattern='/start'))
        @client.on(events.NewMessage(pattern='/help'))
        async def start(event):
            """Send a message when the command /start is issued."""
            await event.respond("Hi, I'm an audio slave! :3\nI would love to convert every wav you got into a telegram voice message. (>.<)")
            raise events.StopPropagation

        @client.on(events.NewMessage(pattern='/main'))
        async def start(event):
            """Send a message when the command /start is issued."""
            cmd_out= BOX.commands('start')()
            await event.respond('Pick one from this grid', buttons= cmd_out[1])

            raise events.StopPropagation

        @client.on(events.NewMessage)
        async def echo(event):
            """Echo the user message."""
            # if telegram message has attached a wav file, download and convert it
            if event.message.file and event.message.file.mime_type == 'audio/x-wav':
                msg = await event.respond("Processing...")

                try:
                    #start = time.time()

                    await msg.edit("**Downloading start...**")

                    # audio_in = io.BytesIO()
                    #audio_in.name = f"{event.message.file.name.split('.')[0]}_snek_{event.message.date.strftime('%m-%d_%H-%M')}.wav"
                    # audio_in = await client.download_media(event.message, audio_in, progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    #     progress(d, t, msg, start)))

                    # audio_seg = AudioSegment.from_wav(audio_in)

                    # audio_out = io.BytesIO()
                    # audio_out = audio_seg.export(audio_out, bitrate="128k", format='ogg', codec="opus", parameters=["-strict", "-2", "-ac", "2", "-vol", "150"], tags={"ARTIST": "waveater", "GENRE": "Meeting/Trashtalk", "ALBUM": "waveater", "TITLE": f"{event.message.file.name.split('.')[0]}_{event.message.media.document.date.strftime('%m-%d_%H-%M')}", "DATE": f"{event.message.media.document.date.strftime('%Y/%m/%d_%H:%M:%S')}", "COMMENT": f"A wav file converted to telegram voice message.", "CONTACT":"@waveater"})
                    # audio_out.name = f"{event.message.file.name.split('.')[0]}_{event.message.media.document.date.strftime('%m-%d_%H-%M')}.ogg"
                    #print(len(audio_seg)//1000)
                    #print(event.message.file.id)
                    #print(event.message.file.title)
                    #print(event.message.file.performer)
                    #print(event.message.file.name)
                    #print(event.message.file.duration)
                    result = await client.send_file(event.chat_id, audio_out, voice_note=True, caption=f"{event.message.message}\n\n`track: '{event.message.file.name.split('.')[0]}_{event.message.media.document.date.strftime('%m-%d_%H-%M')}',\nchannel: '{audio_seg.channels}'',\nformat: 'ogg',\ncodec: 'opus',\nbitrate: '128k'`", reply_to=event.message)
                    #print(result.file.duration)
                    #print(result.file.performer)

                    await msg.delete()

                except Exception as e:
                    print(e)
                    await msg.edit(f"OwO Shit happens! Something has gone wrong.\n\n**Error:** {e}")

        #print(f"{threading.enumerate()}")
        client.run_until_disconnected()

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2020 miraculix-org Florian Kleber
