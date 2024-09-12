import pytest
from rest_framework.test import APIClient
from app.models import Message
from django.contrib.auth.models import User
from model_bakery import baker

#фикстура клиента api (избегаем дублирование кода)
@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user('admin')

#model_bakery для создания данных в базе в автоматическом режим
# pip install model_bakery
@pytest.fixture
def message_factory():
    def factory(*args,**kwargs):
        return baker.make(Message,*args,**kwargs)
    return factory

@pytest.mark.django_db
def test_get_messages(client, user, message_factory):
    # Arrange (подготовка данных)
    #client = APIClient()
    #User.objects.create_user('admin')
    messages = message_factory(_quantity=10)
    #Message.objects.create(user_id=user.id,text='test')


    # Act (вызов методов, тестируемый функционал)
    response = client.get('/messages/')

    # Assert (проверка)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(messages)
    #assert data[0]['text'] == 'test'
    for i, m in enumerate(data):
       assert m['text']  == messages[i].text

@pytest.mark.django_db
def test_create_messages(client, user):
    count = Message.objects.count()
    #User.objects.create_user('admin')
    #response = client.post('/messages/', data={'user': user.id, 'text':'test text'}, format='json')
    response = client.post('/messages/', data={'user': user.id, 'text':'test text'})
    assert response.status_code == 201
    assert Message.objects.count() == count + 1

    


