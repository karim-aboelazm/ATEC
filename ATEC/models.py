from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

class Univeristy(models.Model):
    logo            = models.ImageField(_("logo"),upload_to="University/Logo", blank=True, null=True) 
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    email           = models.EmailField(_("email"),max_length=100)
    country_en      = models.CharField(_("country_en"),max_length=100)
    country_ar      = models.CharField(_("country_ar"),max_length=100)
    privacy_en      = models.CharField(_("privacy_en"),max_length=100)
    privacy_ar      = models.CharField(_("privacy_ar"),max_length=100)
    city_en         = models.CharField(_("city_en"),max_length=100)
    city_ar         = models.CharField(_("city_ar"),max_length=100)
    phone           = models.CharField(_("phone"),max_length=20)
    description_en  = models.TextField(_("description_en"),max_length=1000)
    description_ar  = models.TextField(_("description_ar"),max_length=1000)
    facebook        = models.URLField(_("facebook"),max_length=100, blank=True, null=True)
    twitter         = models.URLField(_("twitter"),max_length=100, blank=True, null=True)
    linkedin        = models.URLField(_("linkedin"),max_length=100, blank=True, null=True)
    google_plus     = models.URLField(_("google_plus"),max_length=100, blank=True, null=True)
    video           = models.FileField(_("video"),upload_to="University/Video", blank=True, null=True)
    class Meta:
        verbose_name_plural = _('University')
    def __str__(self):
        return self.name_en + " University"

class Achivement(models.Model):
    image           = models.ImageField(_("image"),upload_to="Achivement/Image", blank=True, null=True)
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    description_en  = models.TextField(_("description_en"),max_length=1000)
    description_ar  = models.TextField(_("description_ar"),max_length=1000)
    class Meta:
        verbose_name_plural = _('Achivement')
    def __str__(self):
        return self.name_en

class WorkFlow(models.Model):
    image           = models.ImageField(_("image"),upload_to="WorkFlow/Image", blank=True, null=True)
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    description_en  = models.TextField(_("description_en"),max_length=1000)
    description_ar  = models.TextField(_("description_ar"),max_length=1000)
    class Meta:
        verbose_name_plural = _('WorkFlow')
    def __str__(self):
        return self.name_en

class Service(models.Model):
    image           = models.ImageField(_("image"),upload_to="Service/Image", blank=True, null=True)
    icon            = models.CharField(_("icon"),max_length=100)
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    description_en  = models.TextField(_("description_en"),max_length=1000)
    description_ar  = models.TextField(_("description_ar"),max_length=1000)
    class Meta:
        verbose_name_plural = _('Service')
    def __str__(self):
        return self.name_en

class Category(models.Model):
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    class Meta:
        verbose_name_plural = _('Category')
    def __str__(self):
        return self.name_en

class Levels(models.Model):
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    class Meta:
        verbose_name_plural = _('Levels')
    def __str__(self):
        return self.name_en

class Courses(models.Model):
    image           = models.ImageField(_("image"),upload_to="Courses/Image", blank=True, null=True)
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    reviws          = models.PositiveIntegerField(_("reviws"),default=0,validators=[MinValueValidator(1), MaxValueValidator(5)])
    old_price       = models.FloatField(_("old_price"),default=0)
    discount        = models.FloatField(_("discount"),default=0)
    new_price       = property(lambda self: self.old_price - (self.old_price * self.discound / 100))
    status          = models.BooleanField(_("status"),default=True)
    offer           = models.BooleanField(_("offer"),default=False)

    class Meta:
        verbose_name_plural = _('Courses')
    def __str__(self):
        return self.name_en

class Lessons(models.Model):
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    course          = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='lessons')
    video           = models.FileField(_("video"),upload_to="Lessons/Video", blank=True, null=True)
    duration        = models.PositiveIntegerField(_("duration"),default=0)
    level           = models.ForeignKey(Levels, on_delete=models.CASCADE, related_name='lessons')
    class Meta:
        verbose_name_plural = _('Lessons')
    def __str__(self):
        return self.name_en

class CourseOutcomes(models.Model):
    course          = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='course_outcomes')
    description_en  = models.CharField(_("description_en"),max_length=100)
    description_ar  = models.CharField(_("description_ar"),max_length=100)
    class Meta:
        verbose_name_plural = _('Course Outcomes')
    def __str__(self):
        return self.course.name_en + f" outcome {self.id}" 

class CoursesDetails(models.Model):
    course          = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='courses_details')
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    description_en  = models.TextField(_("description_en"),max_length=1000)
    description_ar  = models.TextField(_("description_ar"),max_length=1000)
    certification_en= models.TextField(_("certification_en"),max_length=1000)
    certification_ar= models.TextField(_("certification_ar"),max_length=1000)
    outcome         = models.ManyToManyField(CourseOutcomes, related_name='courses_details')
    lectures        = models.PositiveIntegerField(_("lectures"),default=0)
    duration        = models.PositiveIntegerField(_("duration"),default=0)
    quizzes         = models.PositiveIntegerField(_("quizzes"),default=0)
    for_whom_en     = models.CharField(_("for_whom_en"),max_length=100)
    for_whom_ar     = models.CharField(_("for_whom_ar"),max_length=100)
    language        = models.CharField(_("language"),max_length=100)
    
    class Meta:
        verbose_name_plural = _('Courses Details')
    def __str__(self):
        return self.name_en

