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
    ext = obj.getFilename().split('.')[-1].lower()
    if ct:
        if 'video' in ct and layout != 'video_file':
            obj.setLayout('video_file')
        elif 'audio' in ct and ext == 'mp3' and layout != 'audio_file':
            obj.setLayout('audio_file')
        elif layout != 'file_view':
            obj.setLayout('file_view')
        
    
