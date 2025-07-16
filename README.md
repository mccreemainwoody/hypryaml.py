# hyprthemes

- [Installation](#installation)
- [Usage](#usage)
- [Create a theme](#create-a-theme)
  - [Hyprland](#hyprland)

A CLI utility tool to load Hyprland themes using YAML configurations.

This project is still very young and under development, so expect bugs and
issues. It is for now mostly a personal tool ; but if the project picks your
interest and gives you ideas for improvements, feel free to open an issue or a
pull request!

## Installation

For now, the project can be installed using `uv`: 

```bash
uv build
pip install dist/hyprthemes-X.Y.Z-py3-none-any.whl  # Replace X.Y.Z with the version number
```

## Usage

To use `hyprthemes`, you just need to give your configuration file as an
argument. That's all there is to it !

```bash
hyprthemes /path/to/your/config.yaml
```

## Create a theme

The configuration file is a YAML file that contains the theme settings.

Each node at the root of the file represents a configuration to apply over a
tool.

For now, only Hyprland is supported, but more tools can be added in the future.

### Hyprland

The YAML section dedicated to Hyprland allows you to dynamically override your
Hyprland configuration keywords.

To change a keyword, you just need to write it down as a key within the YAML
file with the value you want to set it to.

To reach a keyword within a section, go down within the hierarchy using YAML
sections.

For example, this configuration could be loaded to change the current border
and blur properties of Hyprland:

```yaml
hyprland:
  general:
    border_size: 1
    col.inactive_border: rgb(ff0000) rgb(ffff00) 45rad
    col.active_border: rgb(33ccff) rgb(00ff99) 45rad
  blur:
    enabled: true
    noise: 0.15
```
