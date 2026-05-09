import app as app_module

app = app_module.app
db = app_module.db
Mensaje = app_module.Mensaje

app.testing = True

def fake_stream(messages):
    class Chunk:
        def __init__(self, content):
            self.content = content

    yield Chunk("Hola, ")
    yield Chunk("esto es una prueba de streaming.")


if __name__ == '__main__':
    # Reemplazar el objeto llm por un stub que implemente stream()
    class FakeLLM:
        def stream(self, messages):
            return fake_stream(messages)

    app_module.llm = FakeLLM()

    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['user'] = 'demo'

        resp = client.post('/api/chat', json={'message': 'prueba de test'})
        print('STATUS:', resp.status_code)
        body = resp.get_data(as_text=True)
        print('BODY:', repr(body))

        # Verificar que se guardó el mensaje AI
        with app.app_context():
            last = Mensaje.query.filter_by(session_id='demo', role='ai').order_by(Mensaje.id.desc()).first()
            if last:
                print('LAST AI SAVED:', last.content)
            else:
                print('No se encontró mensaje AI en BD')
