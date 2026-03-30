# def serve_tea():
#     yield "Tea for Customer 1"
#     yield "Tea for Customer 2"
#     yield "Tea for Customer 3"
# for tea in serve_tea():
#     print(tea)

def papers_correction():
    yield "paper 1 is corrected"
    yield "paper 2 is corrected"
    yield "paper 3 is corrected"
for teacher in papers_correction():
    print(teacher)
