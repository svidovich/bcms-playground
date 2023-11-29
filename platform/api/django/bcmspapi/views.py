from bcmspapi.models import Verb
from rest_framework import routers, serializers, viewsets


class VerbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Verb
        fields = ["infinitive", "english"]


class VerbViewSet(viewsets.ModelViewSet):
    queryset = Verb.objects.all()
    serializer_class = VerbSerializer


router = routers.DefaultRouter()
router.register(r"verbs", VerbViewSet)
