from rouge_score import rouge_scorer
from bert_score import score

def evaluate_query(original, rewritten):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(original, rewritten)
    rouge1 = rouge_scores['rouge1'].fmeasure
    rougeL = rouge_scores['rougeL'].fmeasure

    P, R, F1 = score([rewritten], [original], lang="en", verbose=False)
    bert = F1[0].item()

    return rouge1, rougeL, bert