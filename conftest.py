# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

# инициализация фикстуры
@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture