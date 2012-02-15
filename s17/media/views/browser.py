from five import grok

from zope.interface import Interface
from Acquisition import aq_inner

grok.templatedir("templates")


class VideoView(grok.View):
    grok.context(Interface)
    grok.name("video_file")
    grok.template('video_file')
    grok.require("zope2.View")
    

class AudioView(grok.View):
    grok.context(Interface)
    grok.name("audio_file")
    grok.template('audio_file')
    grok.require("zope2.View")
