from django.db import models

class Log(models.Model):
    uid = models.IntegerField(primary_key=True)
    workpackages = models.TextField(null=True, blank=False)

    def __str__(self):
        return str(self.uid)


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2020 miraculix-org Florian Kleber