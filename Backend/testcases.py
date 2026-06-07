testcases = {
    1: [

        # Easy
    
        {
            "input": "6\n-1 0 1 2 -1 -4",
            "output": "-1 -1 2\n-1 0 1"
        },
    
        {
            "input": "3\n0 0 0",
            "output": "0 0 0"
        },
    
        {
            "input": "4\n-1 0 1 2",
            "output": "-1 0 1"
        },
    
        {
            "input": "5\n-2 0 2 1 -1",
            "output": "-2 0 2\n-1 0 1"
        },
    
        {
            "input": "5\n-3 1 2 0 5",
            "output": "-3 1 2"
        },
    
        # Medium
    
        {
            "input": "6\n-2 -1 0 1 2 3",
            "output": "-2 -1 3\n-2 0 2\n-1 0 1"
        },
    
        {
            "input": "7\n-4 -2 -1 0 1 2 5",
            "output": "-4 -1 5\n-2 0 2\n-1 0 1"
        },
    
        {
            "input": "7\n-5 -3 -2 0 2 3 5",
            "output": "-5 0 5\n-5 2 3\n-3 -2 5\n-3 0 3\n-2 0 2"
        },
    
        {
            "input": "8\n-4 -1 -1 0 1 2 2 3",
            "output": "-4 1 3\n-4 2 2\n-1 -1 2\n-1 0 1"
        },
    
        {
            "input": "7\n-6 -3 0 1 2 3 6",
            "output": "-6 0 6\n-3 0 3\n-3 1 2"
        },
    
        # Hard / Duplicate Heavy
    
        {
            "input": "6\n0 0 0 0 0 0",
            "output": "0 0 0"
        },
    
        {
            "input": "7\n-1 -1 -1 2 2 2 0",
            "output": "-1 -1 2"
        },
    
        {
            "input": "8\n-2 -2 0 0 2 2 1 -1",
            "output": "-2 0 2\n-1 0 1"
        },
    
        {
            "input": "9\n-4 -2 -2 0 0 2 2 4 4",
            "output": "-4 0 4\n-4 2 2\n-2 -2 4\n-2 0 2"
        },
    
        {
            "input": "8\n-3 -3 0 0 3 3 1 -1",
            "output": "-3 0 3\n-1 0 1"
        },
    
        # Edge Cases
    
        {
            "input": "3\n1 2 3",
            "output": ""
        },
    
        {
            "input": "3\n-1 -2 -3",
            "output": ""
        },
    
        {
            "input": "4\n0 1 1 2",
            "output": ""
        },
    
        {
            "input": "3\n-100000 0 100000",
            "output": "-100000 0 100000"
        },
    
        {
            "input": "5\n-100000 -1 0 1 100000",
            "output": "-100000 0 100000\n-1 0 1"
        } 
    ],


    2: [

        # Easy
    
        {
            "input": "6\neat tea tan ate nat bat",
            "output": "eat tea ate\ntan nat\nbat"
        },
    
        {
            "input": "3\nabc bca cab",
            "output": "abc bca cab"
        },
    
        {
            "input": "3\ncat dog tac",
            "output": "cat tac\ndog"
        },
    
        {
            "input": "4\nrat tar art car",
            "output": "rat tar art\ncar"
        },
    
        {
            "input": "2\nhello world",
            "output": "hello\nworld"
        },
    
        # Medium
    
        {
            "input": "6\nlisten silent enlist abc bac cab",
            "output": "listen silent enlist\nabc bac cab"
        },
    
        {
            "input": "6\nloop pool polo hello olleh world",
            "output": "loop pool polo\nhello olleh\nworld"
        },
    
        {
            "input": "5\nabcd bcda cdab dabc xyz",
            "output": "abcd bcda cdab dabc\nxyz"
        },
    
        {
            "input": "6\nrace care acre stop pots tops",
            "output": "race care acre\nstop pots tops"
        },
    
        {
            "input": "6\nmoon mono onom eat tea ate",
            "output": "moon mono onom\neat tea ate"
        },
    
        # Hard
    
        {
            "input": "7\na aa aaa aaaa b bb bbb",
            "output": "a\naa\naaa\naaaa\nb\nbb\nbbb"
        },
    
        {
            "input": "6\nzzz zzz zzz abc bca cab",
            "output": "zzz zzz zzz\nabc bca cab"
        },
    
        {
            "input": "8\nabcd bcad acbd bacd dcba abdc xyz zyx",
            "output": "abcd bcad acbd bacd dcba abdc\nxyz zyx"
        },
    
        {
            "input": "6\nabab baba aabb bbaa abba baab",
            "output": "abab baba\naabb bbaa abba baab"
        },
    
        {
            "input": "6\nstate taste tates hello olleh below",
            "output": "state taste tates\nhello olleh\nbelow"
        },
    
        # Edge Cases
    
        {
            "input": "1\na",
            "output": "a"
        },
    
        {
            "input": "2\nab ba",
            "output": "ab ba"
        },
    
        {
            "input": "3\nabc def ghi",
            "output": "abc\ndef\nghi"
        },
    
        {
            "input": "4\nzzz zzz zzz zzz",
            "output": "zzz zzz zzz zzz"
        },
    
        {
            "input": "5\nx y z xy yz",
            "output": "x\ny\nz\nxy\nyz"
        }
    ],


    3: [

        # Easy

        {
            "input": "4\n1 2 3 4",
            "output": "24 12 8 6"
        },
    
        {
            "input": "3\n2 3 4",
            "output": "12 8 6"
        },
    
        {
            "input": "5\n1 1 1 1 1",
            "output": "1 1 1 1 1"
        },
    
        {
            "input": "2\n5 10",
            "output": "10 5"
        },
    
        {
            "input": "4\n2 2 2 2",
            "output": "8 8 8 8"
        },
    
        # Medium
    
        {
            "input": "5\n1 2 3 4 5",
            "output": "120 60 40 30 24"
        },
    
        {
            "input": "4\n3 4 5 6",
            "output": "120 90 72 60"
        },
    
        {
            "input": "5\n2 3 5 7 11",
            "output": "1155 770 462 330 210"
        },
    
        {
            "input": "6\n1 2 1 2 1 2",
            "output": "8 4 8 4 8 4"
        },
    
        {
            "input": "4\n10 20 30 40",
            "output": "24000 12000 8000 6000"
        },
    
        # Zero Cases
    
        {
            "input": "4\n0 1 2 3",
            "output": "6 0 0 0"
        },
    
        {
            "input": "5\n1 0 3 0 5",
            "output": "0 0 0 0 0"
        },
    
        {
            "input": "3\n0 0 7",
            "output": "0 0 0"
        },
    
        {
            "input": "2\n0 5",
            "output": "5 0"
        },
    
        # Negative Numbers
    
        {
            "input": "4\n-1 2 3 4",
            "output": "24 -12 -8 -6"
        },
    
        {
            "input": "4\n-1 -2 3 4",
            "output": "-24 -12 8 6"
        },
    
        {
            "input": "4\n-1 -2 -3 -4",
            "output": "-24 -12 -8 -6"
        },
    
        # Edge Cases
    
        {
            "input": "1\n5",
            "output": "1"
        },
    
        {
            "input": "2\n1 1",
            "output": "1 1"
        },
    
        {
            "input": "3\n100 100 100",
            "output": "10000 10000 10000"
        }
    ],


    4: [
        {
            "input": "6\n100 4 200 1 3 2",
            "output": "4"
        },
        {
            "input": "5\n0 3 7 2 5",
            "output": "2"
        },
        {
            "input": "9\n0 3 7 2 5 8 4 6 1",
            "output": "9"
        },
        {
            "input": "1\n5",
            "output": "1"
        },
        {
            "input": "5\n1 2 3 4 5",
            "output": "5"
        },
        {
            "input": "5\n5 4 3 2 1",
            "output": "5"
        },
        {
            "input": "6\n10 30 20 40 50 60",
            "output": "1"
        },
        {
            "input": "7\n1 2 2 3 4 4 5",
            "output": "5"
        },
        {
            "input": "5\n-1 -2 -3 -4 -5",
            "output": "5"
        },
        {
            "input": "6\n-2 -1 0 1 2 10",
            "output": "5"
        },
        {
            "input": "8\n9 1 4 7 3 -1 0 5",
            "output": "3"
        },
        {
            "input": "4\n1000 1001 1002 1003",
            "output": "4"
        },
        {
            "input": "4\n1 10 20 30",
            "output": "1"
        },
        {
            "input": "6\n8 7 6 5 4 3",
            "output": "6"
        },
        {
            "input": "3\n1 3 5",
            "output": "1"
        },
        {
            "input": "10\n1 9 3 10 2 20 4 5 6 7",
            "output": "7"
        },
        {
            "input": "5\n100 101 102 104 105",
            "output": "3"
        },
        {
            "input": "5\n0 1 2 50 51",
            "output": "3"
        },
        {
            "input": "6\n-10 -9 -8 1 2 3",
            "output": "3"
        },
        {
            "input": "7\n15 14 13 12 11 10 9",
            "output": "7"
        }
    ],


    5: [

        # Easy
    
        {
            "input": "6 2\n1 1 1 2 2 3",
            "output": "1 2"
        },
    
        {
            "input": "5 1\n5 5 5 1 2",
            "output": "5"
        },
    
        {
            "input": "4 2\n1 1 2 2",
            "output": "1 2"
        },
    
        {
            "input": "6 1\n3 3 3 2 2 1",
            "output": "3"
        },
    
        {
            "input": "5 2\n1 2 2 3 3",
            "output": "2 3"
        },
    
        # Medium
    
        {
            "input": "8 3\n1 1 1 2 2 3 3 4",
            "output": "1 2 3"
        },
    
        {
            "input": "10 2\n5 5 5 5 4 4 4 3 2 1",
            "output": "5 4"
        },
    
        {
            "input": "7 2\n7 7 6 6 5 4 3",
            "output": "7 6"
        },
    
        {
            "input": "9 3\n1 1 2 2 3 3 4 5 6",
            "output": "1 2 3"
        },
    
        {
            "input": "8 2\n9 9 9 8 8 7 6 5",
            "output": "9 8"
        },
    
        # Hard
    
        {
            "input": "12 3\n1 1 1 2 2 2 3 3 3 4 4 5",
            "output": "1 2 3"
        },
    
        {
            "input": "10 4\n1 1 2 2 3 3 4 4 5 5",
            "output": "1 2 3 4"
        },
    
        {
            "input": "12 2\n10 10 10 10 9 9 9 8 8 7 6 5",
            "output": "10 9"
        },
    
        {
            "input": "9 3\n4 4 4 3 3 2 2 1 1",
            "output": "4 3 2"
        },
    
        {
            "input": "11 2\n8 8 8 8 7 7 7 6 6 5 4",
            "output": "8 7"
        },
    
        # Edge Cases
    
        {
            "input": "1 1\n5",
            "output": "5"
        },
    
        {
            "input": "2 2\n1 2",
            "output": "1 2"
        },
    
        {
            "input": "5 5\n1 2 3 4 5",
            "output": "1 2 3 4 5"
        },
    
        {
            "input": "6 1\n0 0 0 0 0 0",
            "output": "0"
        },
    
        {
            "input": "6 2\n-1 -1 -2 -2 -2 -3",
            "output": "-2 -1"
        }
    ],


    6: [
        {"input":"abcabcbb","output":"3"},
        {"input":"bbbbb","output":"1"},
        {"input":"pwwkew","output":"3"},
        {"input":"abcdef","output":"6"},
        {"input":"a","output":"1"},
        {"input":"aa","output":"1"},
        {"input":"ab","output":"2"},
        {"input":"abba","output":"2"},
        {"input":"dvdf","output":"3"},
        {"input":"anviaj","output":"5"},
        {"input":"tmmzuxt","output":"5"},
        {"input":" ","output":"1"},
        {"input":"au","output":"2"},
        {"input":"abcadeaf","output":"5"},
        {"input":"abcddefgh","output":"5"},
        {"input":"abcdefghijklmnopqrstuvwxyz","output":"26"},
        {"input":"abababab","output":"2"},
        {"input":"aab","output":"2"},
        {"input":"abcabcabcd","output":"4"},
        {"input":"zzzzzzzz","output":"1"}
    ],


    7: [
        {"input":"ABAB\n2","output":"4"},
        {"input":"AABABBA\n1","output":"4"},
        {"input":"AAAA\n2","output":"4"},
        {"input":"ABCDE\n1","output":"2"},
        {"input":"ABCDE\n2","output":"3"},
        {"input":"ABBB\n2","output":"4"},
        {"input":"BAAA\n0","output":"3"},
        {"input":"ABAA\n0","output":"2"},
        {"input":"ABAA\n1","output":"4"},
        {"input":"ABCD\n0","output":"1"},
        {"input":"ABCD\n3","output":"4"},
        {"input":"AABBC\n2","output":"4"},
        {"input":"BBBBBA\n1","output":"6"},
        {"input":"ABCABC\n2","output":"4"},
        {"input":"AAAB\n0","output":"3"},
        {"input":"AAAB\n1","output":"4"},
        {"input":"ABABABAB\n2","output":"5"},
        {"input":"ABCCDE\n1","output":"3"},
        {"input":"A\n0","output":"1"},
        {"input":"XYZXYZ\n3","output":"5"}
    ],


    8: [
        {"input":"ab\neidbaooo","output":"True"},
        {"input":"ab\neidboaoo","output":"False"},
        {"input":"adc\ndcda","output":"True"},
        {"input":"hello\nooolleoooleh","output":"False"},
        {"input":"a\nab","output":"True"},
        {"input":"abc\nbbbca","output":"True"},
        {"input":"abc\ncccccc","output":"False"},
        {"input":"xyz\nzyx","output":"True"},
        {"input":"xyz\nxyyzz","output":"False"},
        {"input":"aa\naaa","output":"True"},
        {"input":"aa\nabc","output":"False"},
        {"input":"abc\ncbaebabacd","output":"True"},
        {"input":"abc\nbbbbbbabc","output":"True"},
        {"input":"abcd\nabc","output":"False"},
        {"input":"abcd\ndcba","output":"True"},
        {"input":"ab\nba","output":"True"},
        {"input":"ab\nac","output":"False"},
        {"input":"cat\ntacocat","output":"True"},
        {"input":"dog\ngod","output":"True"},
        {"input":"dog\nodgxx","output":"True"}
    ],


    9: [
        {"input":"7\n2 3 1 2 4 3","output":"2"},
        {"input":"4\n1 4 4 1","output":"1"},
        {"input":"8\n1 1 1 1 1 1 1 1","output":"8"},
        {"input":"6\n1 2 3 4 5 6","output":"1"},
        {"input":"5\n5 1 1 1 1","output":"1"},
    
        # Medium
    
        {"input":"5\n2 2 2 2 2","output":"3"},
        {"input":"5\n10 1 1 1 1","output":"1"},
        {"input":"3\n7 1 1","output":"1"},
        {"input":"5\n1 1 1 1 10","output":"1"},
        {"input":"5\n3 3 3 3 3","output":"2"},
    
        # Hard
    
        {"input":"6\n2 3 1 2 4 3","output":"2"},
        {"input":"5\n1 2 3 4 5","output":"1"},
        {"input":"6\n5 1 3 5 10 7","output":"1"},
        {"input":"4\n2 2 2 2","output":"2"},
        {"input":"5\n8 1 1 1 1","output":"1"},
    
        # Edge Cases
    
        {"input":"7\n1 2 3 4 5 6 7","output":"1"},
        {"input":"4\n1 1 1 1","output":"4"},
        {"input":"5\n9 1 1 1 1","output":"1"},
        {"input":"5\n4 2 2 7 8","output":"1"},
        {"input":"5\n1 1 1 1 1","output":"5"}
    ],


    10: [
        {"input":"6 4\n1 12 -5 -6 50 3","output":"12.75"},
        {"input":"5 1\n1 2 3 4 5","output":"5.0"},
        {"input":"5 5\n1 2 3 4 5","output":"3.0"},
        {"input":"4 2\n5 5 5 5","output":"5.0"},
        {"input":"6 3\n1 2 3 4 5 6","output":"5.0"},
        {"input":"6 2\n1 2 3 4 5 6","output":"5.5"},
        {"input":"4 2\n-1 -2 -3 -4","output":"-1.5"},
        {"input":"5 3\n0 0 0 0 0","output":"0.0"},
        {"input":"6 4\n10 20 30 40 50 60","output":"45.0"},
        {"input":"5 2\n1 100 1 100 1","output":"50.5"},
        {"input":"7 3\n3 3 3 3 3 3 3","output":"3.0"},
        {"input":"6 5\n1 2 3 4 5 6","output":"4.0"},
        {"input":"4 1\n9 8 7 6","output":"9.0"},
        {"input":"5 2\n2 4 6 8 10","output":"9.0"},
        {"input":"6 3\n1 1 100 1 1 1","output":"34.0"},
        {"input":"5 4\n5 4 3 2 1","output":"3.5"},
        {"input":"5 2\n-5 -4 -3 -2 -1","output":"-1.5"},
        {"input":"6 2\n1 3 5 7 9 11","output":"10.0"},
        {"input":"5 3\n2 2 2 2 2","output":"2.0"},
        {"input":"6 4\n4 4 4 4 4 4","output":"4.0"}
    ],


    11: [
        {"input":"9\n1 8 6 2 5 4 8 3 7","output":"49"},
        {"input":"2\n1 1","output":"1"},
        {"input":"5\n1 2 3 4 5","output":"6"},
        {"input":"5\n5 4 3 2 1","output":"6"},
        {"input":"6\n2 3 4 5 18 17","output":"17"},
        {"input":"4\n1 1 1 1","output":"3"},
        {"input":"5\n10 1 10 1 10","output":"40"},
        {"input":"3\n1 2 1","output":"2"},
        {"input":"6\n1 3 2 5 25 24","output":"24"},
        {"input":"4\n100 1 1 100","output":"300"},
        {"input":"5\n4 3 2 1 4","output":"16"},
        {"input":"5\n1 2 1 2 1","output":"4"},
        {"input":"6\n6 5 4 3 2 1","output":"9"},
        {"input":"6\n1 2 3 4 5 6","output":"9"},
        {"input":"5\n2 2 2 2 2","output":"8"},
        {"input":"4\n1 100 100 1","output":"100"},
        {"input":"3\n5 5 5","output":"10"},
        {"input":"4\n0 0 0 0","output":"0"},
        {"input":"5\n0 1 2 3 4","output":"4"},
        {"input":"5\n4 3 2 1 0","output":"4"}  
    ],


    12: [
        {"input":"A man, a plan, a canal: Panama","output":"True"},
        {"input":"race a car","output":"False"},
        {"input":" ","output":"True"},
        {"input":"a","output":"True"},
        {"input":"aa","output":"True"},
        {"input":"ab","output":"False"},
        {"input":"Madam","output":"True"},
        {"input":"No lemon, no melon","output":"True"},
        {"input":"12321","output":"True"},
        {"input":"123421","output":"False"},
        {"input":"Was it a car or a cat I saw?","output":"True"},
        {"input":"hello","output":"False"},
        {"input":"Able was I ere I saw Elba","output":"True"},
        {"input":"abcba","output":"True"},
        {"input":"abccba","output":"True"},
        {"input":"abca","output":"False"},
        {"input":"!!","output":"True"},
        {"input":"0P","output":"False"},
        {"input":"Red rum, sir, is murder","output":"True"},
        {"input":"Never odd or even","output":"True"}  
    ],


    13: [
        {"input":"4 9\n2 7 11 15","output":"1 2"},
        {"input":"3 6\n2 3 4","output":"1 3"},
        {"input":"2 -1\n-1 0","output":"1 2"},
        {"input":"5 8\n1 2 3 4 5","output":"3 5"},
        {"input":"5 7\n1 2 3 4 5","output":"2 5"},
        {"input":"4 5\n1 2 3 4","output":"1 4"},
        {"input":"6 11\n1 2 3 4 5 6","output":"5 6"},
        {"input":"4 3\n1 2 3 4","output":"1 2"},
        {"input":"5 9\n1 2 3 4 5","output":"4 5"},
        {"input":"5 6\n1 2 3 4 5","output":"1 5"},
        {"input":"6 13\n1 2 3 4 5 8","output":"5 6"},
        {"input":"4 10\n1 2 8 9","output":"1 4"},
        {"input":"5 11\n1 2 3 8 9","output":"2 5"},
        {"input":"5 12\n1 2 3 4 8","output":"4 5"},
        {"input":"5 10\n1 2 3 7 8","output":"2 5"},
        {"input":"4 7\n1 2 5 6","output":"1 4"},
        {"input":"6 7\n1 1 2 3 4 6","output":"1 6"},
        {"input":"5 15\n1 2 3 7 8","output":"4 5"},
        {"input":"5 5\n1 2 3 4 5","output":"1 4"},
        {"input":"5 4\n1 2 2 3 4","output":"1 4"}    
    ],
    
    
    14: [
        {"input":"5\n0 1 0 3 12","output":"1 3 12 0 0"},
        {"input":"1\n0","output":"0"},
        {"input":"1\n5","output":"5"},
        {"input":"5\n1 2 3 4 5","output":"1 2 3 4 5"},
        {"input":"5\n0 0 0 1 2","output":"1 2 0 0 0"},
        {"input":"5\n1 2 0 0 3","output":"1 2 3 0 0"},
        {"input":"4\n0 0 0 0","output":"0 0 0 0"},
        {"input":"5\n1 0 2 0 3","output":"1 2 3 0 0"},
        {"input":"6\n0 1 2 3 0 4","output":"1 2 3 4 0 0"},
        {"input":"5\n4 0 5 0 6","output":"4 5 6 0 0"},
        {"input":"3\n1 0 0","output":"1 0 0"},
        {"input":"3\n0 1 0","output":"1 0 0"},
        {"input":"6\n1 2 3 4 5 0","output":"1 2 3 4 5 0"},
        {"input":"6\n0 1 2 3 4 5","output":"1 2 3 4 5 0"},
        {"input":"5\n2 0 2 0 2","output":"2 2 2 0 0"},
        {"input":"4\n9 8 7 6","output":"9 8 7 6"},
        {"input":"4\n0 9 8 7","output":"9 8 7 0"},
        {"input":"4\n9 8 0 7","output":"9 8 7 0"},
        {"input":"5\n0 1 0 0 2","output":"1 2 0 0 0"},
        {"input":"5\n3 0 4 5 0","output":"3 4 5 0 0"}    
    ],


    15: [
        {"input":"5\n-4 -1 0 3 10","output":"0 1 9 16 100"},
        {"input":"5\n-7 -3 2 3 11","output":"4 9 9 49 121"},
        {"input":"1\n0","output":"0"},
        {"input":"1\n5","output":"25"},
        {"input":"1\n-5","output":"25"},
        {"input":"4\n-2 -1 1 2","output":"1 1 4 4"},
        {"input":"5\n-5 -4 -3 -2 -1","output":"1 4 9 16 25"},
        {"input":"5\n1 2 3 4 5","output":"1 4 9 16 25"},
        {"input":"6\n-6 -5 -4 1 2 3","output":"1 4 9 16 25 36"},
        {"input":"4\n-1 0 1 2","output":"0 1 1 4"},
        {"input":"5\n-10 -5 0 5 10","output":"0 25 25 100 100"},
        {"input":"3\n-2 0 2","output":"0 4 4"},
        {"input":"4\n-3 -1 2 4","output":"1 4 9 16"},
        {"input":"5\n-8 -4 0 4 8","output":"0 16 16 64 64"},
        {"input":"2\n-1 1","output":"1 1"},
        {"input":"2\n0 0","output":"0 0"},
        {"input":"3\n1 1 1","output":"1 1 1"},
        {"input":"3\n-1 -1 -1","output":"1 1 1"},
        {"input":"4\n-2 -2 2 2","output":"4 4 4 4"},
        {"input":"5\n-3 -2 -1 0 1","output":"0 1 1 4 9"} 
    ],
}