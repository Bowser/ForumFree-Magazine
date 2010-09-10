#! -*- coding: utf-8 -*-

from flask import request
class generator:
	#variabili per il generatore
	__script = ''
	__check = ''

	#variabili per lo script
	__alert = ''
	__isText = 1
	__id = '0'
	__inputText = ''
	__inputImage = ''
	def __init__(self):
		try:
			self.__check = str(request.args['check'])
		except:
			pass
		try:
			self.__isText = int(request.args['support_isText'])
		except:
			pass
		try:
			self.__alert = str(request.args['support_text'])
		except:
			pass
		try:
			self.__id = str(request.args['support_id'])
		except:
			pass
		self.__inputText = self.__isText and '<input type="submit" value="%s" class="forminput">' % self.__alert or ''
		self.__inputImage = (not int(self.__isText)) and '<input type="image" src="%s" style="border: 0;">' % self.__alert or ''
		if len(self.__check) > 0:
			self.__script = self.__load()
		
	def __load(self):
		return '''<!-- Generato con il FFMagazine FastScripts - Script by Delta e Bowser -->
<form action="http://supporto.forumfree.it/" method="post" name="REPLIER">
<input type="hidden" name="st" value="0">
<input type="hidden" name="act" value="Post">
<input type="hidden" name="f" value="26622">
<input type="hidden" name="CODE" value="03">
<input type="hidden" name="t" value="%s">
%s
<input type="hidden" name="Post" value="Up!">
%s
</form><br>
<small>Ideato da Delta e Bowser (c) <a href="http://ffmagazine.forumfree.it/">ForumFree Magazine</a></small>''' % (self.__id, self.__inputImage, self.__inputText)

	def output(self):
		return self.__script
