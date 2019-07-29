from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(wikiname,topic,rating):
	knowledge_object = Knowledge(
		wikiName = wikiname,
		topic = topic,
		rating = rating)
	session.add(knowledge_object)
	session.commit()

add_article("name","topic",1)	

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(topic = topic).first()
	return article

def query_article_by_rating(threshold):
	articles = []
	for i in range(threshold):
		articles.append(session.query(Knowledge).filter_by(rating = i).all())
	return articles

def query_article_by_primary_key(key):
	article = session.query(Knowledge).filter_by(knowledge_id = key).first()
		
def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic = topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()

def edit_article_rating():
	pass


delete_all_articles()
print(query_all_articles())
