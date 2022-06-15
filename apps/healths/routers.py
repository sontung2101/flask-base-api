from apps.healths.v1.health import Health


def healths_routes(api, prefix):
    api.add_resource(Health, f'{prefix}/health')
