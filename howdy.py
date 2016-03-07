class Howdy:
  word = 'hello'

  def sayit(self):
	  return self.word

def foo(): 
	return 11

def somewordplay():

   howdy = Howdy()
   print howdy.word
   print howdy.sayit()
   howdy.word = 'world'
   print howdy.sayit()
   print foo()
