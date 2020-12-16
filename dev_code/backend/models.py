import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from config import database_setup, SQLALCHEMY_TRACK_MODIFICATIONS
from flask_migrate import Migrate



database_path = "postgres://{}:{}@{}/{}".format(
    database_setup['user_name'], database_setup['password'], database_setup['port'], database_setup['database_name'])

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.app = app
    db.init_app(app)
    # Creating an instance of the Migrate class
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    db.create_all()


'''
Define session Commit, in case create_question fail
'''
def session_commit():
    db.session.commit()
    
    
'''
Define session Rollback, in case create_question fail
'''
def session_rollback():
    db.session.rollback()


'''
Define session Close, in case create_question fail
'''
def session_close():
    db.session.close()
    


'''
Question

'''
class Question(db.Model):  
  __tablename__ = 'questions'

  id = Column(Integer, primary_key=True)
  question = Column(String)
  answer = Column(String)
  category = Column(String)
  difficulty = Column(Integer)

  def __init__(self, question, answer, category, difficulty):
    self.question = question
    self.answer = answer
    self.category = category
    self.difficulty = difficulty

  def insert(self):
    db.session.add(self)
    # db.session.commit()

  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
 
  def format(self):
    return {
      'id': self.id,
      'question': self.question,
      'answer': self.answer,
      'category': self.category,
      'difficulty': self.difficulty
    }

'''
Category

'''
class Category(db.Model):  
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True)
  type = Column(String)

  def __init__(self, type):
    self.type = type

  def format(self):
    return {
      'id': self.id,
      'type': self.type
    }
