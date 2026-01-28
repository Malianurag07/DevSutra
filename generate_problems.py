"""
Problem Generator Script for DevSutra
Generates 250 problems per difficulty level (BEG, INT, ADV, PRO)
"""
import json
import os

# Define problem templates by difficulty
BEGINNER_TOPICS = [
    # Basic I/O and Variables
    ("Sum of {n} Numbers", "Read {n} integers and print their sum.", "basic_sum"),
    ("Product of {n} Numbers", "Read {n} integers and print their product.", "basic_product"),
    ("Average of {n} Numbers", "Read {n} integers and print their average as an integer.", "basic_average"),
    ("Find Maximum of {n} Numbers", "Read {n} integers and print the maximum.", "find_max"),
    ("Find Minimum of {n} Numbers", "Read {n} integers and print the minimum.", "find_min"),
    
    # Arithmetic Operations
    ("Calculate Expression", "Read a, b, c and calculate: (a + b) * c", "calc_expr"),
    ("Celsius to Fahrenheit", "Convert given Celsius temperature to Fahrenheit: F = C * 9/5 + 32", "temp_convert"),
    ("Fahrenheit to Celsius", "Convert given Fahrenheit temperature to Celsius: C = (F - 32) * 5/9", "temp_convert_rev"),
    ("Circle Area", "Read radius and print area of circle (use 3.14159).", "circle_area"),
    ("Rectangle Area", "Read length and width, print area.", "rect_area"),
    ("Triangle Area", "Read base and height, print area (base * height / 2).", "triangle_area"),
    ("Simple Interest", "Calculate Simple Interest: SI = P * R * T / 100", "simple_interest"),
    ("Compound Amount", "Calculate compound amount: A = P * (1 + R/100)^T", "compound_interest"),
    
    # Number Properties
    ("Check Divisibility", "Check if first number is divisible by second.", "divisibility"),
    ("Check Multiple", "Check if a is a multiple of b.", "multiple_check"),
    ("Sum of Even Numbers", "Print sum of even numbers from 1 to N.", "sum_even"),
    ("Sum of Odd Numbers", "Print sum of odd numbers from 1 to N.", "sum_odd"),
    ("Count Even Numbers", "Count even numbers from 1 to N.", "count_even"),
    ("Count Odd Numbers", "Count odd numbers from 1 to N.", "count_odd"),
    ("Print Even Numbers", "Print all even numbers from 1 to N.", "print_even"),
    ("Print Odd Numbers", "Print all odd numbers from 1 to N.", "print_odd"),
    ("Reverse Number", "Reverse a given integer.", "reverse_num"),
    ("Check Palindrome Number", "Check if a number reads same forwards and backwards.", "palindrome_num"),
    ("First N Natural Numbers", "Print first N natural numbers.", "natural_nums"),
    ("Last Digit", "Print the last digit of a number.", "last_digit"),
    ("First Digit", "Print the first digit of a number.", "first_digit"),
    ("Remove Last Digit", "Remove the last digit from a number.", "remove_last"),
    ("Digit at Position", "Print digit at given position (from right).", "digit_pos"),
    
    # String Operations
    ("Count Vowels", "Count number of vowels in a string.", "count_vowels"),
    ("Count Consonants", "Count number of consonants in a string.", "count_consonants"),
    ("Count Words", "Count number of words in a sentence.", "count_words"),
    ("First Character", "Print the first character of a string.", "first_char"),
    ("Last Character", "Print the last character of a string.", "last_char"),
    ("String Concatenation", "Concatenate two strings with a space.", "concat_strings"),
    ("Repeat String", "Repeat a string N times.", "repeat_string"),
    ("Check Empty", "Check if string is empty.", "check_empty"),
    ("Convert to Lowercase", "Convert string to lowercase.", "to_lower"),
    ("Title Case", "Convert first letter of each word to uppercase.", "title_case"),
    ("Remove Spaces", "Remove all spaces from a string.", "remove_spaces"),
    ("Replace Character", "Replace all occurrences of a character with another.", "replace_char"),
    ("Check Starts With", "Check if string starts with given prefix.", "starts_with"),
    ("Check Ends With", "Check if string ends with given suffix.", "ends_with"),
    
    # Conditionals
    ("Grade Calculator", "Print grade based on marks: A(>=90), B(>=80), C(>=70), D(>=60), F.", "grade_calc"),
    ("Age Category", "Categorize age: Child(<13), Teen(13-19), Adult(20-59), Senior(60+).", "age_category"),
    ("Compare Three Numbers", "Find largest of three numbers.", "compare_three"),
    ("Middle Number", "Find the middle value of three numbers.", "middle_num"),
    ("Triangle Validity", "Check if three sides can form a valid triangle.", "valid_triangle"),
    ("Quadrant", "Determine quadrant of a point (x, y).", "quadrant"),
    ("Day of Week", "Print day name for number (1=Monday, 7=Sunday).", "day_name"),
    ("Month Name", "Print month name for number (1-12).", "month_name"),
    ("Season", "Determine season from month number.", "season"),
    ("Sign of Product", "Determine if product of three numbers is positive, negative, or zero.", "sign_product"),
    
    # Loops
    ("Sum 1 to N", "Calculate sum of 1 to N.", "sum_1_n"),
    ("Sum of Squares", "Calculate sum of squares from 1 to N.", "sum_squares"),
    ("Sum of Cubes", "Calculate sum of cubes from 1 to N.", "sum_cubes"),
    ("Count Divisors", "Count how many numbers from 1 to N divide N evenly.", "count_divisors"),
    ("Print Stars", "Print N stars in a line.", "print_stars"),
    ("Print Pattern", "Print right triangle of stars.", "print_pattern"),
    ("Inverted Triangle", "Print inverted triangle of stars.", "inverted_triangle"),
    ("Number Triangle", "Print triangle with numbers.", "number_triangle"),
    ("Fibonacci First N", "Print first N Fibonacci numbers.", "fibonacci_n"),
    ("Nth Fibonacci", "Print the Nth Fibonacci number.", "nth_fibonacci"),
    ("Check Prime", "Check if a number is prime.", "check_prime"),
    ("Prime Numbers to N", "Print all prime numbers up to N.", "primes_to_n"),
    ("Count Primes", "Count prime numbers up to N.", "count_primes"),
    ("GCD of Two Numbers", "Find GCD of two numbers.", "gcd_two"),
    ("LCM of Two Numbers", "Find LCM of two numbers.", "lcm_two"),
    ("Perfect Number", "Check if a number is perfect.", "perfect_num"),
    ("Armstrong Number", "Check if a number is Armstrong.", "armstrong"),
    ("Strong Number", "Check if a number is strong (sum of factorials of digits).", "strong_num"),
    
    # Arrays/Lists
    ("Array Sum", "Read N numbers and print their sum.", "array_sum"),
    ("Array Average", "Read N numbers and print their average.", "array_avg"),
    ("Array Maximum", "Read N numbers and find maximum.", "array_max"),
    ("Array Minimum", "Read N numbers and find minimum.", "array_min"),
    ("Array Search", "Search for an element in array.", "array_search"),
    ("Count Occurrences", "Count occurrences of a value in array.", "count_occur"),
    ("Second Largest", "Find second largest in array.", "second_largest"),
    ("Second Smallest", "Find second smallest in array.", "second_smallest"),
    ("Array Reverse", "Reverse an array.", "array_reverse"),
    ("Rotate Array Left", "Rotate array left by 1.", "rotate_left"),
    ("Rotate Array Right", "Rotate array right by 1.", "rotate_right"),
    ("Sum of Even Elements", "Sum all even elements in array.", "sum_even_arr"),
    ("Sum of Odd Elements", "Sum all odd elements in array.", "sum_odd_arr"),
    ("Count Positive", "Count positive numbers in array.", "count_positive"),
    ("Count Negative", "Count negative numbers in array.", "count_negative"),
]

