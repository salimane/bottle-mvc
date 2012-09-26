# -*- coding: utf-8 -*-


class Printer(object):

    def show_string(self, text):
        if text == '':
            return "You didn't enter any text to flash"
        else:
            return text + "!!!"
