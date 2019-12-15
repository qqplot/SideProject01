from app import app
from flask import session

app.config['TESTING'] = True

def test_index():
    with app.test_client() as web:
        rv = web.get('/', follow_redirects=True)
        assert rv.status_code == 200

        rv = web.get('/game', follow_redirects=True)
        assert rv.status_code == 200

        with web.session_transaction() as sess:
            assert sess['방_이름'] == '중앙_복도'
#    assert "이 폼을 채우세요" in rv.data.decode()

#    data = {'name': '제드', 'greet': 'Hello'}
#    rv = web.post('/hello', follow_redirects=True, data=data)
#    assert "제드" in rv.data.decode()
#    assert b"Hello" in rv.data
