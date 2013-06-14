'''
Base armet resource for the api layer
'''

from __future__ import (division, print_function, unicode_literals,
                        absolute_import)
from armet import resources, authentication, authorization, exceptions
from tempfile import NamedTemporaryFile
import collections
import os
from django.contrib.auth.models import AnonymousUser

class SessionAuthentication(authentication.Authentication):

    allow_anonymous = True

    # TODO: Fix the possible information leak.  If a foreign site performs
    # a GET request on our resource with the user's session key, then they
    # can extract information from ardent.  See here for more info:
    # http://haacked.com/archive/2008/11/20/anatomy-of-a-subtle-json-vulnerability.aspx
    def authenticate(self, request):
        """Django session handling takes care of setting the user model here.
        """
        user = request.user
        # Authenticated users just return the users,
        # anyone else don't let them in.
        if user.is_authenticated():
            return user
        else:
            raise exceptions.Forbidden()

class ModelAuthorization(authorization.ModelAuthorization):

    def is_accessible(self, *args, **kwargs):
        # Our permissions backend doesn't support object-less permission
        # checking so skip this check.
        return True

class Resource(resources.Resource):

    # Only allow session auth and basic auth for now.
    authentication = (
        authentication.Basic(challenge=False),
        SessionAuthentication(),
    )


class ModelResource(resources.Model):

    prefetch = False

    # Only allow session auth and basic auth for now.
    authentication = (
        authentication.Basic(challenge=False),
        SessionAuthentication(),
    )

    authorization = ModelAuthorization()
