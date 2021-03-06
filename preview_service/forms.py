from django import forms

class previewConfigForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    pdftoppm_path = forms.CharField(required=True,
                               label="pdftoppm binary",
                               initial='/usr/bin/pdftoppm',
                               widget=forms.TextInput(),
                               help_text="Full path to pdftoppm binary.")

    def __init__(self, *args, **kwargs):
        super(previewConfigForm, self).__init__(*args, **kwargs)
