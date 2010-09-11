# -*- coding: utf-8 -*-
#!/usr/bin/python
# -------------------------------------------------------------------------
# Modulo: Scripts Anti Copiatura
# Guida associata: http://ffmagazine.forumfree.it/?t=36582013
# -------------------------------------------------------------------------
# ForumFree Magazine Fast Scripts Generator
# Ultimo aggiornamento: 10/09/2010 20:48 - v0.1alpha
# Copyright (C) 2010 ForumFree Magazine http://ffmagazine.forumfree.it
#
# Sviluppatori:
# Niccolo` "Kurono" Campolungo <damnednickix@hotmail.it>
# Antonio Micari <darkstyle96@gmail.com>
# Damiano Faraone (aka Bowser) <bowser@ffmagazine.net>
# -------------------------------------------------------------------------
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
# -------------------------------------------------------------------------
from flask import request
class generator:
	__script = ''
	__check = ''

	__alert = ''
	__select = ''
	
	def __init__(self):
		try:
			self.__select = int(request.args['nocopy_select'])
		except:
			pass
			
		try:
			self.__check = str(request.values['check'])
		except:
			pass
			
		try:
			self.__alert = str(request.values['nocopy_message'])
		except:
			pass

		if len(self.__check) > 0:
			self.__script = self.__load()
		elif self.__select != '':
			self.__script = self.__select
		
	def __load(self):
		if self.__select == 1:
			return '''<script type="text/javascript">
//Generato con il FFMag FastScripts - Script by Bowser
var tdmessaggio="%s";
// Autore dello script: Maximus (maximus@nsimail.com) w/ By DynamicDrive.com
// http://www.dynamicdrive.com/dynamicindex9/noright.htm
// Funzione che disabilita il tasto destro su Internet Explorer
function clickIE4(){ if(event.button==2){ if(tdmessaggio!= '') alert(tdmessaggio); return false; } }
// Funzione che disabilita il tasto destro su Netscape e FireFox
function clickNS4(e){
if (document.layers||document.getElementById&&!document.all){ if (e.which==2||e.which==3){ if(tdmessaggio!= '') alert(tdmessage); return false; } }
}
// Controlli per la selezione del browser
if (document.layers){ document.captureEvents(Event.MOUSEDOWN); document.onmousedown=clickNS4; }
else if (document.all&&!document.getElementById){ document.onmousedown=clickIE4; }
document.oncontextmenu=function(){ if(tdmessaggio!= '') alert(tdmessaggio); return false;};
</script>''' % self.__alert
		elif self.__select == 2:
			return '''<script type="text/javascript">
//Generato con il FFMag FastScripts - Script by Bowser
document.oncontextmenu=document.onselectstart=document.ondragstart=function() {return false;};
</script>'''
		elif self.__select == 3:
			return '''<script type="text/javascript">
//Generato con il FFMag FastScripts - Script by Bowser
var tdmessaggio = "%s";
document.oncontextmenu=function(){ alert(tdmessaggio + "\\nAdesso apparira il menu'"); return true; }
</script>''' % self.__alert
		else:
			return 'ERRORE'

	def output(self):
		return self.__script
