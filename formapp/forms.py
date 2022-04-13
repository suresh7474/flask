from django import forms

class Employee_forms(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField()
    email=forms.EmailField()

    def clean(self):
        print('Clean validation password ')
        tota_cleaned_data=super().clean()
        eamil_=tota_cleaned_data['email']
        if len(eamil_)<10:
            print(len(eamil_))

            print('ssssssssssss')
            raise forms.ValidationError('The email field should not be >3')
            return
