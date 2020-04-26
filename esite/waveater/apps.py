# -*- coding: utf-8 -*-
import os
import io
import logging

from django.conf import settings
from django.apps import AppConfig

from telethon import TelegramClient, events
from telethon.tl.custom import Button
from .file_handler import progress
import os
import time
import datetime
import asyncio
import threading

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
        return{
            'left': lambda: cls.left,
            'right': lambda: cls.right,
        }.get(cmd, lambda: cls.help)()

    @classmethod
    def left(cls, *args):
        if not args[0:]:
            args = ('noarg',)

        return ([
            [Button.inline('LLLeft'), Button.inline('RRRight')],
            [Button.url('Check this site!', 'https://lonamiwebs.github.io')]
        ], 1)

    @classmethod
    def right(cls, *args):
        return ('right', 1)

    @classmethod
    def help(cls, *args):
        return ('useable commands and arguments are:\n\thelp\t--help -h\n\tadd\t--add -a\n\texit\t--exit -e', 1)


class WaveaterConfig(AppConfig):
    name = 'esite.waveater'

    def ready(self):
        """Start the client."""
        print("waveaterbot started...")
        threading.Thread(name="waveater-main-thread", target=Waveater.main).start()

class Waveater():
    def main():
        loop = asyncio.new_event_loop()
        client = TelegramClient('anon', settings.TELEGRAM_API_ID, settings.TELEGRAM_API_HASH, loop=loop).start(bot_token=settings.TELEGRAM_BOT_TOKEN)

        @client.on(events.CallbackQuery)
        async def callback(event):
            print(event.query.msg_id)
            print(event.query.__dict__.keys())
            print(event.query.data.decode("utf-8"))
            print(BOX.commands('help')()[0])
            test = BOX.commands('right')()[0]
            print(test)
            print(BOX.commands('right')(event)[0])
            await client.edit_message(event.chat_id, event.query.msg_id, 'Welcome', buttons=[
                [Button.inline('Left'), Button.inline('Right')],
                [Button.url('Check this site!', 'https://lonamiwebs.github.io')]
            ])

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
            await event.respond('Pick one from this grid', buttons=[
                [Button.inline('Left'), Button.inline('Right')],
                [Button.url('Check this site!', 'https://lonamiwebs.github.io')]
            ])

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
