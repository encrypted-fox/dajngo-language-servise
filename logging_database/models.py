from django.db import models

# Create your models here.


class LoggingDatabaseManager(models.Manager):
    def create_logging(self):
        logging_row = self.create()
        # do something with the book
        return logging_row


class LoggingDatabase(models.Model):
    req_body = models.TextField(default="")
    req_type = models.TextField()
    req_from = models.TextField()
    resp_status = models.TextField()
    resp_body = models.TextField(default="")
    req_date = models.TextField()
    resp_date = models.TextField()

    objects = LoggingDatabaseManager()