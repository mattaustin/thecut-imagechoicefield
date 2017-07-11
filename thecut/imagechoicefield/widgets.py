# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms import RadioSelect


class ImageRadioSelect(RadioSelect):

    _css_class = 'imagechoicefield'

    option_template_name = 'imagechoicefield/_radio_option.html'

    def __init__(self, *args, **kwargs):
        attrs = kwargs.pop('attrs', {})
        classes = attrs.get('class', '').split()
        if self._css_class not in classes:
            classes += [self._css_class]
        attrs.update({'class': ' '.join(classes)})
        kwargs.update({'attrs': attrs})
        super(ImageRadioSelect, self).__init__(*args, **kwargs)

    class Media(object):
        css = {'all': ['imagechoicefield/imagechoicefield.css']}


class AdminImageRadioSelect(ImageRadioSelect):

    class Media(ImageRadioSelect.Media):
        js = ['imagechoicefield/admin.js']
