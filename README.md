# StarQuality
Aggregating Reviews to Rank Products

Reference : http://www.aaai.org/ocs/index.php/ICWSM/ICWSM10/paper/download/1507/1844/

Implemented the statistical and reweighting models as described in the reference, evaluated the models and compared the results.

Extension to the paper:
1. Found the helpfullness scores of reviewers.
2. Implemented a new Re-weighting model using positive and negative votes for given rating :
    modified_rating = ((1+positive_votes) * rating + negative_votes * (6-rating))/(1+total_votes)
    
Important files :
1. get_rating.py  -   contains methods that perform statistical and reweighting models discussed in the paper.
2. helpfullness.py  - to estimate the helpfullness scores of reviewers.
3. get_rating.ipynb - to estimate product rating also considering the votes given to reviews for a given product.
4. report.txt     -   contains results and observations.