INTERMEDIATE_TOPICS = [
    # Advanced Strings
    ("Palindrome Check", "Check if a string is a palindrome (ignore case).", "palindrome_str"),
    ("Anagram Check", "Check if two strings are anagrams.", "anagram"),
    ("Character Frequency", "Print frequency of each character.", "char_freq"),
    ("Most Frequent Character", "Find the most frequent character.", "most_freq_char"),
    ("Longest Word", "Find the longest word in a sentence.", "longest_word"),
    ("Word Frequency", "Count frequency of each word.", "word_freq"),
    ("Remove Duplicates", "Remove duplicate characters from string.", "remove_dup_char"),
    ("Compress String", "Compress string: aabbbcc -> a2b3c2.", "compress_str"),
    ("Valid Parentheses", "Check if parentheses are balanced.", "valid_parens"),
    ("Reverse Words", "Reverse the order of words in a sentence.", "reverse_words"),
    ("Capitalize Words", "Capitalize first letter of each word.", "capitalize"),
    ("Count Substrings", "Count occurrences of a substring.", "count_substr"),
    ("String Rotation", "Check if one string is rotation of another.", "str_rotation"),
    ("Remove Vowels", "Remove all vowels from a string.", "remove_vowels"),
    ("Alternate Case", "Alternate case of each character.", "alternate_case"),
    
    # Advanced Numbers
    ("Next Prime", "Find the next prime after N.", "next_prime"),
    ("Prime Factorization", "Print prime factors of a number.", "prime_factors"),
    ("Perfect Square Check", "Check if a number is a perfect square.", "perfect_square"),
    ("Perfect Cube Check", "Check if a number is a perfect cube.", "perfect_cube"),
    ("Digit Sum Until Single", "Reduce number to single digit by repeated sum.", "digit_reduce"),
    ("Number to Words", "Convert number (0-999) to words.", "num_to_words"),
    ("Roman to Integer", "Convert Roman numeral to integer.", "roman_to_int"),
    ("Integer to Roman", "Convert integer to Roman numeral.", "int_to_roman"),
    ("Binary to Decimal", "Convert binary to decimal.", "binary_to_dec"),
    ("Decimal to Binary", "Convert decimal to binary.", "dec_to_binary"),
    ("Octal to Decimal", "Convert octal to decimal.", "octal_to_dec"),
    ("Decimal to Octal", "Convert decimal to octal.", "dec_to_octal"),
    ("Hex to Decimal", "Convert hexadecimal to decimal.", "hex_to_dec"),
    ("Decimal to Hex", "Convert decimal to hexadecimal.", "dec_to_hex"),
    ("Power using Recursion", "Calculate power using recursion.", "power_rec"),
    
    # Array Operations
    ("Merge Two Arrays", "Merge two sorted arrays.", "merge_arrays"),
    ("Array Intersection", "Find common elements between two arrays.", "array_intersect"),
    ("Array Union", "Find union of two arrays.", "array_union"),
    ("Array Difference", "Find elements in first array not in second.", "array_diff"),
    ("Remove Duplicates Array", "Remove duplicates from array.", "remove_dup_arr"),
    ("Move Zeros", "Move all zeros to end of array.", "move_zeros"),
    ("Leaders in Array", "Find all leaders (greater than all right elements).", "array_leaders"),
    ("Equilibrium Index", "Find index where left sum equals right sum.", "equilibrium"),
    ("Maximum Subarray Sum", "Find maximum sum of contiguous subarray.", "max_subarray"),
    ("Pair Sum", "Find if any pair sums to target.", "pair_sum"),
    ("Triplet Sum", "Find if any triplet sums to target.", "triplet_sum"),
    ("Peak Element", "Find a peak element in array.", "peak_element"),
    ("Missing Number", "Find missing number in 1 to N.", "missing_num"),
    ("Find Duplicate", "Find duplicate in array of N+1 integers.", "find_dup"),
    ("Majority Element", "Find element appearing more than N/2 times.", "majority"),
    
    # Sorting & Searching
    ("Bubble Sort", "Sort array using bubble sort.", "bubble_sort"),
    ("Selection Sort", "Sort array using selection sort.", "selection_sort"),
    ("Insertion Sort", "Sort array using insertion sort.", "insertion_sort"),
    ("Binary Search", "Implement binary search.", "binary_search"),
    ("First Occurrence", "Find first occurrence in sorted array.", "first_occur"),
    ("Last Occurrence", "Find last occurrence in sorted array.", "last_occur"),
    ("Count Occurrences Sorted", "Count occurrences in sorted array.", "count_occur_sorted"),
    ("Floor in Sorted Array", "Find floor of element in sorted array.", "floor_sorted"),
    ("Ceiling in Sorted Array", "Find ceiling of element in sorted array.", "ceil_sorted"),
    ("K-th Smallest", "Find k-th smallest element.", "kth_smallest"),
    ("K-th Largest", "Find k-th largest element.", "kth_largest"),
    
    # Patterns
    ("Diamond Pattern", "Print diamond pattern of stars.", "diamond"),
    ("Hollow Square", "Print hollow square pattern.", "hollow_square"),
    ("Hollow Triangle", "Print hollow triangle pattern.", "hollow_triangle"),
    ("Pascal's Triangle", "Print first N rows of Pascal's triangle.", "pascal_triangle"),
    ("Floyd's Triangle", "Print Floyd's triangle.", "floyd_triangle"),
    ("Number Pyramid", "Print number pyramid.", "num_pyramid"),
    ("Letter Triangle", "Print triangle with letters.", "letter_triangle"),
    ("Butterfly Pattern", "Print butterfly pattern.", "butterfly"),
    ("Spiral Matrix", "Print numbers in spiral order.", "spiral_matrix"),
    ("Zigzag Pattern", "Print zigzag pattern.", "zigzag"),
    
    # Matrix Operations
    ("Matrix Addition", "Add two matrices.", "matrix_add"),
    ("Matrix Subtraction", "Subtract two matrices.", "matrix_sub"),
    ("Matrix Multiplication", "Multiply two matrices.", "matrix_mul"),
    ("Matrix Transpose", "Transpose a matrix.", "matrix_transpose"),
    ("Row Sum", "Find sum of each row.", "row_sum"),
    ("Column Sum", "Find sum of each column.", "col_sum"),
    ("Diagonal Sum", "Find sum of diagonal elements.", "diagonal_sum"),
    ("Matrix Maximum", "Find maximum element in matrix.", "matrix_max"),
    ("Matrix Minimum", "Find minimum element in matrix.", "matrix_min"),
    ("Rotate Matrix 90", "Rotate matrix 90 degrees clockwise.", "rotate_matrix"),
]

