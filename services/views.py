from builtins import staticmethod

from rest_framework.views import APIView, Response


class DocsView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        api_docs = response = {
            "api/v0/": {
                "documentation": {
                    "swagger": request.build_absolute_uri("api/v0/swagger"),
                    "redoc": request.build_absolute_uri("api/v0/redoc"),
                },
                "cities": request.build_absolute_uri("api/v0/cities"),
                "countries": request.build_absolute_uri("api/v0/countries"),
                "languages": request.build_absolute_uri("api/v0/languages"),
            }
        }
        return Response(api_docs)