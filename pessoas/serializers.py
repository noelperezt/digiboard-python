from rest_framework import serializers
from pessoas.models import Pessoas

class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = ('id', 'nome', 'cargo', 'cpf', 'foto')

    