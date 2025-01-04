from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .services import get_and_validate_hash


class TransactionDataAPIView(APIView):
    """ Get info about transaction using hash """
    def post(self, request):
        hash, blockchain = get_and_validate_hash(request)

        return Response({'hash': hash, 'blockchain': blockchain})
