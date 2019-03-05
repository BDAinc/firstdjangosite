from django.db import models as m

# Create your models here.
class Question(m.Model): # ВОПРОСЫ
	question_text = m.CharField(max_length=200)
	pub_date = m.DateTimeField('date published')

	def __str__(self):
		return self.question_text

class Choice(m.Model): # ОТВЕТЫ НА ВОПРОС
	question = m.ForeignKey(Question, on_delete=m.CASCADE)
	choice_text = m.CharField(max_length=200)
	votes = m.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

# Django
# Flask + Djinja + SQLAlchemy


class News(m.Model):
	text = m.CharField(max_length=300)
	pub_date = m.DateTimeField('date published')