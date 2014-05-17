#
# Copyright 2011 Snitch Incorporated
#
# This file is part of AAWS.
#
# AAWS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AAWS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AAWS.  If not, see <http://www.gnu.org/licenses/>.
#


import request
from xml.etree import ElementTree as ET
import os.path


def getCredentials():
	import ConfigParser
	configParser = ConfigParser.ConfigParser()
	pth = 'aws.cfg'
	if not os.path.exists(pth):
		return None, None
	configParser.read(pth)
	key = configParser.get('Credentials', 'aws_access_key_id', False, None)
	secret = configParser.get('Credentials', 'aws_secret_access_key', False, None)
	return key, secret

#getBotoCredentials = getCredentials

class AWSError(Exception):

	def __init__(self, status, reason, data):
		self.status, self.reason, self.data = status, reason, data

	def __str__(self):
		return '(%s %s)\n%s' % (self.status, self.reason, self.data)


class AWSCompoundError(Exception):

	def __init__(self, errors):
		self.errors = errors

	def __str__(self):
		return '\n'.join([str(error) for error in self.errors])


class AWSService(object):
	pass

