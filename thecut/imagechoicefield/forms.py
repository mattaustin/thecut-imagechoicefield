# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import widgets
from django.forms import ChoiceField


class ImageChoiceField(ChoiceField):

    widget = widgets.ImageRadioSelect
