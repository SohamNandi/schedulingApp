from django.db import models


class User(models.Model):
    PermissionLevel = (
        ('ta', 'TA'),
        ('professor', 'Professor'),
        ('admin', 'Admin')
    )

    emailAddress = models.CharField(max_length=32)
    phoneNumber = models.CharField(max_length=16)
    homeAddress = models.CharField(max_length=64)
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    permission = models.CharField(max_length=16,
                                  choices=PermissionLevel,
                                  default=PermissionLevel[0])


class Course(models.Model):
    title = models.CharField(max_length=32)


class Assignment(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=65536)


class CourseToAssignedTAEntry(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=False)
    assignedTA = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    numAllowedLabs = models.IntegerField


class CourseToProfessorEntry(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=False)
    assignedProfessor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=False)
    title = models.CharField(max_length=32)
    assignedTA = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)

    def __init__(self, course, title):
        pass

    def __del__(self):
        pass

    # getters/setters
    def getCourse(self):
        pass

    def getTitle(self):
        pass

    # Following method is possibly outside the scope of the current sprint
    def getTAs(self):
        pass

    def setCourse(self, newCourse):
        pass

    def setTitle(self, newTitle):
        pass

    # Following 2 methods are possibly outside the scope of the current sprint
    def addTA(self, addTA):
        pass

    def removeTA(self, remTA):
        pass


