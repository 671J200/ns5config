## Credit to http://rhoit.com/bio, https://gist.github.com/rhoit/9573c40feaeb3cf44b4a8544dc0ae2a1
import uuid
import os
import mimetypes

def multipart_encoder(params, files):
    boundary = uuid.uuid4().hex
    lines = list()
    for key, val in params.items():
        if val is None: continue
        lines.append('--' + boundary)
        lines.append('Content-Disposition: form-data; name="%s"'%key)
        lines.extend([ '', val ])

    for key, uri in files.items():
        name = os.path.basename(uri)
        mime = mimetypes.guess_type(uri)[0] or 'application/octet-stream'

        lines.append('--' + boundary)
        lines.append('Content-Disposition: form-data; name="{0}"; filename="{1}"'.format(key, name))
        lines.append('Content-Type: ' + mime)
        lines.append('')
        lines.append(open(uri, 'rb').read())

    lines.append('--%s--'%boundary)

    body = bytes()
    for l in lines:
        if isinstance(l, bytes): body += l + b'\r\n'
        else: body += bytes(l, encoding='utf8') + b'\r\n'

    headers = {
        'Content-Type' : 'multipart/form-data; boundary=' + boundary,
    }

    return headers, body
