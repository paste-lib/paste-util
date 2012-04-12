import types


class _ContentType(object):
    class Type:
        HTML = 0
        XHTML = 1
        CE_HTML = 2  # See http://en.wikipedia.org/wiki/CE-HTML
        JAVASCRIPT = 3
        CSS = 4
        TEXT = 5
        XML = 6
        PNG = 7
        GIF = 8
        JPEG = 9
        SWF = 10
        WEBP = 11
        HTC = 12 # HTML Component. See http://en.wikipedia.org/wiki/HTML_Components
        SVG = 13
        EOT = 14
        TTF = 15
        WOFF = 16
        OTF = 17
        ICO = 18

    def __init__(self, mime_type, file_extension, content_type):
        super(_ContentType, self).__init__()
        self.type = content_type
        self.mime_type = mime_type
        self.file_extension = file_extension

    @property
    def is_flash(self):
        return self.type == _ContentType.Type.SWF

    @property
    def is_image(self):
        return self.type == _ContentType.Type.PNG or self.type == _ContentType.Type.GIF or self.type == _ContentType.Type.JPEG or self.type == _ContentType.Type.WEBP or self.type == _ContentType.Type.ICO

    @property
    def is_html_like(self):
        return self.type == _ContentType.Type.HTML or self.type == _ContentType.Type.HTML or self.type == _ContentType.Type.CE_HTML

    @property
    def is_xml_like(self):
        return self.type == _ContentType.Type.XHTML or self.type == _ContentType.Type.XML

    @property
    def is_font(self):
        return self.type == _ContentType.Type.EOT or self.type == _ContentType.Type.TTF or self.type == _ContentType.Type.WOFF or self.type == _ContentType.Type.OTF

_content_types = (
    _ContentType('text/html', '.html', _ContentType.Type.HTML), # RFC 2854
    _ContentType('application/xhtml+xml', '.xhtml', _ContentType.Type.XHTML), # RFC 3236
    _ContentType('application/ce-html+xml', '.xhtml', _ContentType.Type.CE_HTML),

    _ContentType('text/javascript', '.js', _ContentType.Type.JAVASCRIPT),
    _ContentType('text/css', '.css', _ContentType.Type.CSS),
    _ContentType('text/css', '.scss', _ContentType.Type.CSS),
    _ContentType('text/plain', '.txt', _ContentType.Type.TEXT),
    _ContentType('text/xml', '.xml', _ContentType.Type.XML), # RFC 3023

    _ContentType('image/png', '.png', _ContentType.Type.PNG),
    _ContentType('image/gif', '.gif', _ContentType.Type.GIF),
    _ContentType('image/jpeg', '.jpg', _ContentType.Type.JPEG),
    _ContentType('image/x-icon', '.ico',  _ContentType.Type.ICO),

    # Synonyms; Note that the canonical types are referenced by index  in the named references declared below.
    _ContentType('application/x-javascript', '.js', _ContentType.Type.JAVASCRIPT),
    _ContentType('application/javascript', '.js', _ContentType.Type.JAVASCRIPT),
    _ContentType('text/ecmascript', '.js', _ContentType.Type.JAVASCRIPT),
    _ContentType('application/ecmascript', '.js', _ContentType.Type.JAVASCRIPT),
    _ContentType('image/jpeg', '.jpeg', _ContentType.Type.JPEG),
    _ContentType('text/html', '.htm', _ContentType.Type.HTML),
    _ContentType('application/xml', '.xml', _ContentType.Type.XML), # RFC 3023

    _ContentType('image/svg+xml', '.svg',  _ContentType.Type.SVG),
    _ContentType('application/vnd.ms-fontobject', '.eot',  _ContentType.Type.EOT),
    _ContentType('application/x-font-ttf', '.ttf',  _ContentType.Type.TTF),
    _ContentType('application/x-font-woff', '.woff', _ContentType.Type.WOFF),
    _ContentType('application/x-font-otf', '.otf',  _ContentType.Type.OTF)
    )


class ContentTypeHelper(object):
    types = _content_types

    HTML = _content_types[0]
    XHTML = _content_types[1]
    CE_HTML = _content_types[2]

    JAVASCRIPT = _content_types[3]
    CSS = _content_types[4]
    SCSS = _content_types[5]
    TEXT = _content_types[6]
    XML = _content_types[7]

    PNG = _content_types[8]
    GIF = _content_types[9]
    JPEG = _content_types[10]

    @classmethod
    def type_to_content_type(cls, type_int):
        """

        :param type_int:
        :return:
        """
        return next((content_type for content_type in _content_types if content_type.type == type_int), None)

    @classmethod
    def filename_to_content_type(cls, filename):
        """

        :param filename:
        :return:
        """
        result = None

        if not isinstance(filename, types.StringTypes):
            return result

        extension_position = filename.rfind('.')
        if extension_position != -1:
            extension = filename[extension_position:]
            result = next((t for t in _content_types if t.file_extension == extension), None)

        return result

    @classmethod
    def mime_type_to_content_type(cls, mime_type):
        """

        :param mime_type:
        :return:
        """
        semi_colon = mime_type.find(';')
        if semi_colon == -1:
            mime_type = mime_type
        else:
            mime_type = mime_type[:semi_colon]

        return next((t for t in _content_types if t.mime_type == mime_type), None)

