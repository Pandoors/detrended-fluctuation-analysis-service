import numpy as np
import fathon
from fathon import fathonUtils as fu
from flask import Flask, request, jsonify
from flask_cors import CORS


def perform_dfa(data_value):
    # a = np.array(data_value.split(", ")).astype(int)
    a = fu.toAggregated(data_value)
    # a = 60/a
    pydfa = fathon.DFA(a)

    winSizes = fu.linRangeByStep(200, 500)
    revSeg = True
    polOrd = 3

    n, F = pydfa.computeFlucVec(winSizes, revSeg=revSeg, polOrd=polOrd)

    H, H_intercept = pydfa.fitFlucVec()

    limits_list = np.array([[200, 500], [200, 500]], dtype=int)
    list_H, list_H_intercept = pydfa.multiFitFlucVec(limits_list)
    response = {
        'H': H,
        'list_H': list_H.tolist(),  # Convert NumPy array to a list
        'n': n.tolist(),  # Convert NumPy array to a list
        'F': F.tolist()  # Convert NumPy array to a list
    }

    return jsonify(response)


def validate_data(data):
    try:
        numbers = [int(x) for x in data.split(", ")]
        return True
    except ValueError:
        return False


def handle_request():
    data = request.get_json()
    data_value = data['data']
    print(data_value)
    return perform_dfa(data_value)



if __name__ == '__main__':
    pass
