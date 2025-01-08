from flask import Flask, render_template, abort
from pymongo import MongoClient
import base64

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['water_potability']
collection = db['model_plots']
metrics_collection = db['measurements_coll']

def get_model_metrics(model_name):
    """
    Retrieve metrics for a specific model from MongoDB.
    """
    try:
        metric = metrics_collection.find_one({"models": model_name})
        return metric if metric else {}
    except Exception as e:
        print(f"Error retrieving metrics for {model_name}: {str(e)}")
        return {}

def get_model_plots(model_name):
    """
    Retrieve plots for a specific model from MongoDB.
    Returns empty list if no plots are found.
    """
    try:
        plots = collection.find({"model": model_name})
        plot_data = []
        for plot in plots:
            if "name" in plot and "image" in plot:
                # Convert binary image data to base64 if needed
                if isinstance(plot["image"], bytes):
                    image_b64 = base64.b64encode(plot["image"]).decode('utf-8')
                else:
                    image_b64 = plot["image"]
                plot_data.append({
                    "name": plot["name"],
                    "image": image_b64
                })
        return plot_data
    except Exception as e:
        print(f"Error retrieving plots for {model_name}: {str(e)}")
        return []

# Route for main page
@app.route('/')
def index():
    # Fetch metrics for each model
    models = ["logistic_regression", "knn", "naive_bayes", "svm", "decision_tree", "random_forest"]
    accuracies = {}
    f1_score ={}
    for model in models:
        metrics = get_model_metrics(model)
        accuracies[model] = metrics.get("accuracy_score", "N/A")
    return render_template('page3.html', accuracies=accuracies)


# Routes for each model with unique URLs
@app.route('/logistic_regression')
def logistic_regression():
    plots = get_model_plots("logistic_regression")
    metrics = get_model_metrics("logistic_regression")
    return render_template('logistic_regression.html', plots=plots ,metrics=metrics)

@app.route('/knn')
def knn():
    plots = get_model_plots("knn")
    metrics = get_model_metrics("knn")
    return render_template('knn.html', plots=plots, metrics=metrics)

@app.route('/naive_bayes')
def naive_bayes():
    plots = get_model_plots("naive_bayes")
    metrics = get_model_metrics("naive_bayes")
    return render_template('naive_bayes.html', plots=plots , metrics=metrics)

@app.route('/svm')
def svm():
    plots = get_model_plots("svm")
    metrics = get_model_metrics("svm")
    metrics1 = get_model_metrics("better_svm")
    return render_template('svm.html', plots=plots ,metrics=metrics ,metrics1=metrics1)

@app.route('/decision_tree')
def decision_tree():
    plots = get_model_plots("decision_tree")
    metrics = get_model_metrics("decision_tree")
    return render_template('decision_tree.html', plots=plots ,metrics=metrics)

@app.route('/random_forest')
def random_forest():
    plots = get_model_plots("random_forest")
    metrics = get_model_metrics("random_forest")
    return render_template('random_forest.html', plots=plots,metrics=metrics)

@app.route('/model_comparison')
def model_comparison():
    plots = get_model_plots("model_comparison")
    return render_template('model_comparison.html', plots=plots)

if __name__ == "__main__":
    app.run(debug=True,port=5000)