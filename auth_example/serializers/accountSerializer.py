from auth_example.models.account import Account
from rest_framework import serializers
from auth_example.models.user import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['balance', 'last_change_date', 'is_active']

    def to_representation(self, obj):
        accountData = Account.objects.get(id=obj.id)
        userData    = User.objects.get(id=obj.user_id)
        return {
            'id' : accountData.id,
            'balance': accountData.balance,
            'lastChangeDate': accountData.last_change_date,
            'user': {
                'name': userData.balance,
                'email': userData.lastChangeDate
            }
        }
