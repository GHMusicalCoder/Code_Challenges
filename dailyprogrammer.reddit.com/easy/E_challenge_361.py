def get_scores(results):
    scores = {}
    for c in results:
        if c.lower() in scores:
            scores[c.lower()] += 1 if c.islower() else -1
        else:
            scores[c.lower()] = 1 if c.islower() else -1
    return ', '.join(f"{k}:{scores[k]}" for k in sorted(scores, key=scores.get, reverse=True))


input = "EbAAdbBEaBaaBBdAccbeebaec"
print(get_scores(input))