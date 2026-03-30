def serve_tea():
    yield "Tea for Customer 1"
    yield "Tea for Customer 2"
    yield "Tea for Customer 3"
for tea in serve_tea():
    print(tea)