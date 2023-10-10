import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # Dictionary mapping the appropriate month to the required integer storge in evidence
    months = {
        "Jan": 0,
        "Feb": 1,
        "Mar": 2,
        "Apr": 3,
        "May": 4,
        "June": 5,
        "Jul": 6,
        "Aug": 7,
        "Sep": 8,
        "Oct": 9,
        "Nov": 10,
        "Dec": 11,
    }

    revenue = {"TRUE": 1, "FALSE": 0}

    # Read in data, separating evidence and label
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        data = []
        for row in reader:
            data.append(
                {
                    "evidence": [
                        int(row[i])
                        if i == 0 or i == 2 or i == 4 or 10 < i < 15
                        else float(row[i])
                        if i == 1 or i == 3 or 4 < i < 10
                        else months[row[i]]
                        if i == 10
                        else 1
                        if i == 15 and row[i] == "Returning_Visitor"
                        else 0
                        if i == 15
                        else 1
                        if i == 16 and row[i] == "TRUE"
                        else 0
                        for i in range(17)
                    ],
                    "label": revenue[row[17]],
                }
            )
    # Figure out evidence and classification
    evidence = [row["evidence"] for row in data]
    label = [row["label"] for row in data]

    return (evidence, label)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # Initialize model
    model = KNeighborsClassifier(n_neighbors=1)
    # Train model
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    actual_pos = 0
    actual_neg = 0
    pred_pos = 0
    pred_neg = 0
    for i in range(len(labels)):
        if labels[i] == 1:
            actual_pos += 1
            if predictions[i] == 1:
                pred_pos += 1
        else:
            actual_neg += 1
            if predictions[i] == 0:
                pred_neg += 1

    return (pred_pos / actual_pos, pred_neg / actual_neg)


if __name__ == "__main__":
    main()
