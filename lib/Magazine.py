class Magazine:
    all_magazines = []    #for storing all the instances of the magazines
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        Magazine.all_magazines.append(self)
      
    def name(self):
        return self._name

    def category(self):
        return self._category

    def contributors(self):
        return self._contributors
    
    def add_contributor(self, author):
        self._contributors.append(author)


   

author1 = ("MELA CHU")
author2 = ("AVOGADROS")
author3 = ("JULIUS NYAMBUTI")

magazine = Magazine("The croods", "Animation, Adventure")

magazine.add_contributor(author1)
magazine.add_contributor(author2)
magazine.add_contributor(author3)

print(magazine.name())           
print(magazine.category())
print(magazine.contributors())


  
