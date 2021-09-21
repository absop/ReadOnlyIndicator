# ReadOnlyIndicator

A plugin for Sublime Text to toggle the **read-only** mode of view, and indicate whether the view is read only or not.

## Command
```json
[
  {
    "caption": "ReadOnlyIndicator: Toggle Read Only",
    "command": "toggle_read_only"
  }
]
```

## Settings
```json
{
    "readonly_indicator": "🔒",
    "editable_indicator": "🔓"
}
```

You can change the `indicators` from emojis to plain strings or empty strings.
