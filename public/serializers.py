from rest_framework import serializers

from public.models import Todos


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'
        read_only_fields = ('id','created_at','updated_at')