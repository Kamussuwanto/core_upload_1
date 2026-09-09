




# /home/kamusc/myproject/core/forms.py
"""
from django import forms
from .models import Item

class ItemSubmissionForm(forms.ModelForm):
    class Meta:
        model = Item
        # Only expose user-safe inputs. Keep 'is_published' hidden so users can't auto-publish.
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;'}),
            'description': forms.Textarea(attrs={'rows': 4, 'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;'}),
        }


# /home/kamusc/myproject/core/forms.py
from django import forms
from .models import Item

class ItemSubmissionForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'image'] # Added image here
        # ... keep widgets as they were ...
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;'}),
            'description': forms.Textarea(attrs={'rows': 4, 'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;'}),
        }

"""
# /home/kamusc/myproject/core/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Item

class ItemSubmissionForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;'}),
            'description': forms.Textarea(attrs={'rows': 4, 'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px;'}),
        }

    # Custom validation rule for the 'image' field
    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            # Enforce limit in bytes: 2MB = 2 * 1024 * 1024
            max_size = 2 * 1024 * 1024

            if image.size > max_size:
                raise ValidationError(
                    f"The uploaded image is too large ({round(image.size / (1024*1024), 2)} MB). "
                    f"Maximum allowed file size is 2.0 MB."
                )

        return image