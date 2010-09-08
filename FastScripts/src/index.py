#!/usr/bin/env python
#
# ForumFree Magazine Fast Scripts Generator
#
# Copyright (C) 2010 
# Niccolo` "Kurono" Campolungo <damnednickix@hotmail.it>
# Antonio Micari <darkstyle96@gmail.com>
# Damiano "Bowser" Faraone <bowser@ffmagazine.net>
#
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
#

from flask import *

app = Flask(__name__)

@app.route("/")
def index():
	script = ""
	style = ""
	return render_template('index.html', **locals())
	
@app.route("/admin/", methods=['POST','GET'])
def admin():
	script = ""
	style = ""
	return render_template('admin.html', **locals())

if __name__ == "__main__":
	app.debug = True
	app.run()
