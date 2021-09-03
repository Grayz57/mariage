from otree.forms.widgets import BaseWidget


class SliderInput(BaseWidget):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.default = self.__dict__.get('default', False)
        self.output = self.__dict__.get('output', True)
        self.step = self.__dict__.get('step', 1)

    def event_listeners(self):
        event_listeners = str()
        if not self.default:
            event_listeners += f'onclick=this.classList.remove("otree-slider-no-default") '
        # if self.output:
        #     event_listeners += f'oninput={self.field.id}_output.value=this.value ' \
        #                        f'onchange={self.field.id}_output.value=this.value'
        return event_listeners

    def get_html_fragments(self):
        if type(self.__dict__.get('field')).__name__ == 'IntegerField' and not isinstance(self.step, int):
            self.step = round(self.step, 0)
        else:
            self.render_kw['step'] = self.step
        widget = '<div class="otree-form-slider">'
        if self.output:
            widget += f'<div class="otree-slider-output"><output id="{self.field.id}_output"></output></div>'
        if self.default:
            widget += f'<div class="otree-slider-container">' \
                      f'<div class="otree-slider-min">{self.render_kw.get("min", 0)}</div>' \
                      f'<input type="range" class="form-control otree-slider" {self.attrs()} {self.event_listeners()}>' \
                      f'<div class="otree-slider-max">{self.render_kw.get("max", 100)}</div>' \
                      f'</div>'
        else:
            widget += f'<div class="otree-slider-container">' \
                      f'<div class="otree-slider-min">{self.render_kw.get("min", 0)}</div>' \
                      f'<input type="range" class="form-control otree-slider otree-slider-no-default" ' \
                      f'{self.attrs()} {self.event_listeners()}>' \
                      f'<div class="otree-slider-max">{self.render_kw.get("max", 100)}</div>' \
                      f'</div>'
        widget += '</div>'
        yield widget