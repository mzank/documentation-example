import sys
import os
from pytest import approx

sys.path.append(os.path.abspath("src"))

from multiply import multiply

def test_multiply():
  assert multiply(3.0, 6.0) == approx(18.0)
  assert multiply(-2.4, 3.5) == approx(-8.4)
  assert multiply(5.6, -2.8) == approx(-15.68)
  
