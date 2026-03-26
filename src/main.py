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
