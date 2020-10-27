#!/usr/bin/env python3
import pytest
import roots

# Tests are from lecture in the order they were presented in
def test_quadroots_result():
    assert roots.quad_roots(1.0, 1.0, -12.0) == ((3+0j), (-4+0j))

test_quadroots_result()

def test_quadroots_types():
    with pytest.raises(TypeError):
        roots.quad_roots("saul", "elephante", ["hi", "correct", "list", "connotation"])

test_quadroots_types()

def test_quadroots_zerocoeff():
    with pytest.raises(ValueError):
        roots.quad_roots(a=0.0)

test_quadroots_zerocoeff()

def test_linroots_result():
    assert roots.linear_roots(6.0, -12.0) == 2

test_linroots_result()

def test_linroots_types():
    with pytest.raises(TypeError):
        roots.linear_roots("o", 9.0)

test_linroots_types()

def test_linroots_zerocoeff():
    with pytest.raises(ValueError):
        roots.linear_roots(0.0, 10000.0)

test_linroots_zerocoeff()
