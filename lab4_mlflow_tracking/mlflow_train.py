import mlflow
mlflow.set_experiment("mnist_experiment")
with mlflow.start_run():
    mlflow.log_param("epochs", 5)
    mlflow.log_metric("accuracy", 0.92)
    with open("model.txt", "w") as f:
        f.write("fake model")
    mlflow.log_artifact("model.txt")
