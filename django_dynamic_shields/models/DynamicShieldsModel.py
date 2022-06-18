from django.db.models import Model, CharField, IntegerField, BooleanField, DateTimeField


class ShieldsDataModel(Model):
    label = CharField(max_length=50)
    message = CharField(max_length=50)
    color = CharField(max_length=15, default="lightgrey")
    labelColor = CharField(max_length=15, default="grey")
    isError = BooleanField(default=False)
    namedLogo = CharField(max_length=30, null=True)
    logoSvg = CharField(max_length=50000, null=True)
    logoColor = CharField(max_length=15, null=True)
    logoWidth = CharField(max_length=15, null=True)
    logoPosition = CharField(max_length=15, null=True)
    style = CharField(max_length=15, default="flat")
    cacheSeconds = IntegerField(default=300)
    updated_datetime = DateTimeField(auto_now=True)
