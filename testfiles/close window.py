def example():
    example.has_been_called = True
example.has_been_called = False


example()

#Actual Code!:
if example.has_been_called:
   print("foo bar")
