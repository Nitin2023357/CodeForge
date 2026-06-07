from special_judges.judges.three_sum import (
    judge_three_sum
)

from special_judges.judges.group_anagrams import (
    judge_group_anagrams
)

from special_judges.judges.top_k_frequent import (
    judge_top_k_frequent
)



SPECIAL_JUDGES = {
    1: judge_three_sum,
    2: judge_group_anagrams,
    5: judge_top_k_frequent
}