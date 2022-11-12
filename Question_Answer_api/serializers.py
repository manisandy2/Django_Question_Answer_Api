from rest_framework import serializers

from .models import Question_1


class QuestionSerializers(serializers.ModelSerializer):
   class Meta:
       model = Question_1
       fields = ('ans_1','ans_2','ans_3','ans_4','text_ans')

       def __str__(self):
           return self.name


