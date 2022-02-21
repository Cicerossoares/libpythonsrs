import pytest

from libpythonsrs.spam.enviador_email import Enviador, EmailInvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['ozctkz@gmail.com', 'cjgatao02@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'cjgatao@gmail.com',
        'teste do enviador',
        'Voce conseguiu Cicero'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','cjgatao02']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'cjgatao@gmail.com',
            'teste do enviador',
            'Voce conseguiu Cicero'
        )