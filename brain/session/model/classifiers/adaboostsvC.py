import sys
from brain.session.model.adabooster import adaboostgen
from sklearn.svm import SVC


def adaboostsvCgenerate(
    model,
    collection,
    payload,
    list_error,
    learning=1.0,
    estimators=50,
    kernel
):
    return adaboostgen(
        model,
        collection,
        payload,
        list_error,
        learning=learning,
        bnum=estimators,
        be=SVC(kernel=kernel)
    )
