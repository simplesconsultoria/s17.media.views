# -*- coding: utf-8 -*-

import os
import unittest2 as unittest

from zope.event import notify

from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles

from Products.CMFPlone.tests import dummy

from s17.media.views.testing import INTEGRATION_TESTING
from s17.media.views.events import set_media_layout
from s17.media.views.events import set_media_modification_layout

import s17.media.views.tests

dir = s17.media.views.tests

AVI = open(os.path.join(os.path.dirname(dir.__file__),'test.avi')).read()
FLV = open(os.path.join(os.path.dirname(dir.__file__),'test.flv')).read()
MP3 = open(os.path.join(os.path.dirname(dir.__file__),'test.mp3')).read()
MP4 = open(os.path.join(os.path.dirname(dir.__file__),'test.mp4')).read()
OGM = open(os.path.join(os.path.dirname(dir.__file__),'test.ogm')).read()
SWF = open(os.path.join(os.path.dirname(dir.__file__),'test.swf')).read()


class TestEvents(unittest.TestCase):
    """Ensure product is properly installed
    """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', id='media',title='Media')
        self.folder = self.portal['media']
        self.folder.invokeFactory('File', id='file',title='File', file=dummy.File())
        self.file = self.folder['file']

    def test_avi_create(self):
        self.folder.invokeFactory('File', id='avi', title='AVI File', file=dummy.File(filename='test.avi', data=AVI))
        avi = self.folder['avi']
        self.assertEqual(str(avi), AVI)

        event = set_media_layout(avi, self.portal.REQUEST)
        notify(event)
        self.assertEqual(avi.getLayout(),'video_file')

    def test_avi_edit(self):
        self.file.file_edit(file=dummy.File(filename='test.avi', data=AVI))
        event = set_media_modification_layout(self.file, self.portal.REQUEST)
        notify(event)
        self.assertEqual(self.file.getLayout(),'video_file')

    def test_flv_create(self):
        self.folder.invokeFactory('File', id='flv', title='FLV File', file=dummy.File(filename='test.flv', data=FLV))
        flv = self.folder['flv']
        self.assertEqual(str(flv), FLV)

        event = set_media_layout(flv, self.portal.REQUEST)
        notify(event)
        self.assertEqual(flv.getLayout(),'video_file')

    def test_flv_edit(self):
        self.file.file_edit(file=dummy.File(filename='test.flv', data=FLV))
        event = set_media_modification_layout(self.file, self.portal.REQUEST)
        notify(event)
        self.assertEqual(self.file.getLayout(),'video_file')

    def test_mp3_create(self):
        self.folder.invokeFactory('File', id='mp3', title='MP3 File', file=dummy.File(filename='test.mp3', data=MP3))
        mp3= self.folder['mp3']
        self.assertEqual(str(mp3), MP3)

        event = set_media_layout(mp3, self.portal.REQUEST)
        notify(event)
        self.assertEqual(mp3.getLayout(),'audio_file')

    def test_mp3_edit(self):
        self.file.file_edit(file=dummy.File(filename='test.mp3', data=MP3))
        event = set_media_modification_layout(self.file, self.portal.REQUEST)
        notify(event)
        self.assertEqual(self.file.getLayout(),'audio_file')

    def test_mp4_create(self):
        self.folder.invokeFactory('File', id='mp4', title='MP4 File', file=dummy.File(filename='test.mp4', data=MP4))
        mp4= self.folder['mp4']
        self.assertEqual(str(mp4), MP4)

        event = set_media_layout(mp4, self.portal.REQUEST)
        notify(event)
        self.assertEqual(mp4.getLayout(),'video_file')

    def test_mp4_edit(self):
        self.file.file_edit(file=dummy.File(filename='test.mp4', data=MP4))
        event = set_media_modification_layout(self.file, self.portal.REQUEST)
        notify(event)
        self.assertEqual(self.file.getLayout(),'video_file')

    def test_ogm_create(self):
        self.folder.invokeFactory('File', id='ogm', title='OGM File', file=dummy.File(filename='test.ogm', data=OGM))
        ogm= self.folder['ogm']
        self.assertEqual(str(ogm), OGM)

        event = set_media_layout(ogm, self.portal.REQUEST)
        notify(event)
        self.assertEqual(ogm.getLayout(),'video_file')

    def test_ogm_edit(self):
        self.file.file_edit(file=dummy.File(filename='test.ogm', data=OGM))
        event = set_media_modification_layout(self.file, self.portal.REQUEST)
        notify(event)
        self.assertEqual(self.file.getLayout(),'video_file')

    def test_swf_create(self):
        self.folder.invokeFactory('File', id='swf', title='SWF File', file=dummy.File(filename='test.swf', data=SWF))
        swf= self.folder['swf']
        self.assertEqual(str(swf), SWF)

        event = set_media_layout(swf, self.portal.REQUEST)
        notify(event)
        self.assertEqual(swf.getLayout(),'flash_file')

    def test_swf_edit(self):
        self.file.file_edit(file=dummy.File(filename='test.swf', data=SWF))
        event = set_media_modification_layout(self.file, self.portal.REQUEST)
        notify(event)
        self.assertEqual(self.file.getLayout(),'flash_file')

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
