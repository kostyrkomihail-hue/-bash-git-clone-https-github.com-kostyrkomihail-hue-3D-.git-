python
   print("Hello, 3D-Project!")
python
   def main():
       print("Hello, 3D-Project!")

   if name == "main":
       main()
python
   def main():
       print("Hello, 3D-Project!")

   if name == "main":
       main()
python
     import src.main

     def testmainoutput():
         assert src.main.main() is Non
Цей проєкт призначений для роботи з 3D‑візуалізацією та прикладами інтеграції.
python
     from src.main import main
# Тут будуть залежності проєкту
pycache/
     *.pyc
     .DS_Store
     venv/
MIT License

   Copyright (c) 2026 [Твоє ім’я]

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction...
   python
   from setuptools import setup, find_packages

   setup(
       name="3D-project",
       version="0.1",
       packages=find_packages(),
   )
yaml
   name: Python application

   on: [push]

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.x'
         - name: Install dependencies
           run: pip install -r requirements.txt
         - name: Run tests
           run: pytest
yaml
   name: Python application

   on: [push]

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.x'
         - name: Install dependencies
           run: pip install -r requirements.txt
         - name: Run tests
           run: pytest
!CI
markdown
!CI
python
def add_numbers(a, b):
    return a + b
python
from src.main import add_numbers

def testaddnumbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
python
def vector_length(x, y, z):
    """Обчислює довжину 3D-вектора."""
    return (x2 + y2 + z2)  0.5
python
from src.main import vector_length

def testvectorlength():
    assert vector_length(1, 0, 0) == 1
    assert vector_length(0, 3, 4) == 5
    assert round(vector_length(1, 2, 2), 5) == 3.0
