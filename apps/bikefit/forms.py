from django import forms


class MedidasForm(forms.Form):
    cavalo = forms.CharField(
        label="Cavalo: uma das medidas mais importantes para determinar o tamanho do quadro. Fique totalmente "
        "encostado na parede e use um livro ou algo do tipo entre as pernas, o mais alto que puder, para medir "
        "a distancia do chao ate o topo do objeto usado.",
        required=True,
        max_length=6,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "style": "max-width: 100px",
            },
        ),
    )
    esterno = forms.CharField(
        label="Esterno: esta medida servira para, junto com o tamanho do braço, determinar o comprimento total "
        "do quadro + mesa. Mede-se do chao ate a parte inferior da marca em V que temos acima do peito,"
        "onde fica o osso chamado esterno.",
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "style": "max-width: 100px",
            }
        ),
    )
    braco = forms.CharField(
        label="Braço: estique o braço com o polegar para cima para medir conforme a foto ao lado. ",
        required=True,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "style": "max-width: 100px"}
        ),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "style": "max-width: 400px"}
        ),
    )

    def clean_cavalo(self):
        cavalo = self.cleaned_data.get("cavalo").strip()
        if float(cavalo) < 10 or float(cavalo) > 150:
            raise forms.ValidationError("Confira suas medidas, algo está errado")
        else:
            return cavalo

    def clean_esterno(self):
        esterno = self.cleaned_data.get("esterno").strip()
        if float(esterno) < 10 or float(esterno) > 300:
            raise forms.ValidationError("Confira suas medidas, algo está errado.")
        else:
            return esterno

    def clean_braco(self):
        braco = self.cleaned_data.get("braco").strip()
        if float(braco) < 10 or float(braco) > 150:
            raise forms.ValidationError("Confira suas medidas, algo está errado")
        else:
            return braco

    def clean_email(self):
        email = self.cleaned_data.get("email").strip()
        if len(email) > 0 and "@" not in email:
            raise forms.ValidationError("Este não é um email válido")
        else:
            return email


class MuralForm(forms.Form):
    nome = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "max-width: 400px",
                "placeholder": "seu nome",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "style": "max-width: 400px",
                "placeholder": "seu e-mail",
            }
        ),
    )
    mensagem = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "style": "max-width: 600px",
                "placeholder": "sua mensagem",
                "rows": 4,
            }
        ),
    )

    def clean_nome(self):
        nome = self.cleaned_data.get("nome").strip()
        if "www" in nome or "http" in nome:
            raise forms.ValidationError("nome inválido")
        else:
            return nome

    def clean_email(self):
        email = self.cleaned_data.get("email").strip()
        if len(email) > 0 and "@" not in email:
            raise forms.ValidationError("email inválido")
        else:
            return email

    def clean_mensagem(self):
        mensagem = self.cleaned_data.get("mensagem").strip()
        if "href" in mensagem:
            raise forms.ValidationError("sua mensagem possui caracteres proibidos.")
        else:
            return mensagem