ADVANCED_TOPICS = [
    # Dynamic Programming
    ("Climbing Stairs", "Count ways to climb N stairs (1 or 2 steps).", "climb_stairs"),
    ("Coin Change Min", "Find minimum coins needed for amount.", "coin_change_min"),
    ("Coin Change Ways", "Count ways to make change.", "coin_change_ways"),
    ("Longest Common Subsequence", "Find LCS length of two strings.", "lcs"),
    ("Longest Increasing Subsequence", "Find LIS length.", "lis"),
    ("Edit Distance", "Find minimum edits to convert string.", "edit_dist"),
    ("Knapsack 0/1", "Solve 0/1 knapsack problem.", "knapsack_01"),
    ("Unbounded Knapsack", "Solve unbounded knapsack.", "knapsack_unbound"),
    ("Subset Sum", "Check if subset with given sum exists.", "subset_sum"),
    ("Partition Equal", "Check if array can be partitioned equally.", "partition_equal"),
    ("Rod Cutting", "Maximize profit from rod cutting.", "rod_cutting"),
    ("Matrix Chain", "Find optimal matrix chain multiplication order.", "matrix_chain"),
    ("Palindrome Partitioning", "Min cuts to partition into palindromes.", "palindrome_part"),
    ("Word Break", "Check if string can be segmented into words.", "word_break"),
    ("Longest Palindromic Subsequence", "Find longest palindromic subsequence.", "lps"),
    
    # Graph Algorithms
    ("BFS Traversal", "Implement BFS for graph.", "bfs"),
    ("DFS Traversal", "Implement DFS for graph.", "dfs"),
    ("Detect Cycle Undirected", "Detect cycle in undirected graph.", "cycle_undirected"),
    ("Detect Cycle Directed", "Detect cycle in directed graph.", "cycle_directed"),
    ("Topological Sort", "Find topological order.", "topo_sort"),
    ("Shortest Path Unweighted", "Find shortest path in unweighted graph.", "shortest_unweight"),
    ("Dijkstra's Algorithm", "Find shortest paths from source.", "dijkstra"),
    ("Bellman-Ford", "Find shortest paths with negative edges.", "bellman_ford"),
    ("Floyd-Warshall", "Find all pairs shortest paths.", "floyd_warshall"),
    ("Number of Islands", "Count islands in 2D grid.", "num_islands"),
    ("Connected Components", "Count connected components.", "connected_comp"),
    ("Bipartite Check", "Check if graph is bipartite.", "bipartite"),
    ("Minimum Spanning Tree", "Find MST using Prim's or Kruskal's.", "mst"),
    ("Bridge Edges", "Find bridge edges in graph.", "bridges"),
    ("Articulation Points", "Find articulation points.", "articulation"),
    
    # Trees
    ("Tree Inorder", "Inorder traversal of binary tree.", "tree_inorder"),
    ("Tree Preorder", "Preorder traversal of binary tree.", "tree_preorder"),
    ("Tree Postorder", "Postorder traversal of binary tree.", "tree_postorder"),
    ("Tree Level Order", "Level order traversal.", "tree_level"),
    ("Tree Height", "Find height of binary tree.", "tree_height"),
    ("Tree Diameter", "Find diameter of binary tree.", "tree_diameter"),
    ("Mirror Tree", "Create mirror of binary tree.", "mirror_tree"),
    ("Symmetric Tree", "Check if tree is symmetric.", "symmetric"),
    ("Path Sum", "Check if path with given sum exists.", "path_sum"),
    ("LCA Binary Tree", "Find lowest common ancestor.", "lca"),
    ("BST Insert", "Insert into binary search tree.", "bst_insert"),
    ("BST Search", "Search in binary search tree.", "bst_search"),
    ("BST Delete", "Delete from binary search tree.", "bst_delete"),
    ("Validate BST", "Check if tree is valid BST.", "validate_bst"),
    ("Convert Sorted Array to BST", "Create BST from sorted array.", "arr_to_bst"),
    
    # Linked Lists
    ("Linked List Reverse", "Reverse a linked list.", "ll_reverse"),
    ("Linked List Middle", "Find middle of linked list.", "ll_middle"),
    ("Linked List Cycle", "Detect cycle in linked list.", "ll_cycle"),
    ("Linked List Merge", "Merge two sorted linked lists.", "ll_merge"),
    ("Remove Nth from End", "Remove nth node from end.", "ll_remove_nth"),
    ("Linked List Palindrome", "Check if linked list is palindrome.", "ll_palindrome"),
    ("Intersection Point", "Find intersection of two linked lists.", "ll_intersect"),
    ("Flatten Linked List", "Flatten multilevel linked list.", "ll_flatten"),
    ("Add Two Numbers", "Add numbers represented as linked lists.", "ll_add"),
    ("Rotate Linked List", "Rotate linked list by k.", "ll_rotate"),
    
    # Stacks and Queues
    ("Stack using Queue", "Implement stack using queues.", "stack_queue"),
    ("Queue using Stack", "Implement queue using stacks.", "queue_stack"),
    ("Min Stack", "Stack with O(1) min operation.", "min_stack"),
    ("Next Greater Element", "Find next greater for each element.", "nge"),
    ("Stock Span", "Calculate stock span for each day.", "stock_span"),
    ("Largest Rectangle Histogram", "Find largest rectangle in histogram.", "largest_rect"),
    ("Sliding Window Maximum", "Find max in each sliding window.", "sliding_max"),
    ("Evaluate Postfix", "Evaluate postfix expression.", "eval_postfix"),
    ("Infix to Postfix", "Convert infix to postfix.", "infix_postfix"),
    ("Valid Expression", "Check if expression is valid.", "valid_expr"),
    
    # Backtracking
    ("N-Queens", "Solve N-Queens problem.", "n_queens"),
    ("Sudoku Solver", "Solve Sudoku puzzle.", "sudoku"),
    ("Rat in Maze", "Find path in maze.", "rat_maze"),
    ("Subset Generation", "Generate all subsets.", "subsets"),
    ("Permutations", "Generate all permutations.", "permutations"),
    ("Combinations", "Generate all combinations of size k.", "combinations"),
    ("Letter Combinations", "Phone number letter combinations.", "phone_letters"),
    ("Word Search", "Find word in 2D grid.", "word_search"),
    ("Palindrome Partitioning All", "Find all palindrome partitions.", "palindrome_all"),
    ("Knight's Tour", "Find valid knight's tour.", "knight_tour"),
]

