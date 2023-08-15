from abc import ABC, abstractmethod

class dolls(ABC):
    ken=0
   
    @abstractmethod
    def add_ken(self):
        pass

class barbie(dolls):
    
    def add_ken(self):
      
        self.ken=self.ken+1
        return self.ken


Barbie=barbie()
additional_ken=Barbie.add_ken()
another_ken=Barbie.add_ken()

print(Barbie.ken)