python
def distancebetweenpoints(x1, y1, z1, x2, y2, z2):
    """Обчислює відстань між двома точками у 3D."""
    return ((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)  0.5
python
from src.main import distancebetweenpoints

def testdistancebetween_points():
    assert distancebetweenpoints(0, 0, 0, 1, 0, 0) == 1
    assert distancebetweenpoints(0, 0, 0, 0, 3, 4) == 5
    assert round(distancebetweenpoints(1, 2, 3, 4, 5, 6), 5) == 5.19615
python
def normalize_vector(x, y, z):
    """Повертає нормалізований 3D-вектор (довжина = 1)."""
    length = (x2 + y2 + z2)  0.5
    if length == 0:
        return (0, 0, 0)
    return (x/length, y/length, z/length)
У tests/test_main.py
`python
from src.main import normalize_vector

def testnormalizevector():
    assert normalize_vector(1, 0, 0) == (1.0, 0.0, 0.0)
    assert normalize_vector(0, 3, 4) == (0.0, 0.6, 0.8)
    nx, ny, nz = normalize_vector(1, 2, 2)
    assert round((nx2 + ny2 + nz2), 5) == 1.0
python
def add_numbers(a, b):
    """Проста функція додавання."""
    return a + b

def vector_length(x, y, z):
    """Обчислює довжину 3D-вектора."""
    return (x2 + y2 + z2)  0.5

def distancebetweenpoints(x1, y1, z1, x2, y2, z2):
    """Обчислює відстань між двома точками у 3D."""
    return ((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)  0.5

def normalize_vector(x, y, z):
    """Повертає нормалізований 3D-вектор (довжина = 1)."""
    length = (x2 + y2 + z2)  0.5
    if length == 0:
        return (0, 0, 0)
    return (x/length, y/length, z/length)

def dot_product(x1, y1, z1, x2, y2, z2):
    """Обчислює скалярний добуток двох 3D-векторів."""
    return x1x2 + y1y2 + z1*z2
python
from src.main import (
    add_numbers,
    vector_length,
    distancebetweenpoints,
    normalize_vector,
    dot_product
)

def testaddnumbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def testvectorlength():
    assert vector_length(1, 0, 0) == 1
    assert vector_length(0, 3, 4) == 5
    assert round(vector_length(1, 2, 2), 5) == 3.0

def testdistancebetween_points():
    assert distancebetweenpoints(0, 0, 0, 1, 0, 0) == 1
    assert distancebetweenpoints(0, 0, 0, 0, 3, 4) == 5
    assert round(distancebetweenpoints(1, 2, 3, 4, 5, 6), 5) == 5.19615

def testnormalizevector():
    assert normalize_vector(1, 0, 0) == (1.0, 0.0, 0.0)
    assert normalize_vector(0, 3, 4) == (0.0, 0.6, 0.8)
    nx, ny, nz = normalize_vector(1, 2, 2)
    assert round((nx2 + ny2 + nz2), 5) == 1.0

def testdotproduct():
    assert dot_product(1, 0, 0, 1, 0, 0) == 1
    assert dot_product(1, 2, 3, 4, 5, 6) == 32
    assert dot_product(0, 0, 0, 1, 2, 3) == 0
python
def add_numbers(a, b):
    """Проста функція додавання."""
    return a + b

def vector_length(x, y, z):
    """Обчислює довжину 3D-вектора."""
    return (x2 + y2 + z2)  0.5

def distancebetweenpoints(x1, y1, z1, x2, y2, z2):
    """Обчислює відстань між двома точками у 3D."""
    return ((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)  0.5

def normalize_vector(x, y, z):
    """Повертає нормалізований 3D-вектор (довжина = 1)."""
    length = (x2 + y2 + z2)  0.5
    if length == 0:
        return (0, 0, 0)
    return (x/length, y/length, z/length)

def dot_product(x1, y1, z1, x2, y2, z2):
    """Обчислює скалярний добуток двох 3D-векторів."""
    return x1x2 + y1y2 + z1*z2

def cross_product(x1, y1, z1, x2, y2, z2):
    """Обчислює векторний (крос) добуток двох 3D-векторів."""
    return (
        y1z2 - z1y2,
        z1x2 - x1z2,
        x1y2 - y1x2
    )

def midpoint(x1, y1, z1, x2, y2, z2):
    """Обчислює середню точку між двома точками у 3D."""
    return ((x1 + x2)/2, (y1 + y2)/2, (z1 + z2)/2)
python
from src.main import (
    add_numbers,
    vector_length,
    distancebetweenpoints,
    normalize_vector,
    dot_product,
    cross_product,
    midpoint
)

def testaddnumbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def testvectorlength():
    assert vector_length(1, 0, 0) == 1
    assert vector_length(0, 3, 4) == 5
    assert round(vector_length(1, 2, 2), 5) == 3.0

def testdistancebetween_points():
    assert distancebetweenpoints(0, 0, 0, 1, 0, 0) == 1
    assert distancebetweenpoints(0, 0, 0, 0, 3, 4) == 5
    assert round(distancebetweenpoints(1, 2, 3, 4, 5, 6), 5) == 5.19615

def testnormalizevector():
    assert normalize_vector(1, 0, 0) == (1.0, 0.0, 0.0)
    assert normalize_vector(0, 3, 4) == (0.0, 0.6, 0.8)
    nx, ny, nz = normalize_vector(1, 2, 2)
    assert round((nx2 + ny2 + nz2), 5) == 1.0

def testdotproduct():
    assert dot_product(1, 0, 0, 1, 0, 0) == 1
    assert dot_product(1, 2, 3, 4, 5, 6) == 32
    assert dot_product(0, 0, 0, 1, 2, 3) == 0

def testcrossproduct():
    assert cross_product(1, 0, 0, 0, 1, 0) == (0, 0, 1)
    assert cross_product(0, 1, 0, 0, 0, 1) == (1, 0, 0)
    assert cross_product(1, 2, 3, 4, 5, 6) == (-3, 6, -3)

def test_midpoint():
    assert midpoint(0, 0, 0, 2, 2, 2) == (1.0, 1.0, 1.0)
    assert midpoint(1, 2, 3, 4, 5, 6) == (2.5, 3.5, 4.5)
python
def add_numbers(a, b):
    """Проста функція додавання."""
    return a + b

def vector_length(x, y, z):
    """Обчислює довжину 3D-вектора."""
    return (x2 + y2 + z2)  0.5

def distancebetweenpoints(x1, y1, z1, x2, y2, z2):
    """Обчислює відстань між двома точками у 3D."""
    return ((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)  0.5

def normalize_vector(x, y, z):
    """Повертає нормалізований 3D-вектор (довжина = 1)."""
    length = (x2 + y2 + z2)  0.5
    if length == 0:
        return (0, 0, 0)
    return (x/length, y/length, z/length)

def dot_product(x1, y1, z1, x2, y2, z2):
    """Обчислює скалярний добуток двох 3D-векторів."""
    return x1x2 + y1y2 + z1*z2

def cross_product(x1, y1, z1, x2, y2, z2):
    """Обчислює векторний (крос) добуток двох 3D-векторів."""
    return (
        y1z2 - z1y2,
        z1x2 - x1z2,
        x1y2 - y1x2
    )

def midpoint(x1, y1, z1, x2, y2, z2):
    """Обчислює середню точку між двома точками у 3D."""
    return ((x1 + x2)/2, (y1 + y2)/2, (z1 + z2)/2)
python
from src.main import (
    add_numbers,
    vector_length,
    distancebetweenpoints,
    normalize_vector,
    dot_product,
    cross_product,
    midpoint
)

def testaddnumbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def testvectorlength():
    assert vector_length(1, 0, 0) == 1
    assert vector_length(0, 3, 4) == 5
    assert round(vector_length(1, 2, 2), 5) == 3.0

def testdistancebetween_points():
    assert distancebetweenpoints(0, 0, 0, 1, 0, 0) == 1
    assert distancebetweenpoints(0, 0, 0, 0, 3, 4) == 5
    assert round(distancebetweenpoints(1, 2, 3, 4, 5, 6), 5) == 5.19615

def testnormalizevector():
    assert normalize_vector(1, 0, 0) == (1.0, 0.0, 0.0)
    assert normalize_vector(0, 3, 4) == (0.0, 0.6, 0.8)
    nx, ny, nz = normalize_vector(1, 2, 2)
    assert round((nx2 + ny2 + nz2), 5) == 1.0

def testdotproduct():
    assert dot_product(1, 0, 0, 1, 0, 0) == 1
    assert dot_product(1, 2, 3, 4, 5, 6) == 32
    assert dot_product(0, 0, 0, 1, 2, 3) == 0

def testcrossproduct():
    assert cross_product(1, 0, 0, 0, 1, 0) == (0, 0, 1)
    assert cross_product(0, 1, 0, 0, 0, 1) == (1, 0, 0)
    assert cross_product(1, 2, 3, 4, 5, 6) == (-3, 6, -3)

def test_midpoint():
    assert midpoint(0, 0, 0, 2, 2, 2) == (1.0, 1.0, 1.0)
    assert midpoint(1, 2, 3, 4, 5, 6) == (2.5, 3.5, 4.5)
python
import math

def add_numbers(a, b):
    return a + b

def vector_length(x, y, z):
    return (x2 + y2 + z2)  0.5

def distancebetweenpoints(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1)2 + (y2 - y1)2 + (z2 - z1)2)  0.5

def normalize_vector(x, y, z):
    length = vector_length(x, y, z)
    if length == 0:
        return (0, 0, 0)
    return (x/length, y/length, z/length)

def dot_product(x1, y1, z1, x2, y2, z2):
    return x1x2 + y1y2 + z1*z2

def cross_product(x1, y1, z1, x2, y2, z2):
    return (y1z2 - z1y2, z1x2 - x1z2, x1y2 - y1x2)

def midpoint(x1, y1, z1, x2, y2, z2):
    return ((x1 + x2)/2, (y1 + y2)/2, (z1 + z2)/2)

def translate_point(x, y, z, dx, dy, dz):
    """Перенос точки у 3D."""
    return (x + dx, y + dy, z + dz)

def scale_point(x, y, z, sx, sy, sz):
    """Масштабування точки у 3D."""
    return (x  sx, y  sy, z * sz)

def rotatepointx(x, y, z, angle):
    """Обертання точки навколо осі X."""
    rad = math.radians(angle)
    return (x, ymath.cos(rad) - zmath.sin(rad), ymath.sin(rad) + zmath.cos(rad))

def rotatepointy(x, y, z, angle):
    """Обертання точки навколо осі Y."""
    rad = math.radians(angle)
    return (xmath.cos(rad) + zmath.sin(rad), y, -xmath.sin(rad) + zmath.cos(rad))

def rotatepointz(x, y, z, angle):
    """Обертання точки навколо осі Z."""
    rad = math.radians(angle)
    return (xmath.cos(rad) - ymath.sin(rad), xmath.sin(rad) + ymath.cos(rad), z)
python
from src.main import (
    addnumbers, vectorlength, distancebetweenpoints,
    normalizevector, dotproduct, cross_product, midpoint,
    translatepoint, scalepoint,
    rotatepointx, rotatepointy, rotatepointz
)

def testaddnumbers():
    assert add_numbers(2, 3) == 5

def testvectorlength():
    assert vector_length(0, 3, 4) == 5

def testdistancebetween_points():
    assert distancebetweenpoints(0, 0, 0, 0, 3, 4) == 5

def testnormalizevector():
    assert normalize_vector(0, 3, 4) == (0.0, 0.6, 0.8)

def testdotproduct():
    assert dot_product(1, 2, 3, 4, 5, 6) == 32

def testcrossproduct():
    assert cross_product(1, 0, 0, 0, 1, 0) == (0, 0, 1)

def test_midpoint():
    assert midpoint(0, 0, 0, 2, 2, 2) == (1.0, 1.0, 1.0)

def testtranslatepoint():
    assert translate_point(1, 2, 3, 1, 1, 1) == (2, 3, 4)

def testscalepoint():
    assert scale_point(1, 2, 3, 2, 2, 2) == (2, 4, 6)

def testrotatepoint_x():
    rx = rotatepointx(0, 1, 0, 90)
    assert round(rx[1], 5) == 0.0 and round(rx[2], 5) == 1.0

def testrotatepoint_y():
    ry = rotatepointy(1, 0, 0, 90)
    assert round(ry[0], 5) == 0.0 and round(ry[2], 5) == -1.0

def testrotatepoint_z():
    rz = rotatepointz(1, 0, 0, 90)
    assert round(rz[0], 5) == 0.0 and round(rz[1], 5) == 1.0
markdown

Можливості бібліотеки

Ця бібліотека містить набір базових 3D‑математичних функцій:

- Арифметика
  - add_numbers(a, b) — проста функція додавання

- Вектори
  - vector_length(x, y, z) — довжина 3D‑вектора
  - normalize_vector(x, y, z) — нормалізація вектора (довжина = 1)
  - dot_product(x1, y1, z1, x2, y2, z2) — скалярний добуток
  - cross_product(x1, y1, z1, x2, y2, z2) — векторний добуток

- Геометрія
  - distancebetweenpoints(x1, y1, z1, x2, y2, z2) — відстань між точками
  - midpoint(x1, y1, z1, x2, y2, z2) — середня точка

- Перетворення точок
  - translate_point(x, y, z, dx, dy, dz) — перенесення
  - scale_point(x, y, z, sx, sy, sz) — масштабування
  - rotatepointx(x, y, z, angle) — обертання навколо осі X
  - rotatepointy(x, y, z, angle) — обертання навколо осі Y
  - rotatepointz(x, y, z, angle) — обертання навколо осі Z

- Матриці трансформацій (4×4)
  - identity_matrix() — одинична матриця
  - translation_matrix(dx, dy, dz) — матриця переносу
  - scaling_matrix(sx, sy, sz) — матриця масштабування
  - rotationmatrixx(angle) — матриця обертання навколо X
  - rotationmatrixy(angle) — матриця обертання навколо Y
  - rotationmatrixz(angle) — матриця обертання навколо Z
python
from src.main import (
    vectorlength, normalizevector, dot_product,
    crossproduct, midpoint, translatepoint,
    scalepoint, rotatepoint_x
)

Довжина вектора
length = vector_length(1, 2, 2)  # → 3.0

Нормалізація
nx, ny, nz = normalize_vector(0, 3, 4)  # → (0.0, 0.6, 0.8)

Скалярний добуток
dp = dot_product(1, 2, 3, 4, 5, 6)  # → 32

Векторний добуток
cp = cross_product(1, 0, 0, 0, 1, 0)  # → (0, 0, 1)

Середня точка
mid = midpoint(0, 0, 0, 2, 2, 2)  # → (1.0, 1.0, 1.0)

Перенесення точки
moved = translate_point(1, 2, 3, 1, 1, 1)  # → (2, 3, 4)

Масштабування
scaled = scale_point(1, 2, 3, 2, 2, 2)  # → (2, 4, 6)

Обертання навколо X
rotated = rotatepointx(0, 1, 0, 90)  # → (0, 0.0, 1.0)
python
from src.main import (
    addnumbers, vectorlength, distancebetweenpoints,
    normalizevector, dotproduct, cross_product, midpoint,
    translatepoint, scalepoint,
    rotatepointx, rotatepointy, rotatepointz
)
from src.matrix import (
    identitymatrix, translationmatrix, scaling_matrix,
    rotationmatrixx, rotationmatrixy, rotationmatrixz
)

def main():
    print("=== Арифметика ===")
    print("2 + 3 =", add_numbers(2, 3))

    print("\n=== Вектори ===")
    print("Довжина (1,2,2):", vector_length(1, 2, 2))
    print("Нормалізація (0,3,4):", normalize_vector(0, 3, 4))
    print("Dot product (1,2,3)·(4,5,6):", dot_product(1, 2, 3, 4, 5, 6))
    print("Cross product (1,0,0)×(0,1,0):", cross_product(1, 0, 0, 0, 1, 0))

    print("\n=== Геометрія ===")
    print("Відстань між (0,0,0) і (0,3,4):", distancebetweenpoints(0, 0, 0, 0, 3, 4))
    print("Середня точка між (0,0,0) і (2,2,2):", midpoint(0, 0, 0, 2, 2, 2))

    print("\n=== Перетворення точок ===")
    print("Перенесення (1,2,3) на (1,1,1):", translate_point(1, 2, 3, 1, 1, 1))
    print("Масштабування (1,2,3) × (2,2,2):", scale_point(1, 2, 3, 2, 2, 2))
    print("Обертання (0,1,0) навколо X на 90°:", rotatepointx(0, 1, 0, 90))
    print("Обертання (1,0,0) навколо Y на 90°:", rotatepointy(1, 0, 0, 90))
    print("Обертання (1,0,0) навколо Z на 90°:", rotatepointz(1, 0, 0, 90))

    print("\n=== Матриці трансформацій ===")
    print("Одинична матриця:", identity_matrix())
    print("Матриця переносу (1,2,3):", translation_matrix(1, 2, 3))
    print("Матриця масштабування (2,3,4):", scaling_matrix(2, 3, 4))
    print("Матриця обертання X (90°):", rotationmatrixx(90))
    print("Матриця обертання Y (90°):", rotationmatrixy(90))
    print("Матриця обертання Z (90°):", rotationmatrixz(90))

if name == "main":
    main()
python
def applymatrixto_point(matrix, x, y, z):
    """Застосовує матрицю 4×4 до точки (x, y, z)."""
    # Перетворюємо точку у вектор-стовпець (x, y, z, 1)
    point = [x, y, z, 1]
    result = [0, 0, 0, 0]

    for i in range(4):
        for j in range(4):
            result[i] += matrix[i][j] * point[j]

    # Повертаємо тільки перші три координати (x, y, z)
    return (result[0], result[1], result[2])
python
from src.matrix import (
    identitymatrix, translationmatrix, scaling_matrix,
    applymatrixto_point
)

def testapplymatrix_identity():
    m = identity_matrix()
    p = applymatrixto_point(m, 1, 2, 3)
    assert p == (1, 2, 3)

def testapplymatrix_translation():
    m = translation_matrix(1, 2, 3)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (2, 3, 4)

def testapplymatrix_scaling():
    m = scaling_matrix(2, 3, 4)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (2, 3, 4)
python
def multiply_matrices(a, b):
    """Множення двох матриць 4×4."""
    result = [[0 for  in range(4)] for  in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += a[i][k] * b[k][j]
    return result
python
from src.matrix import (
    identitymatrix, translationmatrix, scaling_matrix,
    multiplymatrices, applymatrixtopoint
)

def testmultiplyidentity():
    a = identity_matrix()
    b = translation_matrix(1, 2, 3)
    m = multiply_matrices(a, b)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (2, 3, 4)

def testmultiplyscaling_translation():
    s = scaling_matrix(2, 2, 2)
    t = translation_matrix(1, 1, 1)
    m = multiply_matrices(s, t)
    p = applymatrixto_point(m, 1, 1, 1)
    # Спочатку масштабування (2,2,2), потім перенесення (+1,+1,+1)
    assert p == (3, 3, 3)
python
def lookatmatrix(eye, target, up):
    """View-матриця: камера дивиться з eye на target."""
    import numpy as np

    eye = np.array(eye)
    target = np.array(target)
    up = np.array(up)

    zaxis = (eye - target)
    zaxis = zaxis / np.linalg.norm(zaxis)

    xaxis = np.cross(up, zaxis)
    xaxis = xaxis / np.linalg.norm(xaxis)

    yaxis = np.cross(zaxis, xaxis)

    tx = -np.dot(xaxis, eye)
    ty = -np.dot(yaxis, eye)
    tz = -np.dot(zaxis, eye)

    return [
        [xaxis[0], xaxis[1], xaxis[2], tx],
        [yaxis[0], yaxis[1], yaxis[2], ty],
        [zaxis[0], zaxis[1], zaxis[2], tz],
        [0,        0,        0,        1]
    ]

def perspective_matrix(fov, aspect, near, far):
    """Projection-матриця: перспектива."""
    import math
    f = 1 / math.tan(math.radians(fov) / 2)
    nf = 1 / (near - far)

    return [
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near)  nf, 2  far  near  nf],
        [0, 0, -1, 0]
    ]
python
from src.matrix import lookatmatrix, perspective_matrix

def testlookat_matrix():
    m = lookatmatrix([0, 0, 5], [0, 0, 0], [0, 1, 0])
    assert round(m[2][2], 5) == 1.0  # камера дивиться вздовж Z

def testperspectivematrix():
    m = perspective_matrix(90, 1.0, 1.0, 10.0)
    assert round(m[0][0], 5) > 1.0
    assert m[3][2] == -1
python
def transformpointviewprojection(point, viewmatrix, projection_matrix):
    """Перетворює точку через view + projection."""
    vpmatrix = multiplymatrices(projectionmatrix, viewmatrix)
    return applymatrixtopoint(vpmatrix, *point)
python
from src.matrix import (
    lookatmatrix, perspective_matrix,
    transformpointview_projection
)

def testtransformpointviewprojection():
    eye = [0, 0, 5]
    target = [0, 0, 0]
    up = [0, 1, 0]
    view = lookatmatrix(eye, target, up)
    proj = perspective_matrix(90, 1.0, 1.0, 10.0)
    p = transformpointview_projection([0, 0, 0], view, proj)
    # Точка (0,0,0) має бути попереду камери, отже z < 0
    assert p[2] < 0
python
def applymatrixto_point(matrix, x, y, z):
    """Застосовує матрицю 4×4 до точки (x, y, z)."""
    point = [x, y, z, 1]
    result = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            result[i] += matrix[i][j] * point[j]
    return (result[0], result[1], result[2])

def multiply_matrices(a, b):
    """Множення двох матриць 4×4."""
    result = [[0 for  in range(4)] for  in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += a[i][k] * b[k][j]
    return result

def lookatmatrix(eye, target, up):
    """View-матриця: камера дивиться з eye на target."""
    import numpy as np
    eye, target, up = map(np.array, (eye, target, up))
    zaxis = (eye - target) / np.linalg.norm(eye - target)
    xaxis = np.cross(up, zaxis) / np.linalg.norm(np.cross(up, zaxis))
    yaxis = np.cross(zaxis, xaxis)
    tx, ty, tz = -np.dot(xaxis, eye), -np.dot(yaxis, eye), -np.dot(zaxis, eye)
    return [
        [xaxis[0], xaxis[1], xaxis[2], tx],
        [yaxis[0], yaxis[1], yaxis[2], ty],
        [zaxis[0], zaxis[1], zaxis[2], tz],
        [0, 0, 0, 1]
    ]

def perspective_matrix(fov, aspect, near, far):
    """Projection-матриця: перспектива."""
    import math
    f = 1 / math.tan(math.radians(fov) / 2)
    nf = 1 / (near - far)
    return [
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near)  nf, 2  far  near  nf],
        [0, 0, -1, 0]
    ]

def transformpointviewprojection(point, viewmatrix, projection_matrix):
    """Перетворює точку через view + projection."""
    vpmatrix = multiplymatrices(projectionmatrix, viewmatrix)
    return applymatrixtopoint(vpmatrix, *point)
python
from src.matrix import (
    identitymatrix, translationmatrix, scaling_matrix,
    applymatrixtopoint, multiplymatrices,
    lookatmatrix, perspective_matrix,
    transformpointview_projection
)

def testapplymatrix_identity():
    m = identity_matrix()
    p = applymatrixto_point(m, 1, 2, 3)
    assert p == (1, 2, 3)

def testapplymatrix_translation():
    m = translation_matrix(1, 2, 3)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (2, 3, 4)

def testapplymatrix_scaling():
    m = scaling_matrix(2, 3, 4)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (2, 3, 4)

def testmultiplyidentity():
    a = identity_matrix()
    b = translation_matrix(1, 2, 3)
    m = multiply_matrices(a, b)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (2, 3, 4)

def testmultiplyscaling_translation():
    s = scaling_matrix(2, 2, 2)
    t = translation_matrix(1, 1, 1)
    m = multiply_matrices(s, t)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (3, 3, 3)

def testlookat_matrix():
    m = lookatmatrix([0, 0, 5], [0, 0, 0], [0, 1, 0])
    assert round(m[2][2], 5) == 1.0

def testperspectivematrix():
    m = perspective_matrix(90, 1.0, 1.0, 10.0)
    assert round(m[0][0], 5) > 1.0
    assert m[3][2] == -1

def testtransformpointviewprojection():
    eye, target, up = [0, 0, 5], [0, 0, 0], [0, 1, 0]
    view = lookatmatrix(eye, target, up)
    proj = perspective_matrix(90, 1.0, 1.0, 10.0)
    p = transformpointview_projection([0, 0, 0], view, proj)
    assert p[2] < 0
1. Світова координата  
   → точка у глобальному просторі: (x, y, z)

2. View‑матриця  
   → lookatmatrix(eye, target, up)  
   → перетворює світову точку у координати камери

3. Projection‑матриця  
   → perspective_matrix(fov, aspect, near, far)  
   → додає перспективу: ближче — більше, далі — менше

4. Композиція  
   → multiply_matrices(projection, view)  
   → об’єднує обидві матриці в одну

5. Застосування  
   → applymatrixto_point(matrix, x, y, z)  
   → повертає точку у вигляді, готовому для рендерингу

6. Фінальне перетворення  
   → transformpointview_projection(point, view, projection)  
   → одна функція, яка виконує весь шлях
1. Кодова база
   - [x] Усі функції реалізовані (applymatrixtopoint, multiplymatrices, lookatmatrix, perspectivematrix, transformpointviewprojection)
   - [x] Тести покривають кожну функцію
   - [x] example.py демонструє всі можливості
2. Документація
- [x] README.md містить:
  - “Можливості бібліотеки”
  - “Приклади використання”
  - “Архітектура трансформацій”
- [x] Код‑сніпети перевірені й працюють
toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "vector-math-lib"
version = "1.0.0"
description = "Бібліотека для роботи з векторами, точками та матрицями трансформацій у 3D"
readme = "README.md"
license = {text = "MIT"}
authors = [
    {name = "Твоє ім’я", email = "you@example.com"}
]
dependencies = [
    "numpy>=1.24",
]

[tool.setuptools.packages.find]
where = ["src"]
3. CI/CD
- [x] Налаштований GitHub Actions для запуску pytest
- [x] Усі тести проходять успішно

4. Пакування
- [ ] Додати pyproject.toml або setup.py для встановлення через pip
- [ ] Вказати залежності (numpy, pytest)

5. Реліз
- [ ] Створити тег (v1.0.0)
- [ ] Згенерувати GitHub Release
- [ ] (Опціонально) Завантажити на PyPI
toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "vector-math-lib"
version = "1.0.0"
description = "Бібліотека для роботи з векторами, точками та матрицями трансформацій у 3D"
readme = "README.md"
license = {text = "MIT"}
authors = [
    {name = "Твоє ім’я", email = "you@example.com"}
]
dependencies = [
    "numpy>=1.24",
]

[tool.setuptools.packages.find]
where = ["src"]
bash
pip install 
python
def applymatrixto_point(matrix, x, y, z):
    """Застосовує матрицю 4×4 до точки (x, y, z)."""
    point = [x, y, z, 1]
    result = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            result[i] += matrix[i][j] * point[j]
    return (result[0], result[1], result[2])

def multiply_matrices(a, b):
    """Множення двох матриць 4×4."""
    result = [[0 for  in range(4)] for  in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += a[i][k] * b[k][j]
    return result

def lookatmatrix(eye, target, up):
    """View-матриця: камера дивиться з eye на target."""
    import numpy as np
    eye, target, up = map(np.array, (eye, target, up))
    zaxis = (eye - target) / np.linalg.norm(eye - target)
    xaxis = np.cross(up, zaxis) / np.linalg.norm(np.cross(up, zaxis))
    yaxis = np.cross(zaxis, xaxis)
    tx, ty, tz = -np.dot(xaxis, eye), -np.dot(yaxis, eye), -np.dot(zaxis, eye)
    return [
        [xaxis[0], xaxis[1], xaxis[2], tx],
        [yaxis[0], yaxis[1], yaxis[2], ty],
        [zaxis[0], zaxis[1], zaxis[2], tz],
        [0, 0, 0, 1]
    ]

def perspective_matrix(fov, aspect, near, far):
    """Projection-матриця: перспектива."""
    import math
    f = 1 / math.tan(math.radians(fov) / 2)
    nf = 1 / (near - far)
    return [
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near)  nf, 2  far  near  nf],
        [0, 0, -1, 0]
    ]

def transformpointviewprojection(point, viewmatrix, projection_matrix):
    """Перетворює точку через view + projection."""
    vpmatrix = multiplymatrices(projectionmatrix, viewmatrix)
    return applymatrixtopoint(vpmatrix, *point)
python
from src.matrix import (
    identitymatrix, translationmatrix, scaling_matrix,
    applymatrixtopoint, multiplymatrices,
    lookatmatrix, perspective_matrix,
    transformpointview_projection
)

def testapplymatrix_identity():
    m = identity_matrix()
    p = applymatrixto_point(m, 1, 2, 3)
    assert p == (1, 2, 3)

def testapplymatrix_translation():
    m = translation_matrix(1, 2, 3)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (2, 3, 4)

def testapplymatrix_scaling():
    m = scaling_matrix(2, 3, 4)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (2, 3, 4)

def testmultiplyidentity():
    a = identity_matrix()
    b = translation_matrix(1, 2, 3)
    m = multiply_matrices(a, b)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (2, 3, 4)

def testmultiplyscaling_translation():
    s = scaling_matrix(2, 2, 2)
    t = translation_matrix(1, 1, 1)
    m = multiply_matrices(s, t)
    p = applymatrixto_point(m, 1, 1, 1)
    assert p == (3, 3, 3)

def testlookat_matrix():
    m = lookatmatrix([0, 0, 5], [0, 0, 0], [0, 1, 0])
    assert round(m[2][2], 5) == 1.0

def testperspectivematrix():
    m = perspective_matrix(90, 1.0, 1.0, 10.0)
    assert round(m[0][0], 5) > 1.0
    assert m[3][2] == -1

def testtransformpointviewprojection():
    eye, target, up = [0, 0, 5], [0, 0, 0], [0, 1, 0]
    view = lookatmatrix(eye, target, up)
    proj = perspective_matrix(90, 1.0, 1.0, 10.0)
    p = transformpointview_projection([0, 0, 0], view, proj)
    assert p[2] < 0
markdown

🧠 Архітектура трансформацій

Бібліотека реалізує повний шлях перетворення точки у 3D‑просторі:

1. Світова координата  
   → точка у глобальному просторі: (x, y, z)

2. View‑матриця  
   → lookatmatrix(eye, target, up)  
   → перетворює світову точку у координати камери

3. Projection‑матриця  
   → perspective_matrix(fov, aspect, near, far)  
   → додає перспективу: ближче — більше, далі — менше

4. Композиція  
   → multiply_matrices(projection, view)  
   → об’єднує обидві матриці в одну

5. Застосування  
   → applymatrixto_point(matrix, x, y, z)  
   → повертає точку у вигляді, готовому для рендерингу

6. Фінальне перетворення  
   → transformpointview_projection(point, view, projection)  
   → одна функція, яка виконує весь шлях
yaml
name: Python package tests

on:
  push:
    branches: [ "" ]
  pull_request:
    branches: [ "" ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .
        pip install pytest

    - name: Run tests
      run: pytest
