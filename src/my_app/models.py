from django.db import models

import random
import string
from django.db import models


# Create your models here.

class Links(models.Model):
    old_link = models.URLField()
    new_link = models.URLField()
    
    def save(self, *args, **kwargs):
        if not self.new_link:
            self.new_link = self.get_url()
        super(Links, self).save(*args, **kwargs)

    def get_url(self):
        current_codes = list(Links.objects.values_list(
            'new_link', flat=True))
        while True:
            new_link = self.gen_url()
            if new_link not in current_codes:
                break
            else:
                continue
        return new_link

    
    @staticmethod
    def gen_url():
        url = ''
        for i in range(4):
            url += random.choice(string.ascii_lowercase)
        return url