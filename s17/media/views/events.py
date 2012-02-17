# -*- coding: utf-8 -*-

from five import grok

from Products.ATContentTypes.interfaces import IATFile
from Products.Archetypes.interfaces import IObjectInitializedEvent
from Products.Archetypes.interfaces.event import IObjectEditedEvent


@grok.subscribe(IATFile, IObjectInitializedEvent)
def set_default_layout(obj, event):
    ct = obj.getContentType()
    if ct:
        if 'video' in ct:
            obj.setLayout('video_file')
        elif 'audio' in ct and obj.getFilename().split('.')[-1].lower() == 'mp3':
            obj.setLayout('audio_file')


@grok.subscribe(IATFile, IObjectEditedEvent)
def set_default_layout(obj, event):
    ct = obj.getContentType()
    layout = obj.getLayout()
    if ct:
        if 'video' in ct:
            obj.setLayout('video_file')
        elif 'audio' in ct:
            obj.setLayout('audio_file')
        elif layout != 'file_view':
            obj.setLayout('file_view')
