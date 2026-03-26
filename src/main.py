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
