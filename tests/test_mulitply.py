import sys
import os
from pytest import approx

sys.path.append(os.path.abspath("src"))

from multiply import multiply

def test_multiply():
  assert multiply(3.0, 6.0) = approx(18.0)
  
