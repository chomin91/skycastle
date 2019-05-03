from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
import re
import logging
logger = logging.getLogger(__name__)

class UserManager(BaseUserManager):
	def validation_check(self, email, password):
		email_check = re.compile('^[\w_\.-]{1,50}@[\w_\.-]{1,50}\.(\w{1,10})$')
		pw_check = re.compile('^[\w~`!@#$%^&*()_+=\.-]{8,30}$')

		if email_check.match(email) and pw_check.match(password):
			return True
		else:
			print(logger, " // ",  __name__, ": signup validation error")
			return False

	def _create_user(self, email, password, user_type, **extra_fields):
		if self.validation_check(email, password):
			email = self.normalize_email(email)
			user = self.model(email=email, **extra_fields)
			user.set_password(password)
			user.user_type = user_type
			user.save(using=self._db)
			return user
		else:
			return None
  
	def create_coordinator(self, email, password, **extra_fields):	
		return self._create_user(email, password, 2, **extra_fields)

	def create_parent(self, email, password, **extra_fields):
		return self._create_user(email, password, 3, **extra_fields)
    
	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)
		return self._create_user(email, password, 1, **extra_fields)
    
	def SetCoordinatorInfo(self, coordi, gender, age, university, major, classOf, CSATScore, schoolScore, CSATScoreImage, schoolScoreImage, profileImage):        
		coordiInfo = CoordinatorInfo.objects.get(user=coordi)
		coordiInfo.gender = gender
		coordiInfo.age = age
		coordiInfo.university = university
		coordiInfo.major = major
		coordiInfo.classOf = classOf
		coordiInfo.CSATScore = CSATScore
		coordiInfo.schoolScore = schoolScore
		coordiInfo.CSATScoreImage = CSATScoreImage
		coordiInfo.schoolScoreImage = schoolScoreImage
		coordiInfo.profileImage = profileImage
		coordiInfo.save()
		coordi.save()
		print(coordi.coordi_info) # error....

	def SetStudentInfo(self, gender, age, schoolYear, major, addressState, addressCity, addressDetail):
		student = self.model
		student.gender = gender
		student.age = age
		student.schoolYear = schoolYear
		student.major = major
		student.addressState = addressState
		student.addressCity = addressCity
		student.addressDetail = addressDetail

class User(AbstractBaseUser, PermissionsMixin):
	USER_TYPES = (
		(1, 'admin'),
		(2, 'coordinator'),
		(3, 'parent'),
	)

	email = models.EmailField(_('email address'),
		unique=True,
		error_messages={'unique': _("이미 존재하는 메일주소입니다.")}
	)

	user_type = models.PositiveSmallIntegerField(choices=USER_TYPES)
	is_staff = models.BooleanField(_('staff status'), default=False,)

	objects = UserManager()
	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = ['email', 'user_type']

class CoordinatorInfo(models.Model):
	user = models.OneToOneField(User, on_delete='CASCADE', related_name='coordi_info')
	gender = models.BooleanField(_('gender'))
	age = models.IntegerField(_('age'))
	university = models.CharField(_('university'), max_length=100)
	major = models.CharField(_('major'), max_length=100)
	classOf = models.IntegerField(_('class of'))
	CSATScore = models.IntegerField(_('CSAT score'))
	schoolScore = models.IntegerField(_('school score'))
	CSATScoreImage = models.ImageField(_('CAST score image'), upload_to='uploads/')
	schoolScoreImage = models.ImageField(_('school score image'), upload_to='uploads/')
	profileImage = models.ImageField(_('profile picture'), upload_to='uploads/')
	objects = UserManager()

class StudentInfo(models.Model):
	user = models.OneToOneField(User, on_delete='CASCADE')
	gender = models.BooleanField(_('gender'))
	age = models.IntegerField(_('age'))
	schoolYear = models.CharField(_('school year'), max_length=30)
	major = models.CharField(_('major'), max_length=30)
	addressState = models.CharField(_('address_state'), max_length=100)
	addressCity = models.CharField(_('address_city'), max_length=100)
	addressDetail = models.CharField(_('address_detail'), max_length=100)
	objects = UserManager()
