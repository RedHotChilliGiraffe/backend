from rest_framework import serializers

from red_hot_chilli_giraffe.accounts.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        write_only_fields = ["password"]
        extra_kwargs = {
            "username": {"required": True, "allow_blank": False},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        """Create user object and set password."""
        user, created = User.objects.update_or_create(
            email__iexact=validated_data["email"],
            defaults={
                "email": validated_data["email"],
                "username": validated_data["username"],
            },
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
        ]
