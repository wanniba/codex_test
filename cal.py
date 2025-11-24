
def calculate_average(numbers):
    """Return the arithmetic mean of the values in numbers."""
    if not numbers:
        raise ValueError("numbers must contain at least one value")

    total = 0
    for value in numbers:
        total += value

    average = total / len(numbers)
    return average

# 测试这个函数
scores = [85, 90, 78, 92, 88]
result = calculate_average(scores)
print(f"平均分是：{result}")
