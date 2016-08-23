import sublime, sublime_plugin


class ShowFilenameInStatus(sublime_plugin.EventListener):
    def on_activated_async(self, view):
        filename = '/'.join(['...'] + view.file_name().split('/')[-3:])
        if filename is None:
            view.erase_status('_filename')
        else:
            view.set_status('_filename', "File: " + filename)
