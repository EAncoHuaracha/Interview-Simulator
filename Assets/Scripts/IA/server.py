from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configura la clave de API
genai.configure(api_key="AIzaSyB1W9LDBa1W2sBygY4vlLd8_XC2wT3H-7g")  

# Inicializa el modelo
model = genai.GenerativeModel("gemini-1.5-flash")

predefined_questions = {
    "¿Qué es lo más importante para un desarrollador de software?": "Para un desarrollador de software, lo más importante es entender los requisitos del usuario, escribir código limpio y mantenible, y garantizar que el software sea robusto y eficiente.",
    "¿Cómo manejas los problemas difíciles en el desarrollo de software?": "Manejo los problemas difíciles descomponiéndolos en partes más pequeñas, investigando y buscando soluciones en la documentación o en la comunidad, y pidiendo ayuda a colegas cuando es necesario.",
    "¿Qué técnicas usas para asegurarte de que el código sea de alta calidad?": "Utilizo técnicas como la revisión de código, pruebas unitarias, integración continua y seguimiento de buenas prácticas de codificación para asegurar la alta calidad del código.",
    "¿Cómo te mantienes actualizado con las nuevas tecnologías y tendencias en desarrollo de software?": "Me mantengo actualizado leyendo blogs técnicos, asistiendo a conferencias y talleres, y realizando cursos en línea para aprender sobre las últimas tecnologías y tendencias.",
    "¿Tienes alguna pregunta para mí o hay algo más que te gustaría discutir?": "Si tienes alguna pregunta específica sobre el puesto o la empresa, estaré encantado de responderla."
}

def filter_response_text(text, max_length=200):
    if len(text) > max_length:
        text = text[:max_length]
        last_period_index = text.rfind('.')
        last_space_index = text.rfind(' ')
        
        if last_period_index != -1 and last_period_index > (max_length * 0.8):
            text = text[:last_period_index + 1] 
        elif last_space_index != -1:
            text = text[:last_space_index] + '...'
        else:
            text = text + '...'
    return text

@app.route('/ask', methods=['POST'])
def ask():
    reply = model.generate_content("Quiero que simules ser un entrevistador para una empresa de desarrolladora de software y dame simepre preguntas y mensajes cortos que no sea mayor a 200 caracteres")

    if request.content_type == 'application/x-www-form-urlencoded':
        question = request.form.get('question', '')
    elif request.content_type == 'application/json':
        data = request.json
        question = data.get('question', '')
    else:
        return jsonify({'error': 'Unsupported Media Type'}), 415

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    try:
        # Verificar si la pregunta está en las predefinidas
        if question in predefined_questions:
            reply = predefined_questions[question]
        else:
            # Genera respuesta usando el modelo para preguntas no predefinidas
            response = model.generate_content(question)
            reply = response.text
            reply = filter_response_text(reply, max_length=200)

        # Devuelve la respuesta en formato JSON
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)





