from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'knowledge' 
	knowledge_id = Column(Integer, primary_key=True, autoincrement = True)	
	wikiName = Column(String)
	topic = Column(String)
	rating = Column(Integer)

	def __repr__(self):
		if self.rating < 7:
			return ("if you want learn about {}"
              		", you should look at the Wikipedia article called {}"
               		".We gave this article a rating of {}"
               		"out of 10! {}"
               		" Unfortunately, this article does not have a better rating. Maybe, this is an article that should bereplaced soon!.").format(
                    self.topic, self.wikiName, self.rating, self.knowledge_id)
		return ("if you want learn about {}"
                ", you should look at the Wikipedia article called {}"
                ".We gave this article a rating of {}"
                " out of 10! {}").format(
                    self.topic, self.wikiName, self.rating, self.knowledge_id)
