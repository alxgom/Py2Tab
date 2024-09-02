import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def colormap_to_hex_tex(cmap_name, num_colors, output_file):
    # Get the colormap
    cmap = plt.get_cmap(cmap_name)
    
    # Get colors from the colormap
    colors = [mcolors.rgb2hex(cmap(i / (num_colors - 1))) for i in range(num_colors)]
    
    # Write the colors to a .tex file
    with open(output_file, 'w') as f:
        f.write(f'<color-palette name="{cmap_name}" type="ordered-diverging">\n')
        for color in colors:
            f.write(f'  <color>{color}</color>\n')
        f.write('</color-palette>\n')

# Example usage
colormap_to_hex_tex('plasma', 12, 'colormap_colors.txt')