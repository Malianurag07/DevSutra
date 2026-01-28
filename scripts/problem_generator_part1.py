"""
Quality Problem Generator for DevSutra
Generates unique problems with complete solutions, explanations, and real-life context
"""
import json
import os

def create_beginner_problems():
    """Create 250 unique beginner problems with complete solutions"""
    problems = []
    
    # Category 1: Basic Arithmetic (50 problems)
    arithmetic_problems = [
        {
            "title": "Sum of Two Numbers",
            "description": "Read two integers A and B from input (one per line) and print their sum.",
            "explanation": "We use input() to read values, convert them to integers using int(), add them together with the + operator, and print the result. This demonstrates basic input/output operations.",
            "real_life_context": "Addition is fundamental in shopping carts, calculating totals, budgets, and any financial application where you need to combine values.",
            "starter_code": {
                "python": "# Read two numbers and print their sum\na = int(input())\nb = int(input())\n# Write your code here\n",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        // Write your code here\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    // Write your code here\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    // Write your code here\n    return 0;\n}"
            },
            "solutions": {
                "python": "a = int(input())\nb = int(input())\nprint(a + b)",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a + b);\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a + b);\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a + b;\n    return 0;\n}"
            },
            "test_cases": [
                {"input": "5\n3", "output": "8"},
                {"input": "10\n20", "output": "30"},
                {"input": "-5\n5", "output": "0"}
            ]
        },
        {
            "title": "Grocery Shopping Total",
            "description": "You are tasked with calculating the total cost of a small grocery order. You buy two types of items: apples and oranges.\n\n- Apples cost $2 each.\n- Oranges cost $3 each.\n\nAdditionally, there is a fixed shipping fee of $5 for the entire order.\n\nYour program will receive two lines of input: the quantity of apples (A), followed by the quantity of oranges (O). Calculate and print the final total cost as a single integer.",
            "explanation": "We multiply the quantity of each item by its price, add them together, and add the shipping fee. Formula: Total = (A * 2) + (O * 3) + 5",
            "real_life_context": "Calculating the total price based on itemized costs, quantities, and fixed fees (like sales tax or shipping) is a fundamental skill in finance, e-commerce, and logistics. This problem models a simple checkout process.",
            "starter_code": {
                "python": "# Read the quantity of apples (A) first, then oranges (O).\n# Write your code here\n# Use input() and print()",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"
            },
            "solutions": {
                "python": "a = int(input())\no = int(input())\nprint(a * 2 + o * 3 + 5)",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int o = sc.nextInt();\n        System.out.println(a * 2 + o * 3 + 5);\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    int a, o;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &o);\n    printf(\"%d\", a * 2 + o * 3 + 5);\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, o;\n    cin >> a >> o;\n    cout << a * 2 + o * 3 + 5;\n    return 0;\n}"
            },
            "test_cases": [
                {"input": "1\n1", "output": "10"},
                {"input": "5\n10", "output": "45"},
                {"input": "0\n0", "output": "5"}
            ]
        },
        {
            "title": "Difference of Two Numbers",
            "description": "Read two integers A and B from input and print their difference (A minus B).",
            "explanation": "Read two integers, subtract the second from the first using the - operator, and print the result. The order matters in subtraction.",
            "real_life_context": "Subtraction is used in calculating change, balance remaining, discounts, profit/loss calculations, and time differences.",
            "starter_code": {
                "python": "# Read two numbers and print first - second\n",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"
            },
            "solutions": {
                "python": "a = int(input())\nb = int(input())\nprint(a - b)",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a - b);\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a - b);\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a - b;\n    return 0;\n}"
            },
            "test_cases": [
                {"input": "10\n3", "output": "7"},
                {"input": "5\n5", "output": "0"},
                {"input": "3\n10", "output": "-7"}
            ]
        },
        {
            "title": "Product of Two Numbers",
            "description": "Read two integers A and B from input and print their product (A multiplied by B).",
            "explanation": "Multiply two numbers using the * operator and print the result. Multiplication is commutative, so A*B equals B*A.",
            "real_life_context": "Multiplication is used in calculating areas, pricing (quantity x price), scaling values, compound calculations, and unit conversions.",
            "starter_code": {
                "python": "# Read two numbers and print their product\n",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"
            },
            "solutions": {
                "python": "a = int(input())\nb = int(input())\nprint(a * b)",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a * b);\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a * b);\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a * b;\n    return 0;\n}"
            },
            "test_cases": [
                {"input": "5\n3", "output": "15"},
                {"input": "7\n0", "output": "0"},
                {"input": "-4\n3", "output": "-12"}
            ]
        },
        {
            "title": "Integer Division",
            "description": "Read two integers A and B from input and print the result of integer division (A divided by B, ignoring remainder).",
            "explanation": "Use the // operator in Python for floor division. This gives the quotient without the remainder. In C/C++/Java, integer division with / automatically truncates.",
            "real_life_context": "Integer division is used in splitting items equally, pagination (items per page), distributing resources, and time calculations (hours from minutes).",
            "starter_code": {
                "python": "# Read two numbers and print integer division result\n",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"
            },
            "solutions": {
                "python": "a = int(input())\nb = int(input())\nprint(a // b)",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a / b);\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a / b);\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a / b;\n    return 0;\n}"
            },
            "test_cases": [
                {"input": "10\n3", "output": "3"},
                {"input": "15\n5", "output": "3"},
                {"input": "7\n2", "output": "3"}
            ]
        },
        {
            "title": "Remainder (Modulo)",
            "description": "Read two integers A and B from input and print the remainder when A is divided by B.",
            "explanation": "The modulo operator (%) returns the remainder after division. For example, 10 % 3 = 1 because 10 = 3*3 + 1.",
            "real_life_context": "Modulo is used in determining if a number is even/odd, cycling through options, time calculations (minutes from total seconds), and cryptography.",
            "starter_code": {
                "python": "# Read two numbers and print the remainder\n",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"
            },
            "solutions": {
                "python": "a = int(input())\nb = int(input())\nprint(a % b)",
                "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a % b);\n    }\n}",
                "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a % b);\n    return 0;\n}",
                "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a % b;\n    return 0;\n}"
            },
            "test_cases": [
                {"input": "10\n3", "output": "1"},
                {"input": "15\n5", "output": "0"},
                {"input": "7\n4", "output": "3"}
            ]
        }
    ]
    
    problems.extend(arithmetic_problems)
    
    # Will continue with more categories...
    return problems

# Main execution will be in part 2
if __name__ == "__main__":
    print("Part 1 loaded - contains base structure")
