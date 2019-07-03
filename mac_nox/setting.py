def cx(x):
	return x
def cy(y):
	return y
region_x = 853*2
region_y = 660*2
coord_multiplier = 2.0

"""
selection pool
key: 6 participant classes separated by spaces, [:3] is sorted and [3:] is sorted per group team and enemy, so [:] is not sorted
value: dict as 3 pairs of classes key is team class, value is enemy class
"""
class_selection_pool = {
 'cosmic science skill mystic mystic tech'	: {'cosmic': 'tech', 'science': 'mystic', 'skill': 'mystic'},
 'cosmic mystic mystic cosmic science skill': {'mystic': 'skill', 'cosmic': 'science'},
 'cosmic mystic science cosmic science skill': {'cosmic': 'skill', 'mystic': 'cosmic', 'science': 'science'},
 'cosmic mystic tech cosmic mutant science'	: {'cosmic': 'science', 'mystic': 'cosmic', 'tech': 'mutant'},
 'mutant mutant tech cosmic mutant science'	: {'mutant': 'science', 'tech': 'mutant'},
 'cosmic mystic tech science skill tech'	: {'mystic': 'skill', 'cosmic': 'tech', 'tech': 'science'},
 'mutant mystic science cosmic mutant tech'	: {'mutant': 'mutant', 'mystic': 'cosmic', 'science': 'tech'},
 'mutant mystic skill cosmic mutant science': {'mutant': 'cosmic', 'mystic': 'cosmic', 'skill': 'science'},
 'mutant mystic tech cosmic cosmic cosmic'	: {'mutant': 'cosmic', 'mystic': 'cosmic', 'tech': 'cosmic'},
 'mutant mystic tech science science tech'	: {'mutant': 'science', 'tech': 'science', 'mystic': 'tech'},
 'mutant skill skill mutant science science': {'mutant': 'mutant', 'skill': 'science'},
 'science skill skill cosmic mutant mystic'	: {'science': 'mutant', 'skill': 'mystic'},
 'cosmic mystic tech mutant tech tech'		: {"cosmic":"tech", "mystic":"tech", "tech":"mutant"},
 'cosmic science skill cosmic mutant science': {'cosmic': 'cosmic', 'science': 'mutant', 'skill': 'science'},
 'mystic skill tech cosmic mystic tech'		: {'mystic': 'cosmic', 'skill': 'mystic', 'tech': 'tech'},
 'science skill skill science science tech'	: {'science': 'tech', 'skill': 'science'},
 'cosmic mystic tech cosmic mutant mutant'	: {'cosmic': 'mutant', 'mystic': 'cosmic', 'tech': 'mutant'},
 'cosmic mystic skill cosmic mutant tech'	: {'cosmic': 'tech', 'mystic': 'cosmic', 'skill': 'mutant'},
 'cosmic cosmic skill mystic skill skill'	: {"cosmic":"skill", "cosmic":"skill", "skill":"mystic"},
 'mutant science skill mystic science skill': {"mutant":"skill", "science":"mystic","skill":"science"},
 'cosmic science skill mutant skill tech'	: {"cosmic":"tech", "science":"mutant", "skill":"skill"},
 'mutant science skill mutant mutant science': {"mutant":"mutant", "science":"mutant", "skill":"science"},
 'mutant science tech cosmic mutant mystic'	: {"mutant":"cosmic","science":"mystic", "tech":"mutant"},
 'cosmic skill skill mystic science skill'	: {"cosmic":"skill", "skill":"science","skill":"mystic"},
 'cosmic science skill mystic mystic skill'	: {"cosmic":"skill", "science":"mystic", "skill":"mystic"},
 'mystic skill tech cosmic science skill'	: {"mystic":"cosmic", "skill":"science", "tech":"skill"},
}
