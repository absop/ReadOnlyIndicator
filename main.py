import sublime
import sublime_plugin


class ToggleReadOnlyCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.set_read_only(not self.view.is_read_only())
    indicator.show_read_only_status(self.view)


class ReadOnlyIndicator(sublime_plugin.EventListener):
    def on_new_async(self, view):
        indicator.show_read_only_status(view)

    def on_load_async(self, view):
        indicator.show_read_only_status(view)


class Indicator():
    status_key = '__read_only'

    def __init__(self, settings_name='ReadOnlyIndicator.sublime-settings'):
        self.settings_name = settings_name

    def __getitem__(self, readonly: bool):
        return self.readonly_emoji if readonly else self.editable_emoji

    def stop(self):
        self.iter_views(self.clear_read_only_status)

    def start(self):
        settings = sublime.load_settings(self.settings_name)
        settings.add_on_change('readonly_indicator',
            lambda: self.update_read_only_status(settings))
        self.update_read_only_status(settings)

    def load_emojis(self, settings):
        self.readonly_emoji = settings.get('readonly_indicator', '🔒')
        self.editable_emoji = settings.get('editable_indicator', '🔓')

    def update_read_only_status(self, settings):
        self.load_emojis(settings)
        self.iter_views(self.show_read_only_status)

    def show_read_only_status(self, view):
        view.set_status(self.status_key, self[view.is_read_only()])

    def clear_read_only_status(self, view):
        view.erase_status(self.status_key)

    def iter_views(self, f):
        for window in sublime.windows():
            for view in window.views():
                f(view)


indicator = Indicator()


def plugin_loaded():
    sublime.set_timeout_async(indicator.start, 0)


def plugin_unloaded():
    sublime.set_timeout_async(indicator.stop, 0)
