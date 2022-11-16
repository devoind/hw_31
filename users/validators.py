from rest_framework import serializers
from django.core.exceptions import ValidationError

from dateutil.relativedelta import relativedelta
from datetime import date

from avito.settings import USER_MIN_AGE


def birth_date_validator(value):
    diff_years = relativedelta(date.today(), value).years
    if diff_years < USER_MIN_AGE:
        raise ValidationError('User is to underage')
    return value


def email_validator(value):
    if value.endswith('rambler.ru'):
        raise serializers.ValidationError(f'Cant register email from this domain - {value}')
    return value
