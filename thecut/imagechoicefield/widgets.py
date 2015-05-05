# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from floppyforms.widgets import RadioSelect


class ImageRadioSelect(RadioSelect):

    template_name = 'imagechoicefield/_radio.html'

    class Media(object):
        css = {'all': ['imagechoicefield/imagechoicefield.css']}


class AdminImageRadioSelect(ImageRadioSelect):

    class Media(ImageRadioSelect.Media):
        js = ['imagechoicefield/admin.js']
