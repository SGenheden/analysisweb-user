"""
Module containing the user-defined DB relationship model
"""
import json

from analysisweb.api.base_models import *
from analysisweb.api.mixin_models import *


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    measurements = relationship('Measurement', backref='user')


class Measurement(MeasurementMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @property
    def meta_data(self):
        if self.user:
            return {
                "user": {
                    "username": self.user.username,
                    "email": self.user.email
                }
            }
        else:
            return {
                "user": {
                    "username": "",
                    "email": ""
                }
            }

    @meta_data.setter
    def meta_data(self, value):
        if not value:
            return

        if "user" not in value or "username" not in value["user"] or "email" not in value["user"]:
            raise MetaDataException("Invalid format of metadata")

        db_user = User.query.filter(User.username == value["user"]["username"],
                                    User.email == value["user"]["email"]).first()
        if not db_user:
            db_user = User(username=value["user"]["username"], email=value["user"]["email"])
            db.session.add(db_user)
            db.session.flush()

        self.user = db_user


class Analysis(AnalysisMixin, db.Model):
    pass
