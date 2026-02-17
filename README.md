# Py2Tab

Py2Tab is a simple tool to generate custom Tableau color palettes from Matplotlib colormaps.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd Py2Tab
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line:

```bash
python cm_to_tableau.py <colormap_name> [-n <number_of_colors>] [-o <output_file>]
```

### Examples

Generate a palette from the "plasma" colormap with 12 colors (default):

```bash
python cm_to_tableau.py plasma
```

Generate a palette from "viridis" with 20 colors:

```bash
python cm_to_tableau.py viridis -n 20
```

List available colormaps:

```bash
python cm_to_tableau.py --list
```

## How to use in Tableau

The script generates a text file (default: `colormap_colors.txt`) containing an XML snippet like this:

```xml
<color-palette name="plasma" type="ordered-diverging">
  <color>#0d0887</color>
  <color>#3e049c</color>
  <!-- ... more colors ... -->
  <color>#f0f921</color>
</color-palette>
```

To use this palette in Tableau:

1. Locate your **My Tableau Repository** folder (usually in `Documents/My Tableau Repository`).
2. Open the `Preferences.tps` file in a text editor.
3. Paste the generated `<color-palette>...</color-palette>` block inside the `<preferences>...</preferences>` tags.
4. Restart Tableau. The new palette will appear in the color selection menu.

## About the Author

Check out more projects at [my portfolio](https://alexisgomel.com/projects).
