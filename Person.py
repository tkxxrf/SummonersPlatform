#basic Person object keeping track of name, summoner name, and email
class Person(object):
    #initialize function
    def __init__(self, default_name, default_summoner, default_email):
        self.name = default_name
        self.summoner_name = default_summoner
        self.email = default_email
    
    #string function that prints out the object
    def __str__(self):
        string = 'Name: %s Summoner Name: %s Email: %s' (self.name, self.summoner_name, self.email)
        return string
    
    #allows a user to change their name
    #does not allow changing to the same name or nothing
    def Change_Name(self, new_name):
        if self.name == new_name or new_name == '':
            print "Name Unsuccessfully Changed"
            return False
        self.name = new_name
        print "Name Successfully Changed"
        return True
    
    #allows a user to change their summoner name
    #does not allow summoner name to be the same or nothing
    def Change_summoner_name(self, new_summoner_name):
        if self.summoner_name == new_summoner_name or self.summoner_name == "":
            return False
        self.summoner_name = new_summoner_name
        return True
    
    #did not include a way to change their email as we are using CAS to allow login
    #though it might be needed in case someone gets a new email...
    
    