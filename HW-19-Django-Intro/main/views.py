from django.shortcuts import render
from django.views.generic import TemplateView
from .models import MenuItem, SliderItem


class IndexViewClass(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        menu_items = MenuItem.objects.all()
        slider_items = SliderItem.objects.all()

        context = {
            "menu_items": menu_items,
            "slider_items": slider_items,
        }
        return render(request,
                      template_name=self.template_name,
                      context=context)


# def main(request):
#     menu_items = MenuItem.objects.all()
#     return render(request, "index.html", {"menu_items": menu_items})
