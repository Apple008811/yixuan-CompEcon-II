import matplotlib.pyplot as plt
import numpy as np

def visualize_climbing_paths(n):
    def draw_paths_for_step(target, paths):
        plt.clf()  # Clear the current figure
        
        # Draw stairs and labels
        for i in range(target):
            plt.fill_between([i, i+1], [i, i], color='lightgray')
            plt.plot([i, i+1], [i, i], 'k-', linewidth=2)
            plt.plot([i, i], [i-1, i], 'k-', linewidth=2)
            # Add step labels
            plt.text(i+0.5, i-0.3, f'Step {i+1}', ha='center')
        
        # Draw all paths for this step with different colors, stopping at current height
        colors = plt.cm.rainbow(np.linspace(0, 1, len(paths)))
        for path, color in zip(paths, colors):
            x = np.arange(len(path))
            y = np.array(path)
            # Only plot up to current step height
            mask = y <= target
            plt.plot(x[mask], y[mask], '-', color=color, linewidth=2, alpha=0.7)
        
        plt.title(f'Step {target}: {len(paths)} possible paths')
        plt.xlabel('Step Number')
        plt.ylabel('Height')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.axis('equal')
        plt.pause(0.5)  # Reduce pause time between steps

    def generate_paths(current_step, target, current_path, all_paths):
        if current_step == target:
            all_paths.append(current_path[:])
            return
            
        if current_step + 1 <= target:
            current_path.append(current_step + 1)
            generate_paths(current_step + 1, target, current_path, all_paths)
            current_path.pop()
        if current_step + 2 <= target:
            current_path.append(current_step + 2)
            generate_paths(current_step + 2, target, current_path, all_paths)
            current_path.pop()
    
    plt.figure(figsize=(2, 2))  # Make all figures small and square
    
    # Show paths for each step from 1 to n
    for step in range(1, n + 1):
        paths = []
        print(f"\nShowing all possible paths for step {step}:")
        generate_paths(0, step, [0], paths)
        draw_paths_for_step(step, paths)
        
    plt.show()

# Demonstrate with 5 steps
visualize_climbing_paths(5)
