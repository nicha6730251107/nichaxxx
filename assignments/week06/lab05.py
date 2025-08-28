""" เขียน function ชื่อ count_vowels_consonants ที่มีคุณสมบัติดังนี้:

รับ parameter text เป็น string
นับสระ (a, e, i, o, u) และพยัญชนะ (ไม่นับช่องว่างและตัวเลข)
return dictionary ที่มี vowels และ consonants counts
ไม่สนใจตัวใหญ่ตัวเล็ก (case insensitive) """

def count_vowels_consonants(text):
    text = text.repace("","")
    text = text.lower()
    vowels = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    numbers =text.count('1') + text.count('2') + text.count('3') + text.count('4') + text.count('5') + text.count('6') + text.count('7') + text.count('8') + text.count('9')
    consonants = len(text) + vowels - numbers

    return {
        "vowels": vowels,
        "consonants": consonants
    }


# =============================================================================
# TEST SECTION - DO NOT MODIFY
# =============================================================================

def run_all_tests():
    """Test all functions and display results"""
    print("="*50)
    print("PYTHON FUNCTIONS QUIZ - TEST RESULTS")
    print("="*50)
    
    # Test Problem 1
    print("\n--- Problem 1 Tests ---")
    try:
        result1 = welcome_message("Alice", "Python")
        print(f"Test 1: {result1}")
        result2 = welcome_message("Bob", "Data Science")
        print(f"Test 2: {result2}")
        print("✓ Problem 1: PASSED")
    except Exception as e:
        print(f"✗ Problem 1: ERROR - {e}")
    
    # Test Problem 2
    print("\n--- Problem 2 Tests ---")
    try:
        result1 = calculate_circle(5)
        print(f"Test 1: {result1}")
        result2 = calculate_circle(3)
        print(f"Test 2: {result2}")
        print("✓ Problem 2: PASSED")
    except Exception as e:
        print(f"✗ Problem 2: ERROR - {e}")
    
    # Test Problem 3
    print("\n--- Problem 3 Tests ---")
    try:
        result1 = create_user_profile("john_doe")
        print(f"Test 1: {result1}")
        result2 = create_user_profile("alice", 25)
        print(f"Test 2: {result2}")
        result3 = create_user_profile("bob", 30, True)
        print(f"Test 3: {result3}")
        print("✓ Problem 3: PASSED")
    except Exception as e:
        print(f"✗ Problem 3: ERROR - {e}")
    
    # Test Problem 4
    print("\n--- Problem 4 Tests ---")
    try:
        scores1 = [85, 92, 78, 65, 88, 76, 95]
        result1 = analyze_scores(scores1)
        print(f"Test 1: {result1}")
        scores2 = [45, 67, 89, 72, 58]
        result2 = analyze_scores(scores2)
        print(f"Test 2: {result2}")
        print("✓ Problem 4: PASSED")
    except Exception as e:
        print(f"✗ Problem 4: ERROR - {e}")
    
    # Test Problem 5
    print("\n--- Problem 5 Tests ---")
    try:
        result1 = count_vowels_consonants("Hello World")
        print(f"Test 1: {result1}")
        result2 = count_vowels_consonants("Python Programming 2024")
        print(f"Test 2: {result2}")
        print("✓ Problem 5: PASSED")
    except Exception as e:
        print(f"✗ Problem 5: ERROR - {e}")
    
    print("\n" + "="*50)
    print("END OF TESTS")
    print("="*50)

# Run the tests
if __name__ == "__main__":
    run_all_tests()