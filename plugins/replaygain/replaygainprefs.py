# Copyright (C) 2009 Adam Olsen
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os
from xlgui.prefs import widgets
from xl import xdg

name = 'Replaygain'
basedir = os.path.dirname(os.path.realpath(__file__))
glade = os.path.join(basedir, "replaygainprefs_pane.glade")

class AlbumModePreference(widgets.CheckPrefsItem):
    default = True
    name = 'replaygain/album-mode'

class ClippingProtectionPreference(widgets.CheckPrefsItem):
    default = True
    name = 'replaygain/clipping-protection'

class PreAmpPreference(widgets.SpinPrefsItem):
    default = 0
    name = 'replaygain/pre-amp'

class FallbackGainPreference(widgets.SpinPrefsItem):
    default = 0
    name = 'replaygain/fallback-gain'


