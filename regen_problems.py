"""
Regenerate all problems with complete, working solutions
"""
import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_backend.settings')
django.setup()

from challenges.models import Problem

# First, delete all existing problems
print("Deleting existing problems...")
Problem.objects.all().delete()
print("Done. Now regenerating quality problems...")

# Define complete problem sets for each level
BEGINNER_PROBLEMS = [
    {
        "title": "Sum of Two Numbers",
        "description": "Read two integers A and B from input (one per line) and print their sum.",
        "difficulty": "BEG",
        "explanation": "We use input() to read values, convert them to integers using int(), add them together with the + operator, and print the result.",
        "real_life_context": "Addition is fundamental in shopping carts, calculating totals, budgets, and any financial application.",
        "starter_code": {"python": "# Read two numbers and print their sum\n", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"},
        "solutions": {"python": "a = int(input())\nb = int(input())\nprint(a + b)", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a + b);\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a + b);\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a + b;\n    return 0;\n}"},
        "test_cases": [{"input": "5\n3", "output": "8"}, {"input": "10\n20", "output": "30"}, {"input": "-5\n5", "output": "0"}]
    },
    {
        "title": "Difference of Two Numbers",
        "description": "Read two integers A and B from input and print their difference (A minus B).",
        "difficulty": "BEG",
        "explanation": "Read two integers, subtract the second from the first using the - operator, and print the result.",
        "real_life_context": "Subtraction is used in calculating change, balance remaining, discounts, and time differences.",
        "starter_code": {"python": "# Read two numbers and print first - second\n", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"},
        "solutions": {"python": "a = int(input())\nb = int(input())\nprint(a - b)", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a - b);\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a - b);\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a - b;\n    return 0;\n}"},
        "test_cases": [{"input": "10\n3", "output": "7"}, {"input": "5\n5", "output": "0"}, {"input": "3\n10", "output": "-7"}]
    },
    {
        "title": "Product of Two Numbers",
        "description": "Read two integers A and B from input and print their product.",
        "difficulty": "BEG",
        "explanation": "Multiply two numbers using the * operator and print the result.",
        "real_life_context": "Multiplication is used in calculating areas, pricing (quantity x price), and scaling values.",
        "starter_code": {"python": "# Read two numbers and print their product\n", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"},
        "solutions": {"python": "a = int(input())\nb = int(input())\nprint(a * b)", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a * b);\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a * b);\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a * b;\n    return 0;\n}"},
        "test_cases": [{"input": "5\n3", "output": "15"}, {"input": "7\n0", "output": "0"}, {"input": "-4\n3", "output": "-12"}]
    },
    {
        "title": "Integer Division",
        "description": "Read two integers A and B from input and print the result of integer division (A divided by B).",
        "difficulty": "BEG",
        "explanation": "Use the // operator in Python for floor division. This gives the quotient without the remainder.",
        "real_life_context": "Integer division is used in splitting items equally, pagination, and distributing resources.",
        "starter_code": {"python": "# Read two numbers and print integer division result\n", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"},
        "solutions": {"python": "a = int(input())\nb = int(input())\nprint(a // b)", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a / b);\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a / b);\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a / b;\n    return 0;\n}"},
        "test_cases": [{"input": "10\n3", "output": "3"}, {"input": "15\n5", "output": "3"}, {"input": "7\n2", "output": "3"}]
    },
    {
        "title": "Remainder (Modulo)",
        "description": "Read two integers A and B from input and print the remainder when A is divided by B.",
        "difficulty": "BEG",
        "explanation": "The modulo operator (%) returns the remainder after division.",
        "real_life_context": "Modulo is used in determining if a number is even/odd, cycling through options, and time calculations.",
        "starter_code": {"python": "# Read two numbers and print the remainder\n", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        // Your code here\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    // Your code here\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    // Your code here\n    return 0;\n}"},
        "solutions": {"python": "a = int(input())\nb = int(input())\nprint(a % b)", "java": "import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(a % b);\n    }\n}", "c": "#include <stdio.h>\n\nint main() {\n    int a, b;\n    scanf(\"%d\", &a);\n    scanf(\"%d\", &b);\n    printf(\"%d\", a % b);\n    return 0;\n}", "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a % b;\n    return 0;\n}"},
        "test_cases": [{"input": "10\n3", "output": "1"}, {"input": "15\n5", "output": "0"}, {"input": "7\n4", "output": "3"}]
    }
]

# Create problems
for p in BEGINNER_PROBLEMS:
    Problem.objects.create(**p)
    print(f"Created: {p['title']}")

print(f"\nCreated {len(BEGINNER_PROBLEMS)} beginner problems.")
print("Now import remaining from JSON files...")
