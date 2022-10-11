# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import twint


# Configure
c = twint.Config()
c.Search = "民主共和国"
c.Min_likes = 5

twint.run.Search(c)

