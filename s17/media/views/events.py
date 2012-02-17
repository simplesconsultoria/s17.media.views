# -*- coding: utf-8 -*-
from five import grok
from Products.ATContentTypes.interfaces import IATFile
from Products.Archetypes.interfaces import IObjectInitializedEvent
from Products.Archetypes.interfaces.event import IObjectEditedEvent

from zope.interface import alsoProvides, noLongerProvides

from s17.media.views.browser import IVideo, IAudio

@grok.subscribe(IATFile, IObjectInitializedEvent)
def set_media_layout(obj, event):
    ct = obj.getContentType()
    if ct:
        if 'video' in ct:
            obj.setLayout('video_file')
            alsoProvides(obj, IVideo)
        elif 'audio' in ct and obj.getFilename().split('.')[-1].lower() == 'mp3':
            obj.setLayout('audio_file')
            alsoProvides(obj, IAudio)


@grok.subscribe(IATFile, IObjectEditedEvent)
def set_media_modification_layout(obj, event):
    ct = obj.getContentType()
    layout = obj.getLayout()
    ext = obj.getFilename().split('.')[-1].lower()
    if ct:
        if 'video' in ct and layout != 'video_file':
            obj.setLayout('video_file')
            if IAudio.providedBy(obj):
                noLongerProvides(obj, IAudio)

            if not IVideo.providedBy(obj):
                alsoProvides(obj, IVideo)

        elif 'audio' in ct and ext == 'mp3' and layout != 'audio_file':
            obj.setLayout('audio_file')
            if IVideo.providedBy(obj):
                noLongerProvides(obj, IVideo)

            if not IAudio.providedBy(obj):
                alsoProvides(obj, IAudio)

        elif layout != 'file_view':
            obj.setLayout('file_view')
            if IVideo.providedBy(obj):
                noLongerProvides(obj, IVideo)
            if IAudio.providedBy(obj):
                noLongerProvides(obj, IAudio)
