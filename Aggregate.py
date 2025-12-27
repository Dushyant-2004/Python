# ============================================
# MATHEMATICAL & AGGREGATE FUNCTIONS IN PYTHON
# Complete Guide with Examples
# ============================================

import math
import statistics

# ============================================
# 1. BASIC AGGREGATE FUNCTIONS (Built-in)
# ============================================
print("=" * 60)
print("1. BASIC AGGREGATE FUNCTIONS")
print("=" * 60)

numbers = [15, 22, 8, 45, 30, 12, 38, 25, 10, 50]
print(f"Data: {numbers}\n")

# sum() - Total of all elements
print(f"Sum: {sum(numbers)}")                    # Output: 255

# min() - Smallest element
print(f"Minimum: {min(numbers)}")                # Output: 8

# max() - Largest element
print(f"Maximum: {max(numbers)}")                # Output: 50

# len() - Count of elements
print(f"Count: {len(numbers)}")                  # Output: 10

# ============================================
# 2. MEAN (Average)
# ============================================
print("\n" + "=" * 60)
print("2. MEAN (AVERAGE)")
print("=" * 60)
"""
MEAN = Sum of all values / Number of values
Formula: μ = Σx / n

Types of Mean:
1. Arithmetic Mean - Simple average
2. Geometric Mean - For growth rates
3. Harmonic Mean - For rates and ratios
"""

data = [10, 20, 30, 40, 50]
print(f"Data: {data}\n")

# Method 1: Manual calculation
arithmetic_mean = sum(data) / len(data)
print(f"Arithmetic Mean (manual): {arithmetic_mean}")

# Method 2: Using statistics module
print(f"Arithmetic Mean (statistics): {statistics.mean(data)}")

# Geometric Mean - Used for growth rates, returns nth root of product
print(f"Geometric Mean: {statistics.geometric_mean(data):.2f}")

# Harmonic Mean - Used for averaging rates
print(f"Harmonic Mean: {statistics.harmonic_mean(data):.2f}")

# ============================================
# 3. MEDIAN (Middle Value)
# ============================================
print("\n" + "=" * 60)
print("3. MEDIAN (MIDDLE VALUE)")
print("=" * 60)
"""
MEDIAN = Middle value when data is sorted

For ODD count: Middle element
For EVEN count: Average of two middle elements

WHY MEDIAN?
- Not affected by outliers (extreme values)
- Better for skewed distributions
"""

# Odd number of elements
odd_data = [12, 5, 22, 30, 18]
sorted_odd = sorted(odd_data)
print(f"Odd Data: {odd_data}")
print(f"Sorted: {sorted_odd}")
print(f"Median: {statistics.median(odd_data)}")  # Output: 18

# Even number of elements
even_data = [12, 5, 22, 30, 18, 25]
sorted_even = sorted(even_data)
print(f"\nEven Data: {even_data}")
print(f"Sorted: {sorted_even}")
print(f"Median: {statistics.median(even_data)}") # Output: (18+22)/2 = 20

# Median vs Mean with outliers
outlier_data = [10, 12, 14, 15, 100]  # 100 is an outlier
print(f"\nData with outlier: {outlier_data}")
print(f"Mean: {statistics.mean(outlier_data)}")     # Affected by outlier
print(f"Median: {statistics.median(outlier_data)}") # Not affected

# ============================================
# 4. MODE (Most Frequent Value)
# ============================================
print("\n" + "=" * 60)
print("4. MODE (MOST FREQUENT)")
print("=" * 60)
"""
MODE = Value that appears most frequently
"""

mode_data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(f"Data: {mode_data}")
print(f"Mode: {statistics.mode(mode_data)}")           # Output: 3
print(f"All Modes: {statistics.multimode(mode_data)}") # For multiple modes

# ============================================
# 5. VARIANCE & STANDARD DEVIATION
# ============================================
print("\n" + "=" * 60)
print("5. VARIANCE & STANDARD DEVIATION")
print("=" * 60)
"""
VARIANCE = Average of squared differences from mean
Formula: σ² = Σ(x - μ)² / n

STANDARD DEVIATION = Square root of variance
Formula: σ = √variance

WHY IMPORTANT?
- Measures spread/dispersion of data
- Low SD = data points close to mean
- High SD = data points spread out
"""

