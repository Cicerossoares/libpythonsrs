from unittest.mock import Mock

import pytest as pytest

from libpythonsrs.spam.enviador_email import Enviador
from libpythonsrs.spam.main import EnviadorDeSpam
from libpythonsrs.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Cicero', email='ozctkz@gmail.com'),
            Usuario(nome='Junior', email='ozctkz@gmail.com')
        ],
        [
            Usuario(nome='Cicero', email='ozctkz@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ozctkz@gmail.com',
        'Testando',
        'testando'
    )
    assert len(usuarios) == enviador.enviar.call_count


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Cicero', email='ozctkz@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'cjgatao@gmail.com',
        'Testando',
        'testando'
    )
    enviador.enviar.assert_called_once_with(
        'cjgatao@gmail.com',
        'ozctkz@gmail.com',
        'Testando',
        'testando'
    )