import json

from django.shortcuts import render

from library.models import Book, Inv, Author
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse


# reate your views here.
def inventory_number_management(request, pk):
    start_range = ''
    end_range = ''
    book = Book.objects.get(id_book=pk)
    existing_inventories = None


    context = {
        'start_range': start_range,
        'end_range': end_range,
        'book': book,
        'text': existing_inventories,
    }
    return render(request, 'inventory_number_management/inventory_number_management.html', context)


def get_inventory_number_list(request, book_id):
    #items = Inv.objects.all().values('num')
    book = Book.objects.get(id_book=book_id)
    items = book.inv.values_list('id_in', 'num')
    return JsonResponse(list(items), safe=False)


def add_inventory_number(request, book_id):
    if request.method == 'POST':
        try:
            # Получение данных из тела запроса
            data = json.loads(request.body)

            # Получение значения inv из тела запроса
            start_range = data.get('startRange')
            end_range = data.get('endRange')

            if not start_range.isdigit() or not end_range.isdigit():
                return JsonResponse({'error': 'Only digits you can use'}, status=400)

            rangeNumbers = range(int(start_range), int(end_range) + 1)

            # Получаем из базы инв. номера, которые уже существуют в таблице Inv (просто существующие и привязанные к книге)
            existing_inventories = Inv.objects.filter(num__in=rangeNumbers).values_list('num', flat=True)

            # Получаем список инвентарных номеров, которые привязаны к книге
            binded_inventory_numbers = Book.objects.filter(inv__in=existing_inventories).values_list('inv__num', flat=True)

            if not binded_inventory_numbers.exists():
                book = Book.objects.get(id_book=book_id)
                for number in rangeNumbers:
                    inv, created = Inv.objects.get_or_create(num=number)
                    book.inv.add(inv)

            return JsonResponse({'success': True, 'inventory_number': list(rangeNumbers)})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def check_inventory_number_exists(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_range = data.get('startRange')
        end_range = data.get('endRange')
        rangeNumbers = range(int(start_range), int(end_range) + 1)

        # Получаем из базы инв. номера, которые уже существуют в таблице Inv (просто существующие и привязанные к книге)
        existing_inventories = Inv.objects.filter(num__in=rangeNumbers)

        # Получаем список инвентарных номеров, которые привязаны к книге
        binded_inventory_numbers = Book.objects.filter(inv__in=existing_inventories).values_list('inv__num', flat=True)

        return JsonResponse(list(binded_inventory_numbers), safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


""" 

    if request.method == 'POST':
        start_range = int(request.POST.get('start_range'))
        end_range = int(request.POST.get('end_range'))
        rangeNumbers = range(start_range, end_range + 1)

        existing_inventories = (Inv.objects.filter(num__in=rangeNumbers))

        if not existing_inventories.exists():
            for number in rangeNumbers:
                inv = Inv(num=number)
                inv.save()
                book.inv.add(inv)


def inventory_number_management(request, pk):
    start_range = ''
    end_range = ''
    book = Book.objects.get(id_book=pk)
    existing_inventories = None

    if request.method == 'POST':
        start_range = int(request.POST.get('start_range'))
        end_range = int(request.POST.get('end_range'))
        rangeNumbers = range(start_range, end_range + 1)

        existing_inventories = (Inv.objects.filter(num__in=rangeNumbers))

        if not existing_inventories.exists():
            for number in rangeNumbers:
                inv = Inv(num=number)
                inv.save()
                book.inv.add(inv)


    context = {
        'start_range': start_range,
        'end_range': end_range,
        'book': book,
        'text': existing_inventories,
    }
    return render(request, 'index.html', context)


"""