scores = [85, 90, 78, 92, 88]
print(f"Scores: {scores}")
print(f"Mean: {statistics.mean(scores)}")

# Population variance & SD (when you have ALL data)
print(f"\nPopulation Variance: {statistics.pvariance(scores):.2f}")
print(f"Population Std Dev: {statistics.pstdev(scores):.2f}")

# Sample variance & SD (when you have a SAMPLE of data)
print(f"\nSample Variance: {statistics.variance(scores):.2f}")
print(f"Sample Std Dev: {statistics.stdev(scores):.2f}")

# ============================================
# 6. VECTOR NORMALIZATION
# ============================================
print("\n" + "=" * 60)
print("6. VECTOR NORMALIZATION")
print("=" * 60)
"""
VECTOR NORMALIZATION = Converting a vector to unit vector (length = 1)
Formula: normalized_vector = vector / magnitude

MAGNITUDE (Length) = √(x² + y² + z²)

WHY NORMALIZE?
1. Machine Learning - Feature scaling
2. Graphics - Direction without magnitude
3. Comparing vectors of different scales
4. Neural Networks - Prevents gradient explosion
"""

# 2D Vector Normalization
vector_2d = [3, 4]
magnitude_2d = math.sqrt(sum(x**2 for x in vector_2d))
normalized_2d = [x / magnitude_2d for x in vector_2d]

print(f"2D Vector: {vector_2d}")
print(f"Magnitude: {magnitude_2d}")
print(f"Normalized: {normalized_2d}")
print(f"Verify (length should be 1): {math.sqrt(sum(x**2 for x in normalized_2d)):.4f}")

# 3D Vector Normalization
vector_3d = [1, 2, 2]
magnitude_3d = math.sqrt(sum(x**2 for x in vector_3d))
normalized_3d = [x / magnitude_3d for x in vector_3d]

print(f"\n3D Vector: {vector_3d}")
print(f"Magnitude: {magnitude_3d}")
print(f"Normalized: [{normalized_3d[0]:.4f}, {normalized_3d[1]:.4f}, {normalized_3d[2]:.4f}]")

# ============================================
# 7. OTHER IMPORTANT MATH FUNCTIONS
# ============================================
print("\n" + "=" * 60)
print("7. IMPORTANT MATH FUNCTIONS")
print("=" * 60)

x = 16
y = -5.7
z = 2.5

print(f"Values: x={x}, y={y}, z={z}\n")

# Square root
print(f"sqrt({x}) = {math.sqrt(x)}")

# Power
print(f"pow(2, 3) = {math.pow(2, 3)}")  # 2³ = 8

# Absolute value
print(f"abs({y}) = {abs(y)}")
print(f"fabs({y}) = {math.fabs(y)}")

# Floor (round down) and Ceil (round up)
print(f"floor({z}) = {math.floor(z)}")   # 2
print(f"ceil({z}) = {math.ceil(z)}")     # 3

# Round
print(f"round({z}) = {round(z)}")
print(f"round(2.567, 2) = {round(2.567, 2)}")  # 2 decimal places

# Factorial
print(f"factorial(5) = {math.factorial(5)}")  # 5! = 120

# GCD (Greatest Common Divisor)
print(f"gcd(48, 18) = {math.gcd(48, 18)}")    # 6

# LCM (Least Common Multiple) - Python 3.9+
print(f"lcm(4, 6) = {math.lcm(4, 6)}")        # 12

# Logarithms
print(f"\nlog(100, 10) = {math.log(100, 10)}")  # log base 10
print(f"log10(100) = {math.log10(100)}")
print(f"log2(8) = {math.log2(8)}")
print(f"ln(e) = {math.log(math.e)}")           # natural log

# Exponential
print(f"exp(2) = {math.exp(2):.4f}")           # e²

