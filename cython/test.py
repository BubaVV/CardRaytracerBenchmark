from card_raytracer import testVector, Vector

print(Vector(1, 2, 3))
print(Vector(1, 1, 1) + Vector(1, 1, 1))
print(Vector(1, 1, 1) * 3.1415)
print(Vector(1, 1, 1) % Vector(2, 2, 2))
print(Vector(1, 1, 1) ^ Vector(2, 2, 2))
print(~Vector(1, 1, 1))
testVector()