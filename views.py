from os import error, replace
from utils import add_data, delete_data, update_data, get_all_data, load_template, build_response
import urllib
from database import Database, Note

def index(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados

        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            params[chave_valor.split('=')[0]] = urllib.parse.unquote_plus(chave_valor.split('=')[1])
        add_data(params,'banco' )

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content)
        for dados in get_all_data('banco')
    ]
    notes = '\n'.join(notes_li)
    if request.startswith('POST'):
        return build_response(code=303, reason='See Other', headers='Location: /') + load_template('index.html').format(notes=notes).encode()
    else:
        return build_response() + load_template('index.html').format(notes=notes).encode()