from django import forms
from django.contrib.auth.forms import AuthenticationForm

#ログインフォームのデザインをBootstrapを対応
class LoginForm(AuthenticationForm):
    
    def __init__ (self, *args, **kwargs):

         #親クラスAuthenticationFormを初期化
        super().__init__(*args,**kwargs)

        #ユーザー名入力欄のデザインを設定
        self.fields["username"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"ユーザー名",
        })

        #パスワード入力欄のデザインを設定
        self.fields["password"].widget.attrs.update({
            "class":"form-control",
            "placeholder":"パスワード",
        })