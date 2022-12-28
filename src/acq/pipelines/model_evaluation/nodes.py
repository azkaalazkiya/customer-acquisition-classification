"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.18.3
"""
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, f1_score, roc_auc_score, precision_score, roc_curve
import matplotlib.pyplot as plt
from kedro.extras.datasets.matplotlib import MatplotlibWriter
import seaborn as sns

def matrix_confusion(df:pd.DataFrame):
    cm = confusion_matrix(df['label'], df['prediction'])
    #plot confusion matrix
    plot = plt.figure(figsize=(6,6))
    sns.heatmap(cm, annot=True, fmt='.1f', 
                xticklabels =['acq','not acq'],
                yticklabels =['acq','not acq'])
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.title("Confusion Matrix")
    plt.show()
    single_plot_writer = MatplotlibWriter(
      filepath="data/08_reporting/matrix_confusion.png"
    )
    single_plot_writer.save(plot)

def plot_training(df1:pd.DataFrame):
    auc = roc_auc_score(df1['label'], df1['probability'])
    fpr, tpr, thresholds = roc_curve(df1['label'], df1['probability'])
    plot = plt.figure(figsize=(12, 7))
    plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
    plt.plot([0, 1], [0, 1], color='blue', linestyle='--', label='Baseline')
    plt.title('ROC Curve Training', size=20)
    plt.xlabel('False Positive Rate', size=14)
    plt.ylabel('True Positive Rate', size=14)
    plt.legend()
    plt.show()
    single_plot_writer = MatplotlibWriter(
      filepath="data/08_reporting/plot_training.png"
    )
    single_plot_writer.save(plot)

def plot_testing(df1:pd.DataFrame):
    auc = roc_auc_score(df1['label'], df1['probability'])
    fpr, tpr, thresholds = roc_curve(df1['label'], df1['probability'])
    plot = plt.figure(figsize=(12, 7))
    plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
    plt.plot([0, 1], [0, 1], color='blue', linestyle='--', label='Baseline')
    plt.title('ROC Curve Testing', size=20)
    plt.xlabel('False Positive Rate', size=14)
    plt.ylabel('True Positive Rate', size=14)
    plt.legend()
    plt.show()
    single_plot_writer = MatplotlibWriter(
      filepath="data/08_reporting/plot_testing.png"
    )
    single_plot_writer.save(plot)

def score(training:pd.DataFrame, testing:pd.DataFrame):
    akurasi = "Akurasi: " + str(accuracy_score(testing.label, testing.prediction)) +"\n"
    presisi = "Presisi: " + str(precision_score(testing.label, testing.prediction)) +"\n"
    recall = "Recall: "+ str(recall_score(testing.label, testing.prediction)) +"\n"
    f1 = "F1-score: " + str(f1_score(testing.label, testing.prediction)) +"\n"
    roc_training = "ROC Training: " + str(roc_auc_score(training['label'], training['probability'])) + "\n"
    roc_testing = "ROC Testing: " + str(roc_auc_score(testing['label'], testing['probability']))
    metrics = akurasi + presisi + recall + f1 + roc_training + roc_testing
    matrix_confusion(testing)
    plot_training(training)
    plot_testing(testing)
    return metrics