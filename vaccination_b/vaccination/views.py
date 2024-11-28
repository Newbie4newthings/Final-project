from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Individual, Admin
from .serializers import IndividualSerializer, AdminSerializer, AdminLoginSerializer

# Admin Registration API
class AdminRegister(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin Login API
class AdminLogin(APIView):
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({"message": "Login successful", "user": user.username}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CRUD Operations for Individual records
class IndividualList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # Create or update individual records
    def post(self, request):
        serializer = IndividualSerializer(data=request.data)
        if serializer.is_valid():
            individual, created = Individual.objects.update_or_create(
                individual_id=request.data.get('individual_id'),
                defaults=serializer.validated_data
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # List all individuals
    def get(self, request):
        individuals = Individual.objects.all()
        serializer = IndividualSerializer(individuals, many=True)
        return Response(serializer.data)

# Individual Detail API (get individual by id)
class IndividualDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, individual_id):
        try:
            individual = Individual.objects.get(individual_id=individual_id)
        except Individual.DoesNotExist:
            return Response({"detail": "Individual not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = IndividualSerializer(individual)
        return Response(serializer.data)

    # Update individual record
    def put(self, request, individual_id):
        try:
            individual = Individual.objects.get(individual_id=individual_id)
        except Individual.DoesNotExist:
            return Response({"detail": "Individual not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = IndividualSerializer(individual, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete individual record
    def delete(self, request, individual_id):
        try:
            individual = Individual.objects.get(individual_id=individual_id)
        except Individual.DoesNotExist:
            return Response({"detail": "Individual not found"}, status=status.HTTP_404_NOT_FOUND)
        
        individual.delete()
        return Response({"detail": "Individual deleted"}, status=status.HTTP_204_NO_CONTENT)
