from rest_framework.routers import SimpleRouter

from red_hot_chilli_giraffe.accounts.views import RegisterView, ProfileView

router = SimpleRouter()

router.register(r"auth/register", RegisterView, "register")
router.register(r"auth", ProfileView, "profile")
