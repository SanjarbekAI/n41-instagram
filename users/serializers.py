from rest_framework import serializers

from shared.utils import send_code_to_email, send_code_to_phone
from users.models import UserModel, VIA_EMAIL, VIA_PHONE


class SignUpSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(SignUpSerializer, self).__init__(*args, **kwargs)
        self.fields['email_phone_number'] = serializers.CharField(max_length=128, required=False)

    uuid = serializers.IntegerField(read_only=True)
    auth_type = serializers.CharField(read_only=True, required=False)
    auth_status = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = UserModel
        fields = ['uuid', 'auth_type', 'auth_status']

    def validate(self, data):
        data = self.auth_validate(data=data)
        # auth_type = data['auth_type']
        # if auth_type == VIA_EMAIL:
        #     if UserModel.objects.filter(email=data['email']).exists():
        #         raise serializers.ValidationError("This email is already registered, use resend code api")
        # else:
        #     if UserModel.objects.filter(phone_number=data['phone_number']).exists():
        #         raise serializers.ValidationError("This phone number is already registered, use resend code api")
        return data

    def create(self, validated_data):
        user = super(SignUpSerializer, self).create(validated_data)
        code = user.create_verify_code(user.auth_type)

        if user.auth_type == VIA_EMAIL:
            send_code_to_email(user.email, code)
        else:
            send_code_to_phone(phone_number=user.phone_number, code=code)
        user.save()
        return user

    @staticmethod
    def auth_validate(data):
        user_input = str(data['email_phone_number']).lower()
        if user_input.endswith('@gmail.com'):
            data = {
                'email': user_input,
                'auth_type': VIA_EMAIL
            }
        elif user_input.startswith("+"):
            data = {
                'phone_number': user_input,
                'auth_type': VIA_PHONE
            }
        else:
            data = {
                'success': False,
                'message': "Please enter a valid phone number or email"
            }
            raise serializers.ValidationError(data)
        return data

    def to_representation(self, instance):
        data = super(SignUpSerializer, self).to_representation(instance)
        data['access_token'] = instance.token()['access_token']
        return data
