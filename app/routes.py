import io
import base64
from flask import Blueprint, request, send_file, jsonify
import qrcode
from PIL import Image

bp = Blueprint('api', __name__)

@bp.route('/generate', methods=['POST'])
def generate_qr():
    data = request.get_json() or {}
    url = data.get('url')
    fill = data.get('fill', '#000000')
    if not url:
        return jsonify({'error': 'url required'}), 400
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color='white').convert('RGB')
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')
