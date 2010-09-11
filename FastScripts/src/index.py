# -*- coding: utf-8 -*-
#!/usr/bin/python
# -------------------------------------------------------------------------
# Index File
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

# Core Modules
from flask import Flask, render_template, Markup, request, jsonify, escape
import os

app = Flask(__name__)

# ----- Index ------
@app.route("/")
def index():
	try:
		script = Markup(request.args['script'])
	except:
		script = Markup("document.write('Test JavaScript<br />')")
	try:
		style = request.args['style']
	except:
		style = "body { background: #000; color: #fff; }"
	return render_template('index.html', **locals())

# ----- Generatori ------
@app.route("/generator/<gen_name>", methods=['GET', 'POST'])
def generatore(gen_name):
	gen_name = gen_name.lower()
	gen_list = os.listdir('modules')

	if (gen_name + '.py') in gen_list:
		gen_load = __import__('modules.'+gen_name, globals(), locals(), ['generator'], -1)
		gen = gen_load.generator()

		output = gen.output()

		html = render_template('modules/'+gen_name+'.html', output=output)
		return html

# -------------------------------------------------------------------------
if __name__ == "__main__":
	app.debug = True
	app.run()
	# app.run('0.0.0.0')
