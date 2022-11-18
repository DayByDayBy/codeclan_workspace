def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"
    if final_score["home_score"] < final_score["away_score"]:
        return "Away win"
    if final_score["away_score"] == final_score["home_score"]:
        return "Draw"

def get_results(final_scores):
    results = [get_result(score) for score in final_scores]
    return results