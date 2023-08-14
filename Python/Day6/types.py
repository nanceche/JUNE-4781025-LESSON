from abc import ABC, abstractmethod

class dolls(ABC):

   
    @abstractmethod
    def add_ken(self):
        pass

class barbie(dolls):
    
    def add_ken(self):
        ken=0
        new_ken= ken+1
        return new_ken


Barbie=barbie()
additional_ken=Barbie.add_ken()

print(additional_ken)