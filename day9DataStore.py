# When you import ndb, you can use these specific database methods.
#
# Create . put
# Read . name
# Update .name="newName"
# Delete .delete
#
#
# in main.py:
import webapp2
from google.appengine.ext import ndb

class Answer(ndb.Model): #add the properties you want to store
  question = ndb.StringProperty(required = True)
  answer = ndb.StringProperty(required = True)


class AddHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write("hello world")
    #define what the properties of this object will be (normally they'll come from a form)
    user_question = "Will I be happy?"
    our_answer = "Maybe"
    #now build the actual object to store
    answer_to_store = Answer(question = user_question, answer = our_answer)
    #you created the object, now store it with put
    answer_to_store.put()
    #check that the object is stored in your developers console>datastore viewer on google app engine website

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Search them all! <br>")
        user_question = "Will I be happy tomorrow"
        #do a query on the object; want to access the APi that can be used for reading the data.
        #on this query i want to do a filter, and I specify what element I'm filtering for
        filtered_search = Answer.query().filter(
            Answer.question == user_question
        ).fetch()
        #i want objects of type answer. on those objects i'm making a query. that query will be filtered, and i want it filtered by user question.
        #now fetch the data. get will return one element; fetch returns a list of elements stored in that quesion.
        #returns a list of answer objects with the key, the question, and the answer.
        for answer in filtered_search:
            self.response.write(str(answer) + "<br>")
            #for every answer in my future search, I will bring that answer.

class DeleteHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write("Delete them all!")
    user_question = "Will I be happy tomorrow?"
    filtered_search = Answer.query().filter(
        Answer.question ==user_question).fetch()
    for answer in filtered_search:
        answer.key.delete #delete is a method of the key of your object, not of your object itself


class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write("hello world")

app = webapp2.WSGIApplication([
('/', MainHandler)
('/add', AddHandler)
('/search', SearchHandler)
('/delete', DeleteHandler)

]), debug = True
