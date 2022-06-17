import datetime
import os
import mongoengine as me
import pytz

from bson import ObjectId

timezone = pytz.timezone(os.environ.get('TZ', 'UTC'))


class BaseDocument(me.Document):
    meta = {'allow_inheritance': True, 'abstract': True}

    created_at = me.DateTimeField(required=True, default=datetime.datetime.now(timezone).astimezone())
    updated_at = me.DateTimeField(required=True, default=datetime.datetime.now(timezone).astimezone())

    def save(
            self,
            force_insert=False,
            validate=True,
            clean=True,
            write_concern=None,
            cascade=None,
            cascade_kwargs=None,
            _refs=None,
            save_condition=None,
            signal_kwargs=None,
            **kwargs,
    ):
        if not self.id:
            self.created_at = datetime.datetime.now(timezone).astimezone()
            # self.id = ObjectId()
        self.updated_at = datetime.datetime.now(timezone).astimezone()
        super().save(
            force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs, save_condition,
            signal_kwargs, **kwargs
        )
