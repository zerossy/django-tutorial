import datetime  # python 의 표준 모듈인 datetime 모듈을 참조하기 위해 추가한 것

from django.db import models
from django.utils import timezone  # Django 의 시간대 관련 유틸리티인 django.utils.timezone 을 참조하기 위해 추가한 것

# Create your models here.

class Question(models.Model):  # 각 필드가 어떤 자료형을 가질 수 있는지 Django에게 말해줌
    # question_text 와 pub_date 는 machine-friendly form 의 데이터베이스 필드 이름. 데이터베이스에서 컬럼명으로 사용할 것
    question_text = models.CharField(max_length=200)  # CharField 는 문자(character) 필드를 표현
    # Field 클래스인 CharField는 max_length라는 필수 인수가 필요함

    pub_date = models.DateTimeField('date published')  # DateTimeField 는 날짜와 시간(datetime) 필드를 표현
    # 'date published' 는 첫번째 위치 인수를 전달하여 human-readable 이름을 지정한 것임

    # Question.objects.all() 시에 question_text를 보기 위함
    def __str__(self):
        return self.question_text

    # 커스텀 메소드
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # on_delete 선택 인수는 Django 에서 모델을 구현할 때 ForeignKey Field 가 바라보는 값이 삭제될 때 해당 요소를 처리하는 방법을 지저
    # CASCADE : ForeignKey Field 를 포함하는 모델 인스턴스(row)도 같이 삭제한다
    # PROTECT, SET_NULL, SET_DEFAULT, SET(), DO_NOTHING 도 on_delete 의 선택 인수

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # default 라는 선택 인수를 통해 votes의 기본값을 0으로 설정함

    def __str__(self):
        return self.choice_text