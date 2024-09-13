from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Duyarlılık analizi modelini yükle
classifier = pipeline("sentiment-analysis")

@app.route("/analyze_sentiment", methods=["POST"])
def analyze_sentiment():
    # Gelen isteği JSON formatına çevir ve yorumu al
    request_data = request.get_json()
    comment = request_data["comment"]

    # Yorumu analiz et
    result = classifier(comment)

    # Analiz sonucunu JSON olarak döndür
    return jsonify({"sentiment": result[0]['label']})

if __name__ == "__main__":
    app.run(debug=True)
