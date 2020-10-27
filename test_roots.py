#!/usr/bin/env python3
import pytest
import roots

# Tests are from lecture in the order they were presented in
def test_quadroots_result():
    assert roots.quad_roots(1.0, 2.0, -12.0) == ((3+0j), (-4+0j))

def test_quadroots_types():
    with pytest.raises(TypeError):
        roots.quad_roots("saul", "elephante", ["hi", "correct", "list", "connotation"])

def test_quadroots_zerocoeff():
    with pytest.raises(ValueError):
        roots.quad_roots(a=0.0)

def test_linroots_result():
    assert roots.linear_roots(6.0, -12.0) == 2

def test_linroots_types():
    with pytest.raises(TypeError):
        roots.linear_roots("o", 9.0)

def test_linroots_zerocoeff():
    with pytest.raises(ValueError):
        roots.linear_roots(0.0, 10000.0)
