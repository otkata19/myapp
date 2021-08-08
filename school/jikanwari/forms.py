from django import forms

class HelloForm(forms.Form):
    data=[
        ('サンプル1', '1'),
        ('サンプル2', '2'),
        ('サンプル3', '3'),
    ]
    choice = forms.ChoiceField(label='プルダウンメニュー',choices=data)

class SmplForm(forms.Form):
    labels = ['静的単一選択','静的複数選択','動的単一選択','動的複数選択']
    three = forms.ChoiceField(
        required=True,
        disabled=False,
        widget=forms.Select(attrs={
            'id': 'three',}))    