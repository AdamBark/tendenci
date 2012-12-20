from haystack.query import SearchQuerySet

from django.db.models import Manager
from django.db.models import Q


class CorporateMembershipManager(Manager):
    def search(self, query=None, *args, **kwargs):
        """
        haystack to query corporate memberships.
        Returns a SearchQuerySet
        """
        from tendenci.addons.corporate_memberships.models import CorporateMembership

        sqs = SearchQuerySet().models(CorporateMembership)

        if query:
            sqs = sqs.filter(content=sqs.query.clean(query))
        else:
            sqs = sqs.all()

        # the filter logic for the permission is handled in the search view

        return sqs


class CorpMembershipManager(Manager):
    def search(self, query=None, *args, **kwargs):
        """
        haystack to query corporate memberships.
        Returns a SearchQuerySet
        """
        from tendenci.addons.corporate_memberships.models import CorpMembership

        sqs = SearchQuerySet().models(CorpMembership)

        if query:
            sqs = sqs.filter(content=sqs.query.clean(query))
        else:
            sqs = sqs.all()

        # the filter logic for the permission is handled in the search view

        return sqs


class CorpMembershipAppManager(Manager):
    def current_app(self, **kwargs):
        """
        Returns the app being used currently.
        """
        [current_app] = self.filter(
                           status=True,
                           status_detail__in=['active', 'published']
                           ).order_by('id')[:1] or [None]

        return current_app