class CourseInstructor(models.Model):
    course          = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='course_instructor')
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    profession_en   = models.CharField(_("profession_en"),max_length=100)
    profession_ar   = models.CharField(_("profession_ar"),max_length=100)
    description_en  = models.TextField(_("description_en"),max_length=1000)
    description_ar  = models.TextField(_("description_ar"),max_length=1000)
    image           = models.ImageField(_("image"),upload_to="CourseInstructor/Image", blank=True, null=True)
    facebook        = models.URLField(_("facebook"),max_length=100, blank=True, null=True)
    twitter         = models.URLField(_("twitter"),max_length=100, blank=True, null=True)
    linkedin        = models.URLField(_("linkedin"),max_length=100, blank=True, null=True)
    google_plus     = models.URLField(_("google_plus"),max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = _('Course Instructor')
    def __str__(self):
        return self.name_en

class Statistics(models.Model):
    icon            = models.CharField(_("icon"),max_length=100)
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    number          = models.PositiveIntegerField(_("number"),default=0)
    class Meta:
        verbose_name_plural = _('Statistics')
    def __str__(self):
        return self.name_en

class Events(models.Model):
    image           = models.ImageField(_("image"),upload_to="Events/Image", blank=True, null=True)
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    date            = models.DateField(_("date"))
    start_time      = models.TimeField(_("start_time"))
    end_time        = models.TimeField(_("end_time"))
    description_en  = models.TextField(_("description_en"),max_length=1000)
    description_ar  = models.TextField(_("description_ar"),max_length=1000)
    location_en     = models.CharField(_("location_en"),max_length=100)
    location_ar     = models.CharField(_("location_ar"),max_length=100)
    class Meta:
        verbose_name_plural = _('Events')
    def __str__(self):
        return self.name_en

class Testimonials(models.Model):
    image           = models.ImageField(_("image"),upload_to="Testimonials/Image", blank=True, null=True)
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    profession_en   = models.CharField(_("profession_en"),max_length=100)
    profession_ar   = models.CharField(_("profession_ar"),max_length=100)
    letter_en       = models.TextField(_("letter_en"),max_length=300)
    letter_ar       = models.TextField(_("letter_ar"),max_length=300)
    class Meta:
        verbose_name_plural = _('Testimonials')
    def __str__(self):
        return self.name_en

class News(models.Model):
    image           = models.ImageField(_("image"),upload_to="News/Image", blank=True, null=True)
    title_en         = models.CharField(_("title_en"),max_length=100)
    title_ar         = models.CharField(_("title_ar"),max_length=100)
    date            = models.DateField(_("date"))
    author_en       = models.CharField(_("author_en"),max_length=100)
    author_ar       = models.CharField(_("author_ar"),max_length=100)
    description_en  = models.CharField(_("description_en"),max_length=200)
    description_ar  = models.CharField(_("description_ar"),max_length=200)

    class Meta:
        verbose_name_plural = _('News')
    def __str__(self):
        return self.name_en

class Subscribe(models.Model):
    email           = models.EmailField(_("email"),max_length=100)
    class Meta:
        verbose_name_plural = _('Subscribe')
    def __str__(self):
        return self.email

class Gallery(models.Model):
    image           = models.ImageField(_("image"),upload_to="Gallery/Image", blank=True, null=True)
    class Meta:
        verbose_name_plural = _('Gallery')
    def __str__(self):
        return self.image

class FAQ(models.Model):
    question_en     = models.CharField(_("question_en"),max_length=100)
    question_ar     = models.CharField(_("question_ar"),max_length=100)
    answer_en       = models.TextField(_("answer_en"),max_length=1000)
    answer_ar       = models.TextField(_("answer_ar"),max_length=1000)
    class Meta:
        verbose_name_plural = _('FAQ')
    def __str__(self):
        return self.question_en

class Contact(models.Model):
    name            = models.CharField(_("name"),max_length=100)
    email           = models.EmailField(_("email"),max_length=100)
    subject         = models.CharField(_("subject"),max_length=100)
    message         = models.TextField(_("message"),max_length=1000)
    class Meta:
        verbose_name_plural = _('Contact')
    def __str__(self):
        return self.name

class MemberShips(models.Model):
    name_en         = models.CharField(_("name_en"),max_length=100)
    name_ar         = models.CharField(_("name_ar"),max_length=100)
    description_en  = models.CharField(_("description_en"),max_length=100)
    description_ar  = models.CharField(_("description_ar"),max_length=100)
    price           = models.PositiveIntegerField(_("price"),default=0)
    duration        = models.PositiveIntegerField(_("duration"),default=0)
    fee_time        = models.PositiveIntegerField(_("fee_time"),default=0)
    num_users       = models.PositiveIntegerField(_("num_users"),default=0)
    avilaibility    = models.PositiveIntegerField(_("avilaibility"),default=0)
    features        = models.PositiveIntegerField(_("features"),default=0)
    no_day_list     = models.PositiveIntegerField(_("no_day_list"),default=0)
    support         = models.PositiveIntegerField(_("support"),default=0)
    select          = models.BooleanField(_("select"),default=False)
    class Meta:
        verbose_name_plural = _('MemberShips')
    def __str__(self):
        return self.name_en

class WhyUs(models.Model):
    question_en     = models.CharField(_("question_en"),max_length=100)
    question_ar     = models.CharField(_("question_ar"),max_length=100)
    answer_en       = models.TextField(_("answer_en"),max_length=1000)
    answer_ar       = models.TextField(_("answer_ar"),max_length=1000)
    video           = models.FileField(_("video"),upload_to="WhyUs/Video", blank=True, null=True)
    class Meta:
        verbose_name_plural = _('WhyUs')
    def __str__(self):
        return self.question_en
