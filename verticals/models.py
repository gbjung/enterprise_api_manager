from django.db import models


class Vertical(models.Model):
    '''
    models for Vertical specifics
    ie. Gov, Law, Tax
    '''
    name = models.TextField(unique=True)

    def sections(self):
        return self.section_set.all()

    def __str__(self):
        return self.name

class Section(models.Model):
    '''
    models for various logical teams within a vertical
    '''
    name = models.TextField()
    vertical = models.ForeignKey(Vertical, related_name='sections', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def vertical_owner(self):
        return self.vertical

class Endpoint(models.Model):
    '''
    models for the actual api endpoints

    Can have Parameters and Contraints
    '''
    name = models.TextField()
    base_url = models.URLField()
    section = models.ForeignKey(Section, related_name="endpoints", on_delete=models.CASCADE)
    description = models.TextField()

    def vertical(self):
        return self.section.vertical.name

    def __str__(self):
        return self.name

class Constraint(models.Model):
    '''
    API Paywall constaints, values tied to verticals
    '''
    name = models.TextField()
    description = models.TextField()
    value = models.TextField()
    endpoints = models.ForeignKey(Endpoint, related_name="constraints", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Parameter(models.Model):
    '''
    API Parameters
    '''
    name = models.TextField()
    optional = models.BooleanField(default=True)
    accepted_values = models.TextField()
    description = models.TextField()
    endpoint = models.ForeignKey(Endpoint, related_name="parameters", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
