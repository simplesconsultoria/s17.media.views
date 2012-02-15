# -*- coding: utf-8 -*-
from five import grok
from Products.ATContentTypes.interfaces import IATFile
from Products.Archetypes.interfaces import IObjectInitializedEvent

@grok.subscribe(IATFile, IObjectInitializedEvent)
def set_default_layout(obj, event):
    ct = obj.getContentType()
    if ct:
        if 'video' in ct:
            obj.setLayout('video_file')
        elif 'audio' in ct:
            obj.setLayout('audio_file')
