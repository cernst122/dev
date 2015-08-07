#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext import ndb





class Team(ndb.Model):
  city = ndb.StringProperty()
  name = ndb.StringProperty()

class Player(ndb.Model):
  name = ndb.StringProperty()
  position=ndb.StringProperty()
  team = ndb.KeyProperty(Team)
  
team1= Team(city = "Chicago", name = "Christinas")
team1.put()
player1= Player(name = "Arely", position = "quarterback", team =team1.key)
player1.put()
player2= Player(name = "Christina", position = "quarterback", team =team1.key)
player2.put()
print team1
print player1
