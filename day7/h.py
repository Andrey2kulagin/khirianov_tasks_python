def dot_product(N, vector1, vector2):
    product = 0
    for i in range(N):
        product += vector1[i]*vector2[i]
    return product
