import abc


class BrushObserver:
    """
    Implemented by all components which are dependent on changes of the Brush
    Uses the Observable pattern
    """

    def __init__(self, brush):
        self.brush = brush  # instance of the subject is kept in every Observable
        brush.attach(self)

    @abc.abstractmethod
    def update_brush(self):
        """
        Triggered by the brush if it's internal state has changed, uses the pull method of the Observer pattern
        :return: No return value
        """
        pass
