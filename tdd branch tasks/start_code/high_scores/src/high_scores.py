def latest(scores):
    latest = scores[-1]
    return latest

def personal_best(self):
        scores = [300, 200, 150, 425]
        my_best = max(scores)
        return my_best
        
def personal_top_three(scores):
    top_three = sorted(scores, reverse=True)[:3:]
    return top_three

