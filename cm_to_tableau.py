import argparse
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import sys

def colormap_to_tableau_palette(cmap_name, num_colors, output_file):
    """
    Generates a Tableau preferences file snippet from a matplotlib colormap.
    """
    try:
        # Get the colormap
        cmap = plt.get_cmap(cmap_name)
    except ValueError:
        print(f"Error: Colormap '{cmap_name}' not found in matplotlib.")
        print("Use --list to see available colormaps.")
        sys.exit(1)
    
    # Get colors from the colormap
    colors = [mcolors.rgb2hex(cmap(i / (num_colors - 1))) for i in range(num_colors)]
    
    # Write the colors to a .txt file (or stdout if preferred, but here file as requested)
    try:
        with open(output_file, 'w') as f:
            f.write(f'<color-palette name="{cmap_name}" type="ordered-diverging">\n')
            for color in colors:
                f.write(f'  <color>{color}</color>\n')
            f.write('</color-palette>\n')
        print(f"Successfully wrote palette '{cmap_name}' with {num_colors} colors to '{output_file}'.")
    except IOError as e:
        print(f"Error writing to file '{output_file}': {e}")
        sys.exit(1)

def list_colormaps():
    """Lists available matplotlib colormaps."""
    print("Available colormaps (partial list):")
    # There are many, let's just show some popular ones or all
    # For brevity in output, maybe just a few categories or print them all but user can grep
    # Let's print all valid names
    cmaps = sorted(plt.colormaps())
    for cm in cmaps:
        print(cm)

def main():
    parser = argparse.ArgumentParser(description="Generate a Tableau palette from a Matplotlib colormap.")
    
    parser.add_argument('cmap_name', nargs='?', help='Name of the matplotlib colormap (e.g., "viridis", "plasma").')
    parser.add_argument('-n', '--num_colors', type=int, default=12, help='Number of colors in the palette (default: 12).')
    parser.add_argument('-o', '--output', default='colormap_colors.txt', help='Output filename (default: colormap_colors.txt).')
    parser.add_argument('--list', action='store_true', help='List available colormaps and exit.')

    args = parser.parse_args()

    if args.list:
        list_colormaps()
        sys.exit(0)

    if not args.cmap_name:
        parser.print_help()
        sys.exit(1)

    colormap_to_tableau_palette(args.cmap_name, args.num_colors, args.output)

if __name__ == "__main__":
    main()
