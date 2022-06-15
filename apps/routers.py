from apps.healths.routers import healths_routes
from apps.api.routers import views_routes


def initial_routes(api, prefix='/api/v1'):
    healths_routes(api, prefix)

    views_routes(api, prefix)
