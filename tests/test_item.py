from fastapi.testclient import TestClient


def test_find_all(client_fixture: TestClient):
    resp = client_fixture.get('/items')
    assert resp.status_code == 200

    items = resp.json()
    assert len(items) == 2


def test_find_by_id_ok(client_fixture: TestClient):
    resp = client_fixture.get('/items/1')
    assert resp.status_code == 200

    item = resp.json()
    assert item['id'] == 1


def test_find_by_id_not_found(client_fixture: TestClient):
    resp = client_fixture.get('/items/100')
    assert resp.status_code == 404
    assert resp.json()['detail'] == 'Item not found'


def test_find_by_name(client_fixture: TestClient):
    resp = client_fixture.get('/items/?name=PC1')
    assert resp.status_code == 200

    items = resp.json()
    assert len(items) == 1
    assert items[0]['name'] == 'PC1'


def test_create(client_fixture: TestClient):
    resp = client_fixture.post(
        '/items',
        json={
            'name': 'Smart Phone',
            'price': 30000,
            'user_id': 1
        }
    )
    assert resp.status_code == 201

    item = resp.json()
    assert item['id'] == 3
    assert item['name'] == 'Smart Phone'
    assert item['price'] == 30000

    resp = client_fixture.get('/items')
    assert len(resp.json()) == 3


def test_update_ok(client_fixture: TestClient):
    resp = client_fixture.put(
        '/items/1',
        json={
            'name': 'Smart Phone',
            'price': 50000
        }
    )
    assert resp.status_code == 200

    item = resp.json()
    assert item['name'] == 'Smart Phone'
    assert item['price'] == 50000


def test_update_not_found(client_fixture: TestClient):
    resp = client_fixture.put(
        '/items/100',
        json={
            'name': 'Smart Phone',
            'price': 50000
        }
    )
    assert resp.status_code == 404
    assert resp.json()['detail'] == 'Item not updated'


def test_delete_ok(client_fixture: TestClient):
    resp = client_fixture.delete('/items/1')
    assert resp.status_code == 200

    resp = client_fixture.get('/items')
    assert len(resp.json()) == 1


def test_delete_not_found(client_fixture: TestClient):
    resp = client_fixture.delete('/items/100')
    assert resp.status_code == 404
    assert resp.json()['detail'] == 'Item not deleted'
