#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2018
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
import pytest

from telegram import TelegramError
from telegram.error import Unauthorized, InvalidToken, NetworkError, BadRequest, TimedOut, \
    ChatMigrated, RetryAfter


class TestErrors(object):

    @staticmethod
    def test_telegram_error():
        with pytest.raises(TelegramError, match="^test message$"):
            raise TelegramError("test message")
        with pytest.raises(TelegramError, match="^Test message$"):
            raise TelegramError("Error: test message")
        with pytest.raises(TelegramError, match="^Test message$"):
            raise TelegramError("[Error]: test message")
        with pytest.raises(TelegramError, match="^Test message$"):
            raise TelegramError("Bad Request: test message")

    @staticmethod
    def test_unauthorized():
        with pytest.raises(Unauthorized, match="test message"):
            raise Unauthorized("test message")
        with pytest.raises(Unauthorized, match="^Test message$"):
            raise Unauthorized("Error: test message")
        with pytest.raises(Unauthorized, match="^Test message$"):
            raise Unauthorized("[Error]: test message")
        with pytest.raises(Unauthorized, match="^Test message$"):
            raise Unauthorized("Bad Request: test message")

    @staticmethod
    def test_invalid_token():
        with pytest.raises(InvalidToken, match="Invalid token"):
            raise InvalidToken

    @staticmethod
    def test_network_error():
        with pytest.raises(NetworkError, match="test message"):
            raise NetworkError("test message")
        with pytest.raises(NetworkError, match="^Test message$"):
            raise NetworkError("Error: test message")
        with pytest.raises(NetworkError, match="^Test message$"):
            raise NetworkError("[Error]: test message")
        with pytest.raises(NetworkError, match="^Test message$"):
            raise NetworkError("Bad Request: test message")

    @staticmethod
    def test_bad_request():
        with pytest.raises(BadRequest, match="test message"):
            raise BadRequest("test message")
        with pytest.raises(BadRequest, match="^Test message$"):
            raise BadRequest("Error: test message")
        with pytest.raises(BadRequest, match="^Test message$"):
            raise BadRequest("[Error]: test message")
        with pytest.raises(BadRequest, match="^Test message$"):
            raise BadRequest("Bad Request: test message")

    @staticmethod
    def test_timed_out():
        with pytest.raises(TimedOut, match="^Timed out$"):
            raise TimedOut

    @staticmethod
    def test_chat_migrated():
        with pytest.raises(ChatMigrated, match="Group migrated to supergroup. New chat id: 1234"):
            raise ChatMigrated(1234)
        try:
            raise ChatMigrated(1234)
        except ChatMigrated as e:
            assert e.new_chat_id == 1234

    @staticmethod
    def test_retry_after():
        with pytest.raises(RetryAfter, match="Flood control exceeded. Retry in 12 seconds"):
            raise RetryAfter(12)
