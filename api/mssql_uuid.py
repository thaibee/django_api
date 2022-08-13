from uuid import UUID

from django.core.exceptions import ValidationError
from django.db.models import UUIDField


class MssqlUUID(UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 36
        super(UUIDField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        if self.primary_key:
            return 'uniqueidentifier default (newid())'
        else:
            return 'uniqueidentifier'

    def rel_db_type(self, connection):
        return 'uniqueidentifier'

    # leave id out of payload on insert
    def contribute_to_class(self, cls, name, **kwargs):
        assert not self.primary_key or (
                self.primary_key and not cls._meta.auto_field), "A model can't have more than one AutoField."
        super().contribute_to_class(cls, name, **kwargs)
        if self.primary_key:
            cls._meta.auto_field = self

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None
        if not isinstance(value, UUID):
            value = self.to_python(value)

        return str(value)

    def from_db_value(self, value, expression, connection):
        return self._to_uuid(value)

    def to_python(self, value):
        return self._to_uuid(value)

    def _to_uuid(self, value):
        if value is not None and not isinstance(value, UUID):
            try:
                return UUID(value)
            except (AttributeError, ValueError):
                raise ValidationError(
                    self.error_messages['invalid'],
                    code='invalid',
                    params={'value': value},
                )
        return value
