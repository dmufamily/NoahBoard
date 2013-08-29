from django.db import models

# Create your models here.




#BasicInfo
class BasicInfo(models.Model):
    email_address= models.EmailField()
    linkedin_member_id=models.CharField(max_length=20)
    facebook_member_id=models.CharField(max_length=20)
    website = models.URLField()
    account_type = models.CharField(max_length=1)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #work is different form the db design
    about_me = models.CharField(max_length=300)
    ACCESS_RIGHTS = (
        ('PUB', 'Public'),
        ('PRI', 'Private')
    )
    access_rights = models.CharField(max_length=3, choices=ACCESS_RIGHTS)


#WorkPlace class
class WorkPlace(models.Model):
    company_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    position = models.CharField(max_length=30)
    start_date = models.DateField()
    basic_infor = models.ForeignKey(BasicInfo)

#KnowledgeBoard
class KnowledgeBoard(models.Model):
    def __unicode__(self):
        return ""

 #KnowledgProfile
class KnowledgeProfile(models.Model):
    interests = models.CharField(max_length=50)
    num_flowers = models.IntegerField()
    num_posts = models.IntegerField()
    num_tags = models.IntegerField()
    num_followings = models.IntegerField()
    num_followers = models.IntegerField()
    ACCESS_RIGHTS = (
        ('PUB', 'Public'),
        ('PRI', 'Private'),
    )
    access_rights = models.CharField(max_length=3, choices=ACCESS_RIGHTS)
    knowledge_board = models.OneToOneField(KnowledgeBoard)


#UserProfile
class UserProfile(models.Model):
    basic_info = models.OneToOneField(BasicInfo)
    followers = models.ManyToManyField(BasicInfo,related_name="followers_basic_info")
    knowledge_profile = models.OneToOneField(KnowledgeProfile)


#KnowledgeCard


class KnowledgeCard(models.Model):
    knowledge_board = models.ForeignKey(KnowledgeBoard)
    title = models.CharField(max_length=30)
    #need to verify max chars
    contents = models.CharField(max_length=450)
    picture = models.ImageField(upload_to='/Users/jinguangzhou/git/NoahBoard/images')
    video_link = models.URLField()
    source_link = models.URLField()
    CATEGORIES = (
        ('IT', 'Technology'),
        ('ST', 'Startup'),
    )
    category = models.CharField(max_length=2, choices=CATEGORIES)
    TAGS = (
        ('JAVA', 'Java'),
        ('Python', 'Python'),
    )
    tags = models.CharField(max_length=10, choices=TAGS)
    post_date = models.DateField()
    num_thumbs = models.IntegerField()
    num_shares = models.IntegerField()
    num_comments = models.IntegerField()
    ACCESS_RIGHTS = (
        ('PUB', 'Public'),
        ('PRI', 'Private'),
    )
    access_rights = models.CharField(max_length=3, choices=ACCESS_RIGHTS)


#Comments
class Comment(models.Model):
    knowledge_card = models.ForeignKey(KnowledgeCard)
    contents = models.CharField(max_length=100)
    post_date = models.DateField()
    num_upvotes = models.IntegerField()