PRO_TOPICS = [
    # Advanced DP
    ("Longest Common Substring", "Find longest common substring.", "longest_common_substr"),
    ("Longest Repeating Subsequence", "Find longest repeating subsequence.", "lrs"),
    ("Shortest Common Supersequence", "Find shortest common supersequence.", "scs"),
    ("Count Distinct Subsequences", "Count distinct subsequences of pattern.", "count_subseq"),
    ("Wildcard Matching", "Implement wildcard pattern matching.", "wildcard"),
    ("Regular Expression Match", "Implement regex matching.", "regex_match"),
    ("Interleaving String", "Check if C is interleaving of A and B.", "interleave"),
    ("Distinct Paths", "Count distinct paths in grid.", "distinct_paths"),
    ("Minimum Path Sum", "Find minimum path sum in grid.", "min_path_sum"),
    ("Maximum Path Sum", "Find maximum path sum in triangle.", "max_path_sum"),
    ("Burst Balloons", "Maximum coins from bursting balloons.", "burst_balloons"),
    ("Egg Drop Problem", "Minimum trials to find critical floor.", "egg_drop"),
    ("Optimal BST", "Find cost of optimal BST.", "optimal_bst"),
    ("Boolean Parenthesization", "Ways to parenthesize expression to get True.", "bool_parens"),
    ("Painting Fence", "Ways to paint fence with k colors.", "paint_fence"),
    
    # Advanced Graphs
    ("Kosaraju's Algorithm", "Find strongly connected components.", "kosaraju"),
    ("Tarjan's Algorithm", "Find SCCs using Tarjan's.", "tarjan"),
    ("Eulerian Path", "Find Eulerian path if exists.", "euler_path"),
    ("Hamiltonian Path", "Find Hamiltonian path if exists.", "hamilton_path"),
    ("Graph Coloring", "Check if graph is k-colorable.", "graph_color"),
    ("Max Flow", "Find maximum flow in network.", "max_flow"),
    ("Min Cut", "Find minimum cut in graph.", "min_cut"),
    ("Bipartite Matching", "Find maximum bipartite matching.", "bipartite_match"),
    ("Cheapest Flights", "Find cheapest flight with k stops.", "cheapest_flight"),
    ("Network Delay", "Calculate network delay time.", "network_delay"),
    ("Course Schedule", "Check if courses can be completed.", "course_schedule"),
    ("Alien Dictionary", "Find character order in alien language.", "alien_dict"),
    ("Word Ladder", "Find shortest transformation sequence.", "word_ladder"),
    ("Clone Graph", "Deep clone a graph.", "clone_graph"),
    ("Reconstruct Itinerary", "Reconstruct valid itinerary.", "itinerary"),
    
    # Advanced Trees
    ("Serialize Tree", "Serialize and deserialize binary tree.", "serialize"),
    ("Tree from Traversals", "Build tree from inorder and preorder.", "tree_from_trav"),
    ("Vertical Order Traversal", "Print tree in vertical order.", "vertical_order"),
    ("Boundary Traversal", "Print boundary of binary tree.", "boundary"),
    ("Maximum Width", "Find maximum width of binary tree.", "max_width"),
    ("Burn Tree", "Find time to burn entire tree from node.", "burn_tree"),
    ("Two Sum BST", "Find if two nodes sum to target.", "two_sum_bst"),
    ("Kth Largest BST", "Find kth largest in BST.", "kth_largest_bst"),
    ("Recover BST", "Recover BST with two swapped nodes.", "recover_bst"),
    ("Flatten to Linked List", "Flatten tree to linked list.", "flatten_tree"),
    
    # Segment Trees & BIT
    ("Segment Tree Build", "Build segment tree for range sum.", "seg_build"),
    ("Segment Tree Query", "Range sum query.", "seg_query"),
    ("Segment Tree Update", "Point update in segment tree.", "seg_update"),
    ("Range Minimum Query", "Range minimum using segment tree.", "rmq"),
    ("Binary Indexed Tree", "Implement BIT for prefix sum.", "bit"),
    ("Count Inversions", "Count inversions using BIT.", "count_inv"),
    ("Range Updates", "Lazy propagation for range updates.", "lazy_prop"),
    
    # Tries
    ("Trie Insert Search", "Implement Trie operations.", "trie_basic"),
    ("Prefix Search", "Count words with given prefix.", "prefix_count"),
    ("Word Dictionary", "Add and search with wildcards.", "word_dict"),
    ("Maximum XOR", "Find maximum XOR of two numbers.", "max_xor"),
    ("Word Suggestions", "Suggest words based on prefix.", "word_suggest"),
    
    # Advanced String Algorithms
    ("KMP Pattern Match", "Implement KMP algorithm.", "kmp"),
    ("Rabin-Karp", "Implement Rabin-Karp algorithm.", "rabin_karp"),
    ("Z Algorithm", "Implement Z algorithm.", "z_algo"),
    ("Manacher's Algorithm", "Find longest palindromic substring.", "manacher"),
    ("Suffix Array", "Build suffix array.", "suffix_arr"),
    ("Longest Repeated Substring", "Find longest repeated substring.", "long_repeat"),
    
    # Bit Manipulation
    ("Count Set Bits", "Count number of 1s in binary.", "count_bits"),
    ("Power of Two", "Check if number is power of 2.", "power_two"),
    ("Single Number II", "Find single number (others appear 3 times).", "single_num_ii"),
    ("Single Number III", "Find two single numbers.", "single_num_iii"),
    ("Maximum AND", "Find maximum AND of any pair.", "max_and"),
    ("Subset XOR", "Find maximum XOR of any subset.", "subset_xor"),
    ("Reverse Bits", "Reverse bits of a number.", "reverse_bits"),
    ("Next Higher Same Bits", "Find next number with same set bits.", "next_higher"),
    
    # Advanced Array
    ("Median of Two Sorted", "Find median of two sorted arrays.", "median_sorted"),
    ("Trapping Rain Water", "Calculate trapped rain water.", "trap_water"),
    ("Container With Water", "Find container with most water.", "container_water"),
    ("Candy Distribution", "Minimum candies for rating distribution.", "candy"),
    ("Jump Game", "Check if can reach last index.", "jump_game"),
    ("Jump Game II", "Minimum jumps to reach end.", "jump_game_ii"),
    ("Gas Station", "Find starting station for circuit.", "gas_station"),
    ("First Missing Positive", "Find first missing positive.", "first_missing"),
    ("Longest Consecutive", "Find longest consecutive sequence.", "longest_consec"),
    
    # Heap/Priority Queue
    ("Kth Largest Stream", "Kth largest element in stream.", "kth_stream"),
    ("Merge K Sorted Lists", "Merge k sorted linked lists.", "merge_k"),
    ("Find Median Stream", "Find median from data stream.", "median_stream"),
    ("Top K Frequent", "Find k most frequent elements.", "top_k_freq"),
    ("K Closest Points", "Find k closest points to origin.", "k_closest"),
    ("Reorganize String", "Rearrange string so no adjacent same.", "reorganize"),
    ("Task Scheduler", "Minimum time to complete tasks.", "task_scheduler"),
]

