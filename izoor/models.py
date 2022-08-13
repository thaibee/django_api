from django.urls import reverse

from api.mssql_uuid import MssqlUUID
from django.db import models


class Wristband(models.Model):
    slug = models.CharField(db_column='Wrist_Num', max_length=10, editable=False, default=None)
    balance =  models.DecimalField(db_column='Top_up_rest', max_digits=19, decimal_places=4, blank=False, null=False) 

    def get_absolute_url(self):
        return reverse('org_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return 'W.'+self.Wrist_NUM

    # def get_countries(self):
    #     return self.org_country

    class Meta:
        managed = False
        db_table = 'Wristband'
        # ordering = ['org_name']
