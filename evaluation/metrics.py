def compute_f1(predicted, gold):
    predicted_set = set(predicted)
    gold_set = set(gold)
    overlap = predicted_set & gold_set
    precision = len(overlap) / len(predicted_set) if predicted_set else 0
    recall = len(overlap) / len(gold_set) if gold_set else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
    return precision, recall, f1