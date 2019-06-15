def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    precision = 0
    recall = 0
    accuracy = 0
    f1 = 0

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score

    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(prediction.shape[0]):
        if prediction[i] == True:
            if prediction[i] == ground_truth[i]:
                TP = TP + 1
            else:
                FP = FP + 1
        
        if prediction[i] == False:
            if prediction[i] == ground_truth[i]:
                TN = TN + 1
            else:
                FN = FN + 1

    RE = len(list(filter(lambda x: x == True, ground_truth)))

    Pred_true = len(list(filter(lambda x: x == True, prediction)))

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    accuracy = (TP+TN)/(TP+FP+FN+TN)

    f1 = (2*precision*recall)/(precision + recall)

    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    return 0
