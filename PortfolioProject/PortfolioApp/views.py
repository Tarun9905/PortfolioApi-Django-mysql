# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from PortfolioApp.serializers import PortfolioSerializer,UserSerializer
# from PortfolioApp.models import PortfolioDetails,User
# from django.views import View
# from django.utils.decorators import method_decorator
# import json
# from django.contrib.auth.hashers import check_password


# @method_decorator(csrf_exempt, name='dispatch')
# class PortfolioDetailsView(View):
#     def post(self, request):
#         try:
#             Portfolio_details = JSONParser().parse(request)  # Parse JSON from request body
#             Portfolio_serializer = PortfolioSerializer(data=Portfolio_details)

#             if Portfolio_serializer.is_valid():
#                 Portfolio_serializer.save()
#                 return JsonResponse({"message": "Added successfully"}, safe=False, status=201)

#             return JsonResponse(Portfolio_serializer.errors, safe=False, status=400)  # Return validation errors

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, safe=False, status=500)  # Log any unexpected error

#     def get(self, request, email=None):
#         if email:
#             try:
#                 Portfolio_details = PortfolioDetails.objects.filter(email=email)  # Use filter instead of get
#                 Portfolio_serializer = PortfolioSerializer(Portfolio_details, many=True)
#                 return JsonResponse(Portfolio_serializer.data, safe=False)
#             except Exception as e:
#                 return JsonResponse({'error': str(e)}, status=404)


# @method_decorator(csrf_exempt, name='dispatch')
# class UserRegister(View):
#     def post(self, request):
#         try:
#             User_details = JSONParser().parse(request)  # Parse JSON from request body
#             User_serializer = UserSerializer(data=User_details)

#             if User_serializer.is_valid():
#                 User_serializer.save()
#                 return JsonResponse({"message": "User added"}, safe=False, status=201)

#             return JsonResponse(User_serializer.errors, safe=False, status=400)  # Return validation errors

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, safe=False, status=500)  # Log any unexpected error

# @method_decorator(csrf_exempt, name='dispatch')
# class UserLogin(View):
#     def post(self, request):
#         try:
#             data = JSONParser().parse(request)  # Parse JSON from request
#             email = data.get('email')
#             password = data.get('password')

#             if not email or not password:
#                 return JsonResponse({"error": "Email and password are required"}, status=400)

#             # Check if the user exists
#             try:
#                 user = User.objects.get(email=email)
#             except User.DoesNotExist:
#                 return JsonResponse({"error": "Invalid email or password"}, status=401)

#             # Verify password (assuming password is stored as a hash)
#             if not check_password(password, user.password):
#                 return JsonResponse({"error": "Invalid email or password"}, status=401)

#             # Successful login
#             return JsonResponse({"message": "Login successful", "email": user.email}, status=200)

#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON format"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)


from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import PortfolioSerializer, UserSerializer
from .models import PortfolioDetails, User
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password, make_password
import json


@method_decorator(csrf_exempt, name='dispatch')
class PortfolioDetailsView(View):
    def post(self, request):
        try:
            portfolio_details = JSONParser().parse(request)  # Parse JSON from request body
            portfolio_serializer = PortfolioSerializer(data=portfolio_details)

            if portfolio_serializer.is_valid():
                portfolio_serializer.save()
                return JsonResponse({"message": "Added successfully"}, safe=False, status=201)

            return JsonResponse(portfolio_serializer.errors, safe=False, status=400)  # Return validation errors

        except Exception as e:
            return JsonResponse({"error": str(e)}, safe=False, status=500)  # Log any unexpected error

    def get(self, request, email=None):
        if email:
            try:
                portfolio_details = PortfolioDetails.objects.filter(email=email)  # Use filter instead of get
                portfolio_serializer = PortfolioSerializer(portfolio_details, many=True)
                return JsonResponse(portfolio_serializer.data, safe=False)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=404)

    # In views.py of Django backend
    def put(self, request, email=None):
        portfolio = PortfolioDetails.objects.get(email=email)
        data = JSONParser().parse(request)
        serializer = PortfolioSerializer(portfolio, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class UserRegister(View):
    def post(self, request):
        try:
            user_details = JSONParser().parse(request)  # Parse JSON from request body

            # Hash the password before saving
            user_details['password'] = make_password(user_details['password'])

            user_serializer = UserSerializer(data=user_details)

            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse({"message": "User registered successfully"}, safe=False, status=201)

            return JsonResponse(user_serializer.errors, safe=False, status=400)  # Return validation errors

        except Exception as e:
            return JsonResponse({"error": str(e)}, safe=False, status=500)  # Log any unexpected error


@method_decorator(csrf_exempt, name='dispatch')
class UserLogin(View):
    def post(self, request):
        try:
            data = JSONParser().parse(request)  # Parse JSON from request
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({"error": "Email and password are required"}, status=400)

            # Check if the user exists
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return JsonResponse({"error": "Invalid email or password"}, status=401)

            # Verify password
            if not check_password(password, user.password):
                return JsonResponse({"error": "Invalid email or password"}, status=401)

            # Successful login
            return JsonResponse({"message": "Login successful", "email": user.email}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
