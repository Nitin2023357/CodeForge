problems = {
    1: {
        "id": 1,
        "title": "3Sum",
        "difficulty": "Medium",
        "topic": "Arrays",
    
        "statement":
            "Given an array of N integers, find all unique triplets "
            "(a, b, c) such that a + b + c = 0.\n\n"
            "Print each valid triplet in sorted order. "
            "The output triplets must also be unique.",
    
        "examples": [
            {
                "input": "6\n-1 0 1 2 -1 -4",
                "output": "-1 -1 2\n-1 0 1",
                "explanation":
                    "There are two unique triplets whose sum is 0."
            },
            {
                "input": "3\n0 0 0",
                "output": "0 0 0",
                "explanation":
                    "Only one valid triplet exists."
            }
        ],
    
        "constraints": [
            "3 <= N <= 3000",
            "-10^5 <= arr[i] <= 10^5"
        ]
    },
    
    2: {
        "id": 2,
        "title": "Group Anagrams",
        "difficulty": "Medium",
        "topic": "Arrays",
    
        "statement":
            "Given N strings, group all anagrams together.\n\n"
            "Strings belonging to the same anagram group "
            "must be printed on the same line.",
    
        "examples": [
            {
                "input": "6\neat tea tan ate nat bat",
                "output": "eat tea ate\ntan nat\nbat",
                "explanation":
                    "Words that are anagrams are grouped together."
            }
        ],
    
        "constraints": [
            "1 <= N <= 1000",
            "1 <= length of each string <= 100"
        ]
    },
    
    3: {
        "id": 3,
        "title": "Product of Array Except Self",
        "difficulty": "Medium",
        "topic": "Arrays",
    
        "statement":
            "Given an array of N integers, construct an output array "
            "where output[i] is equal to the product of all elements "
            "except arr[i].\n\n"
            "Do not use division.",
    
        "examples": [
            {
                "input": "4\n1 2 3 4",
                "output": "24 12 8 6",
                "explanation":
                    "Each position contains the product of all other elements."
            }
        ],
    
        "constraints": [
            "2 <= N <= 100000",
            "-30 <= arr[i] <= 30"
        ]
    },
    
    4: {
        "id": 4,
        "title": "Longest Consecutive Sequence",
        "difficulty": "Medium",
        "topic": "Arrays",
    
        "statement":
            "Given an unsorted array of integers, determine the length "
            "of the longest sequence of consecutive integers.",
    
        "examples": [
            {
                "input": "6\n100 4 200 1 3 2",
                "output": "4",
                "explanation":
                    "The longest consecutive sequence is 1,2,3,4."
            }
        ],
    
        "constraints": [
            "0 <= N <= 100000",
            "-10^9 <= arr[i] <= 10^9"
        ]
    },
    
    5: {
        "id": 5,
        "title": "Top K Frequent Elements",
        "difficulty": "Medium",
        "topic": "Arrays",
    
        "statement":
            "Given an integer array and an integer K, print the K most "
            "frequent elements in the array.\n\n"
            "If multiple answers are possible, print any valid order.",
    
        "examples": [
            {
                "input": "6 2\n1 1 1 2 2 3",
                "output": "1 2",
                "explanation":
                    "1 appears three times and 2 appears twice."
            }
        ],
    
        "constraints": [
            "1 <= N <= 100000",
            "-10000 <= arr[i] <= 10000",
            "1 <= K <= number of unique elements"
        ]
    },
    
    6: {
        "id": 6,
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "topic": "Sliding Window",
    
        "statement":
            "Given a string S, find the length of the longest substring "
            "that contains no repeating characters.",
    
        "examples": [
            {
                "input": "abcabcbb",
                "output": "3",
                "explanation":
                    "The longest substring without repeating characters is 'abc'."
            }
        ],
    
        "constraints": [
            "0 <= |S| <= 50000",
            "S consists of English letters, digits and symbols"
        ]
    },
    
    7: {
        "id": 7,
        "title": "Longest Repeating Character Replacement",
        "difficulty": "Medium",
        "topic": "Sliding Window",
    
        "statement":
            "Given a string S and an integer K, you may replace at most "
            "K characters. Find the length of the longest substring "
            "containing the same character after replacements.",
    
        "examples": [
            {
                "input": "ABAB\n2",
                "output": "4",
                "explanation":
                    "Replace two characters to make the whole string identical."
            }
        ],
    
        "constraints": [
            "1 <= |S| <= 100000",
            "0 <= K <= |S|"
        ]
    },
    
    8: {
        "id": 8,
        "title": "Permutation in String",
        "difficulty": "Medium",
        "topic": "Sliding Window",
    
        "statement":
            "Given two strings S1 and S2, determine whether any permutation "
            "of S1 exists as a substring of S2.",
    
        "examples": [
            {
                "input": "ab\neidbaooo",
                "output": "True",
                "explanation":
                    "Substring 'ba' is a permutation of 'ab'."
            }
        ],
    
        "constraints": [
            "1 <= |S1|, |S2| <= 10000"
        ]
    },
    
    9: {
        "id": 9,
        "title": "Minimum Size Subarray Sum",
        "difficulty": "Medium",
        "topic": "Sliding Window",
    
        "statement":
            "Given a target integer and an array of positive integers, "
            "find the minimum length of a contiguous subarray whose sum "
            "is greater than or equal to the target. "
            "Return 0 if no such subarray exists.",
    
        "examples": [
            {
                "input": "7\n2 3 1 2 4 3",
                "output": "2",
                "explanation":
                    "The subarray [4,3] has sum 7."
            }
        ],
    
        "constraints": [
            "1 <= N <= 100000",
            "1 <= arr[i] <= 100000",
            "1 <= target <= 10^9"
        ]
    },
    
    10: {
        "id": 10,
        "title": "Maximum Average Subarray I",
        "difficulty": "Medium",
        "topic": "Sliding Window",
    
        "statement":
            "Given an array and an integer K, find the maximum average "
            "value among all contiguous subarrays of length K.",
    
        "examples": [
            {
                "input": "6 4\n1 12 -5 -6 50 3",
                "output": "12.75",
                "explanation":
                    "Subarray [12,-5,-6,50] gives the maximum average."
            }
        ],
    
        "constraints": [
            "1 <= N <= 100000",
            "1 <= K <= N"
        ]
    },
    
    11: {
        "id": 11,
        "title": "Container With Most Water",
        "difficulty": "Medium",
        "topic": "Two Pointers",
    
        "statement":
            "Given N vertical lines represented by heights, find two lines "
            "that together with the x-axis form a container holding the "
            "maximum amount of water.",
    
        "examples": [
            {
                "input": "9\n1 8 6 2 5 4 8 3 7",
                "output": "49",
                "explanation":
                    "Maximum area is formed by heights 8 and 7."
            }
        ],
    
        "constraints": [
            "2 <= N <= 100000",
            "0 <= height[i] <= 10000"
        ]
    },
    
    12: {
        "id": 12,
        "title": "Valid Palindrome",
        "difficulty": "Medium",
        "topic": "Two Pointers",
    
        "statement":
            "Given a string, determine whether it is a palindrome after "
            "removing all non-alphanumeric characters and ignoring case.",
    
        "examples": [
            {
                "input": "A man, a plan, a canal: Panama",
                "output": "True",
                "explanation":
                    "The cleaned string is a palindrome."
            }
        ],
    
        "constraints": [
            "1 <= |S| <= 200000"
        ]
    },
    
    13: {
        "id": 13,
        "title": "Two Sum II - Input Array Is Sorted",
        "difficulty": "Medium",
        "topic": "Two Pointers",
    
        "statement":
            "Given a sorted array and a target value, find the indices "
            "of two numbers whose sum equals the target.",
    
        "examples": [
            {
                "input": "4 9\n2 7 11 15",
                "output": "1 2",
                "explanation":
                    "2 + 7 = 9."
            }
        ],
    
        "constraints": [
            "2 <= N <= 100000"
        ]
    },
    
    14: {
        "id": 14,
        "title": "Move Zeroes",
        "difficulty": "Medium",
        "topic": "Two Pointers",
    
        "statement":
            "Move all zeroes to the end of the array while maintaining "
            "the relative order of non-zero elements.",
    
        "examples": [
            {
                "input": "5\n0 1 0 3 12",
                "output": "1 3 12 0 0",
                "explanation":
                    "All non-zero elements remain in original order."
            }
        ],
    
        "constraints": [
            "1 <= N <= 100000"
        ]
    },
    
    15: {
        "id": 15,
        "title": "Squares of a Sorted Array",
        "difficulty": "Medium",
        "topic": "Two Pointers",
    
        "statement":
            "Given a sorted array, return an array of the squares of each "
            "number also sorted in non-decreasing order.",
    
        "examples": [
            {
                "input": "5\n-4 -1 0 3 10",
                "output": "0 1 9 16 100",
                "explanation":
                    "Squaring and sorting gives the result."
            }
        ],
    
        "constraints": [
            "1 <= N <= 100000",
            "-10000 <= arr[i] <= 10000"
        ]
    }
}