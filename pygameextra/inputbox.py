from pygameextra import settings


class StandaloneInputBoxManager:
    def __init__(self):
        self.input_boxes = []
        self.previous_input_boxes = []
        self.active_input_box = None

    def update_input_boxes(self):
        if self.active_input_box and self.active_input_box not in self.input_boxes:
            self.active_input_box = None

    def push_input_boxes(self):
        self.input_boxes, self.previous_input_boxes = [], self.input_boxes

    def handle_input_boxes(self, event):
        if not self.active_input_box:
            return


class ContextualizedInputBoxManager:
    def __init__(self, set_as_context: bool = True):
        self.input_box_manager = StandaloneInputBoxManager()
        if set_as_context:
            settings.game_context = self