# ============================================
# 8. TRIGONOMETRIC FUNCTIONS
# ============================================
print("\n" + "=" * 60)
print("8. TRIGONOMETRIC FUNCTIONS")
print("=" * 60)

angle_deg = 45
angle_rad = math.radians(angle_deg)  # Convert to radians

print(f"Angle: {angle_deg}° = {angle_rad:.4f} radians\n")

print(f"sin({angle_deg}°) = {math.sin(angle_rad):.4f}")
print(f"cos({angle_deg}°) = {math.cos(angle_rad):.4f}")
print(f"tan({angle_deg}°) = {math.tan(angle_rad):.4f}")

# Inverse trigonometric
print(f"\nasin(0.5) = {math.degrees(math.asin(0.5)):.2f}°")
print(f"acos(0.5) = {math.degrees(math.acos(0.5)):.2f}°")
print(f"atan(1) = {math.degrees(math.atan(1)):.2f}°")

# ============================================
# 9. MATHEMATICAL CONSTANTS
# ============================================
print("\n" + "=" * 60)
print("9. MATHEMATICAL CONSTANTS")
print("=" * 60)

print(f"π (pi) = {math.pi}")
print(f"e (Euler's number) = {math.e}")
print(f"τ (tau = 2π) = {math.tau}")
print(f"∞ (infinity) = {math.inf}")
print(f"NaN (Not a Number) = {math.nan}")

# ============================================
# 10. DATA NORMALIZATION TECHNIQUES
# ============================================
print("\n" + "=" * 60)
print("10. DATA NORMALIZATION (Machine Learning)")
print("=" * 60)
"""
WHY NORMALIZE DATA?
1. Brings all features to same scale
2. Faster convergence in ML algorithms
3. Prevents features with larger values from dominating
"""

data = [10, 20, 30, 40, 50]
print(f"Original Data: {data}\n")

# Min-Max Normalization (scales to 0-1)
# Formula: (x - min) / (max - min)
min_val, max_val = min(data), max(data)
min_max_normalized = [(x - min_val) / (max_val - min_val) for x in data]
print(f"Min-Max Normalization (0-1): {min_max_normalized}")

# Z-Score Normalization (Standardization)
# Formula: (x - mean) / std_dev
mean = statistics.mean(data)
std_dev = statistics.stdev(data)
z_score_normalized = [(x - mean) / std_dev for x in data]
print(f"Z-Score Normalization: {[round(x, 2) for x in z_score_normalized]}")

# ============================================
# 11. PRACTICAL EXAMPLE: Student Performance Analysis
# ============================================
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Student Performance Analysis")
print("=" * 60)

students_marks = {
    'Math': [78, 85, 92, 65, 88, 72, 95, 80, 70, 83],
    'Science': [82, 78, 88, 70, 92, 68, 90, 75, 85, 80],
    'English': [75, 80, 85, 72, 78, 82, 88, 70, 76, 84]
}

print("\nSubject-wise Analysis:")
print("-" * 50)

for subject, marks in students_marks.items():
    print(f"\n{subject}:")
    print(f"  Mean: {statistics.mean(marks):.2f}")
    print(f"  Median: {statistics.median(marks)}")
    print(f"  Mode: {statistics.mode(marks)}")
    print(f"  Std Dev: {statistics.stdev(marks):.2f}")
    print(f"  Range: {max(marks) - min(marks)}")

# ============================================
# SUMMARY TABLE
# ============================================
print("\n" + "=" * 60)
print("SUMMARY: WHEN TO USE WHAT?")
print("=" * 60)
print("""
| Function          | Use Case                              |
|-------------------|---------------------------------------|
| Mean              | General average, symmetric data       |
| Median            | Skewed data, presence of outliers     |
| Mode              | Categorical data, most common value   |
| Std Deviation     | Measure spread/consistency            |
| Vector Normalize  | ML features, direction vectors        |
| Min-Max Scaling   | Scale to specific range (0-1)         |
| Z-Score           | Compare different distributions       |
| Geometric Mean    | Growth rates, percentages             |
| Harmonic Mean     | Rates, speed calculations             |
""")
