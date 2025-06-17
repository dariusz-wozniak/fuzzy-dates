import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from datetime import datetime, timedelta

def plot_normal_distribution():
    # Generate data for normal distribution
    x = np.linspace(2017, 2029, 1000)
    y = stats.norm.pdf(x, loc=2023, scale=2)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.fill_between(x, y, alpha=0.3)
    plt.title('Normal Distribution (μ=2023, σ=2)')
    plt.xlabel('Year')
    plt.ylabel('Probability Density')
    plt.grid(True, alpha=0.3)
    plt.savefig('normal_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_uniform_distribution():
    # Generate data for uniform distribution
    start_date = datetime(2024, 6, 1)
    end_date = datetime(2024, 6, 30)
    days = (end_date - start_date).days
    
    x = np.linspace(0, days, 1000)
    y = stats.uniform.pdf(x, loc=0, scale=days)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'g-', linewidth=2)
    plt.fill_between(x, y, alpha=0.3)
    plt.title('Uniform Distribution (June 2024)')
    plt.xlabel('Days from June 1, 2024')
    plt.ylabel('Probability Density')
    plt.grid(True, alpha=0.3)
    plt.savefig('uniform_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_triangular_distribution():
    # Generate data for triangular distribution
    x = np.linspace(1801, 1900, 1000)
    y = stats.triang.pdf((x - 1801) / (1900 - 1801), c=(1850 - 1801) / (1900 - 1801))
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'r-', linewidth=2)
    plt.fill_between(x, y, alpha=0.3)
    plt.title('Triangular Distribution (19th Century)')
    plt.xlabel('Year')
    plt.ylabel('Probability Density')
    plt.grid(True, alpha=0.3)
    plt.savefig('triangular_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    plot_normal_distribution()
    plot_uniform_distribution()
    plot_triangular_distribution() 