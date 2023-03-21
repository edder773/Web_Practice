from django import forms
from .models import Article
# Django form 종류는 2가지
# 1. form -> 사용자의 입력을 받기위해 사용
# - 사용자의 입력을 개발자가 직접 구성
# -> Model의 필드와 관계없이 마음대로 구성
# 장점 : 내 마음대로 원하는 입력을 받을 수 있음
# 단점 : DB에 정확히 저장하기 위해서는 Models를 완벽하게 파악
#        models.py와 중복 코드가 많이 발생
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=30)
    # widget : form이 지원하는 기본 기능 외의 추가적인 동작을 원할 때 사용
    content = forms.CharField(widget=forms.Textarea)
# 2. Modelform
# - model에 정의된 필드만 입력 받을 수 있음
# - 장점 : 사용법이 너무 쉽다
# - 단점 : 내 마음대로 입력을 못 받는다

class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'Enter the title',
            }
        ),
    )
    class Meta:
        # 특정 모델을 참조 해야 함
        model = Article
        # 모든 필드 입력 받을시
        fields = '__all__'
        #원하는 필드만 입력받을시 튜플이나 리스트 형태로 작성
        # fields = ('title',) # 반드시 뒤에 콤마로 튜플로 표시
        
        # 특정 필드만 제외하고 입력을 받고 싶을 경우 exclude 사용
        # exclude = ('author',)
        