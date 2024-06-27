from rest_framework import serializers

from shared.utils import send_code_to_email, send_code_to_phone
from users.models import UserModel, VIA_EMAIL, VIA_PHONE


class SignUpSerializer(serializers.ModelSerializer):
    def __init__(self):
        super(SignUpSerializer, self).__init__()
        self.fields['email_phone_number'] = serializers.CharField(max_length=256)

    class Meta:
        model = UserModel
        fields = ['uuid', 'auth_type', 'auth_status']

    def validate(self, attrs):
        return self.auth_validate(attrs)

    def create(self, validated_data):
        user = super(SignUpSerializer, self).create(validated_data)
        code = user.create_verify_code(verify_type=user.verify_type)
        if user.verify_type == VIA_EMAIL:
            send_code_to_email(user.email, code)
        else:
            send_code_to_phone(user.phone_number, code)
        user.save()
        return user

    @staticmethod
    def auth_validate(data: dict):
        user_input = str(data.get('email_phone_number', None))
        if user_input.endswith('@gmail.com'):
            data['email'] = user_input
            data['auth_type'] = VIA_EMAIL
        elif user_input.startswith('+'):
            data['phone_number'] = user_input
            data['auth_type'] = VIA_PHONE
        else:
            response = {
                'success': False,
                'message': 'Invalid email or phone'
            }
            raise serializers.ValidationError(response)
        return data