def generate_starter_code(topic_id, difficulty):
    """Generate starter code for each language"""
    return {
        "python": f"# {topic_id} - Write your solution below\n",
        "java": f"import java.util.Scanner;\n\npublic class Solution {{\n    public static void main(String[] args) {{\n        Scanner sc = new Scanner(System.in);\n        // {topic_id} - Your code here\n    }}\n}}",
        "c": f"#include <stdio.h>\n\nint main() {{\n    // {topic_id} - Your code here\n    return 0;\n}}",
        "cpp": f"#include <iostream>\nusing namespace std;\n\nint main() {{\n    // {topic_id} - Your code here\n    return 0;\n}}"
    }

def generate_solution_placeholder(topic_id, difficulty):
    """Generate placeholder solution for each language"""
    return {
        "python": f"# Solution for {topic_id}\n# Implementation depends on specific problem",
        "java": f"// Solution for {topic_id}",
        "c": f"// Solution for {topic_id}",
        "cpp": f"// Solution for {topic_id}"
    }

def generate_test_cases(topic_id):
    """Generate sample test cases"""
    return [
        {"input": "5", "output": "Expected output 1"},
        {"input": "10", "output": "Expected output 2"},
        {"input": "1", "output": "Expected output 3"}
    ]

def generate_problems_for_level(topics, difficulty_code, start_id=1):
    """Generate problems for a difficulty level"""
    problems = []
    real_life_contexts = {
        "BEG": [
            "This skill is fundamental for building any software application.",
            "Understanding this concept helps in everyday calculations and data analysis.",
            "This is commonly used in form validation and user input processing.",
            "Essential for creating interactive applications and games.",
            "Used extensively in data processing and file handling."
        ],
        "INT": [
            "This optimization technique is used in production systems at scale.",
            "Understanding this helps in building efficient search engines.",
            "Critical for data structures used in databases and file systems.",
            "Used in competitive programming and technical interviews.",
            "Essential for building scalable web applications."
        ],
        "ADV": [
            "This algorithm is used by tech giants like Google and Facebook.",
            "Critical for machine learning and AI applications.",
            "Used in network routing and GPS navigation systems.",
            "Essential for building recommendation systems.",
            "Used in financial modeling and risk analysis."
        ],
        "PRO": [
            "Used in designing distributed systems at scale.",
            "Critical for real-time streaming applications.",
            "Essential for building high-frequency trading systems.",
            "Used in cryptographic applications and security systems.",
            "Fundamental for compiler optimization and code generation."
        ]
    }
    
    explanations = {
        "BEG": "This problem teaches fundamental programming concepts. Start by understanding the input format, then implement step by step.",
        "INT": "This problem requires combining multiple concepts. Think about edge cases and optimize your solution.",
        "ADV": "This problem requires deep understanding of algorithms and data structures. Consider time and space complexity.",
        "PRO": "This is a challenging problem that tests advanced problem-solving skills. Consider multiple approaches before implementing."
    }
    
    problem_id = start_id
    
    # Generate variations for each topic to reach 250 problems
    variations_needed = 250 // len(topics) + 1
    
    for topic_idx, (title_template, desc, topic_id) in enumerate(topics):
        for variant in range(variations_needed):
            if len(problems) >= 250:
                break
                
            # Create variations by changing parameters
            if "{n}" in title_template:
                n_values = [3, 4, 5, 6, 7, 8, 10]
                n = n_values[variant % len(n_values)]
                title = title_template.format(n=n)
                description = desc.format(n=n)
            else:
                if variant == 0:
                    title = title_template
                    description = desc
                else:
                    title = f"{title_template} (Variant {variant + 1})"
                    description = f"{desc} (with modified constraints)"
            
            problem = {
                "title": title,
                "description": f"{description}\n\nRead input from stdin and print output to stdout.",
                "explanation": explanations[difficulty_code],
                "real_life_context": real_life_contexts[difficulty_code][problem_id % len(real_life_contexts[difficulty_code])],
                "starter_code": generate_starter_code(topic_id, difficulty_code),
                "solutions": generate_solution_placeholder(topic_id, difficulty_code),
                "test_cases": generate_test_cases(topic_id)
            }
            
            problems.append(problem)
            problem_id += 1
    
    return problems[:250]  # Ensure exactly 250 problems

def main():
    """Generate all problem files"""
    output_dir = r"c:\Users\malia\OneDrive\Desktop\DevSutra\challenges\data"
    
    levels = [
        ("problems_beginner.json", BEGINNER_TOPICS, "BEG"),
        ("problems_intermediate.json", INTERMEDIATE_TOPICS, "INT"),
        ("problems_advanced.json", ADVANCED_TOPICS, "ADV"),
        ("problems_pro.json", PRO_TOPICS, "PRO"),
    ]
    
    for filename, topics, difficulty in levels:
        print(f"Generating {filename}...")
        problems = generate_problems_for_level(topics, difficulty)
        
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(problems, f, indent=4, ensure_ascii=False)
        
        print(f"  Generated {len(problems)} problems for {difficulty}")
    
    print("\nDone! All problem files generated.")

if __name__ == "__main__":
    main()
