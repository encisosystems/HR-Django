from django.db import models

class Area(models.Model):
    """
    In this model the departments/Area that the organization owns are created.
    """

    areaName = models.CharField(
        verbose_name = 'Area name',
        max_length=250, 
        help_text="Department/Area name")
    areaDescription = models.CharField(
        verbose_name = 'Area description',
        max_length=500, 
        help_text="Description of the department/area")
    areaCode = models.CharField(
        verbose_name = 'Area Code',
        max_length=250, 
        help_text="Department/Area code")

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        """Return area name"""
        return self.areaName

class JobDescription(models.Model):
    """
    In this model the job descriptions to be used for recruitments are created.
    Stores a Job Description entry, related to :model:`auth.User` and :model:`hr.Area`.  
    """

    createdBy = models.CharField(
        verbose_name = 'Created by',
        max_length=250,
        help_text="User creating the job description")
    creationDate = models.DateField(
        verbose_name = 'Creation date',
        help_text="Creation date for job description")
    code = models.CharField(
        verbose_name = 'Code',
        max_length=250, 
        help_text="ID of the job description")
    title = models.CharField(
        verbose_name = 'Title',
        max_length=250, 
        help_text="Title/name of the job description")
    departament = models.ForeignKey(
        Area,
        null=False,
        on_delete=models.CASCADE,  
        verbose_name = 'Departament',
        help_text="Department/Area associated with the job description")
    reportTo = models.CharField(
        verbose_name = 'Report to',
        max_length=250, 
        help_text="Immediate supervisor associated with the job description")
    jobDescription = models.CharField(
        verbose_name = 'Job description',
        max_length=500, 
        help_text="Job description")
    responsabilities = models.CharField(
        verbose_name = 'Responsabilities',
        max_length=500, 
        help_text="Job functions")
    skills = models.CharField(
        verbose_name = 'Skills',
        max_length=500, 
        help_text="The capacities to perform tasks that you are developed")
    abilities = models.CharField(
        verbose_name = 'Abilities',
        max_length=250,
        help_text="Talents you are born with.")
    experience = models.CharField(
        verbose_name = 'Experience',
        max_length=250,
        help_text="Time of experience on the job")
    educationRequirements = models.CharField(
        verbose_name = 'Education requirements',
        max_length=250,
        help_text="Level of education required")
    knowledge = models.CharField(
        verbose_name = 'Knowledge',
        max_length=250,
        help_text="Knowledge required for the job")
    annualSalary = models.DecimalField(
        verbose_name = 'Annual salary', 
        default = 0,
        decimal_places = 2,
        max_digits = 11,
        help_text="Approximate annual salary")

    class Meta:
        verbose_name = 'Job description'
        verbose_name_plural = 'Job descriptions'

    def __str__(self):
        """Return code job description"""
        return self.code

class Recruitment(models.Model):
    """  
    Recruitment applications are created in this model.
    
    Stores a Recruitment entry, related to :model:`auth.User`, :model:`hr.JobDescription` and :model:`hr.Area`. 
    """

    requester = models.CharField(
        verbose_name = 'Requester',
        max_length=250, 
        help_text="User who created the request")
    dateOfRequest = models.DateField(
        verbose_name = 'Date of request',
        help_text="Date of recruitment request")
    departament = models.ForeignKey(
        Area,
        null=False,
        on_delete=models.CASCADE,
        verbose_name = 'Departament',
        help_text="Department/Area that require the recruitment")
    departament_req = models.CharField(
        verbose_name = 'Departament',
        max_length=250, 
        help_text="Department/Area that require the recruitment - requester")
    jobDescription = models.ForeignKey(
        JobDescription,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name = 'Job description',
        help_text="Associated job description")
    startingDate = models.DateField(
        verbose_name = 'Starting date',
        help_text="Start date of the job")
    numberOfVacancies = models.PositiveIntegerField(
        verbose_name = 'Number of vacancies',
        help_text="Number of vacancies available")
    title = models.CharField(
        verbose_name = 'Title',
        max_length=250, 
        help_text="Name of vacancy")
    title_req = models.CharField(
        verbose_name = 'Title',
        max_length=250, 
        help_text="Name of vacancy - requester")
    responsabilities = models.CharField(
        verbose_name = 'Responsabilities',
        max_length=500, 
        help_text="Job functions")
    location = models.CharField(
        verbose_name = 'Location',
        max_length=250, 
        help_text="Work location")
    comments = models.CharField(
        verbose_name = 'Comments',
        blank=True,
        max_length=500, 
        help_text="A maximum of 500 characters is allowed")
    requisitionApproved = models.BooleanField(
        verbose_name = 'Requisition approved', 
        default=False,
        help_text="Requisition Approved?")
    approvalsComments = models.CharField(
        verbose_name = 'Approvals comments',
        blank=True,
        max_length=500, 
        help_text="A maximum of 500 characters is allowed")

    class Meta:
        verbose_name = 'Recruitment'
        verbose_name_plural = 'recruitments'

    def __str__(self):
        """Return title of recruitment"""
        return self.title