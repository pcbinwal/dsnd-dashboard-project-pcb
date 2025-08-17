from .combined_component import CombinedComponent
from fasthtml.common import Button, Form, Group

class FormGroup(CombinedComponent):

    id = ""
    action = ""
    method = ""
    children = []
    button_label = "Refresh"

    def call_children(self, userid, model):
        children = super().call_children(userid, model)
        children.append(Button(self.button_label))

        return children

    def outer_div(self, children, div_args):

        return Form(Group(*children), **div_args, align="center")
    
    def div_args(self, userid, model):

        return {
            'id': self.id,
            'action': self.action,
            'method': self.method,
            }