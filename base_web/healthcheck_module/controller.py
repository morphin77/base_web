class HealthCheckController:
    @staticmethod
    async def get_health_check():
        return {
            'response': 'ok'
        }