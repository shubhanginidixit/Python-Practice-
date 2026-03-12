import cProfile
import pstats

# Function to analyze
def slow_function():
    total = 0
    for i in range(5000):
        for j in range(5000):
            total += i * j
    return total

# Run profiler
profiler = cProfile.Profile()
profiler.enable()

slow_function()

profiler.disable()

# Print profiling statistics
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)