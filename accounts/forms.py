from django import forms
from .models import User
from .models import CoordinatorInfo

class SignupForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput, label='비밀번호')	
	
	class Meta:
		model = User
		fields = [
                'email',
                ]

		labels = {
                'email': '이메일',
                }
	
class CoordiInfoForm(forms.ModelForm):
    class Meta:
        model = CoordinatorInfo
        fields = [
                'gender',
                'age',
                'university',
                'major',
                'classOf',
                'CSATScore',
                'schoolScore',
                'CSATScoreImage',
                'schoolScoreImage',
                'profileImage',
                ]
        labels = {
                'gender':'성별',
                'age':'나이',
                'university':'대학교',
                'major':'전공',
                'classOf':'학번',
                'CSATScore':'수능점수',
                'schoolScore':'내신점수',
                'CSATScoreImage':'수능성적표',
                'schoolScoreImage':'내신성적표',
                'profileImage':'프로필사진',
                }

class UnivInfoForm(forms.ModelForm):
	class Meta:
		model = CoordinatorInfo
		fields = [
				'university',
				'major',
				'classOf',
				]
