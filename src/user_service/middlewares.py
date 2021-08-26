def metrics_middleware(get_response):

    def middleware(request):
        tick = time.time()
        response = get_response(request)
        tok = time.time()
        portal_requests_latency.labels(request.method, request.path).observe(tok-tick)
        portal_requests.labels(request.method, request.path).inc()
        return response

    return middleware