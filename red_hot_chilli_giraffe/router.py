from rest_framework import routers
from rest_framework.routers import SimpleRouter

from red_hot_chilli_giraffe.accounts.urls import router as accounts_router


class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for extending url routes from another router.
    """

    def extend(self, router: SimpleRouter) -> None:
        """
        Extend the routes with url routes of the passed in router.

        Args:
             router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)


router = DefaultRouter()
router.extend(accounts_router)
