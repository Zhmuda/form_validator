from flask import Flask, request, jsonify
from app.database import get_templates
from app.utils import validate_field, determine_field_type

app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form.to_dict()
    templates = get_templates()
    
    for template in templates:
        if all(
            field in data and validate_field(data[field], template[field])
            for field in template if field != "name"
        ):
            return jsonify({"template_name": template["name"]})
    
    response = {
        field: determine_field_type(value)
        for field, value in data.items()
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
