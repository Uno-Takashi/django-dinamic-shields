from django.db.models import Model


class ShieldsDataModel(Model):
    label = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    color = models.CharField(max_length=15, default="lightgrey")
    labelColor = models.CharField(max_length=15, default="grey")
    isError = models.BooleanField(default=False)
    namedLogo = models.CharField(max_length=30, null=True)
    logoSvg = models.CharField(max_length=50000, null=True)
    logoColor = models.CharField(max_length=15, null=True)
    logoWidth = models.CharField(max_length=15, null=True)
    logoPosition = models.CharField(max_length=15, null=True)
    style = models.CharField(max_length=15, default="flat")
    cacheSeconds = models.IntegerField(default=300)
    updated_datetime = models.DateTimeField(auto_now=True)
