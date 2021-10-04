#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Jackbro007

from pyrogram import filters, Client
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    if not await db.is_user_exist(update.from_user.id):
        await db.add_user(update.from_user.id)   
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    try:
        member = await bot.get_chat_member(chat_id=Translation.FORCE_SUB_CHANNEL, user_id=update.from_user.id)
    except UserNotParticipant:
        buttons = [[
        InlineKeyboardButton('OTT', url='https://t.me/M76Links')
    ],[
        InlineKeyboardButton('CHANNEL', url=f'https://t.me/onlyseries76?start={file_uid}')
    ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        await bot.send_message(
            text="<b>Uh oh It looks like you Aren't Subscribed To My <code><a href='https://telegram.dog/M76Links'>Channel</a></code>\n Please Join My Channel And come back and click on the Ok I've Joined Button</b>",
            chat_id=update.from_user.id,
            parse_mode="html",
            reply_markup=reply_markup
        )
        return
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
       
        if (file_id or file_type) == None:
            return
        caption_maker = file_caption.split()
        if "@M76Links" not in file_caption.split() :
            for i in file_caption.split():
                if i.startswith(r"@|https"):
                    file_caption=file_caption.replace(i,"@M76Links")
        
        file_caption = "<b>" + file_caption + "</b>"
        caption = file_caption if file_caption != ("" or None) else ("<b>" + file_name + "</b>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Join', url="https://t.me/M76Links"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('Group', url='https://t.me/onlymovie76')
    ],[
        InlineKeyboardButton('Channel', url='https://t.me/onlyseries76')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

